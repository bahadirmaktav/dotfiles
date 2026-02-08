#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path


# -----------------------------
# Paths
# -----------------------------
HOME = Path.home()
WAL_COLORS = HOME / ".cache/wal/colors.json"

HYPR_COLORS = HOME / ".config/hypr/hyprcolors.conf"
KITTY_COLORS = HOME / ".config/kitty/kitty_colors.conf"
WAYBAR_COLORS = HOME / ".config/waybar/colors.css"
HYPRPAPER_CONF = HOME / ".config/hypr/hyprpaper.conf"
ROFI_COLORS = HOME / ".config/rofi/colors.rasi"


# -----------------------------
# Helpers
# -----------------------------
def hex_to_rgba(hex_color: str, alpha: float = 1.0) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"


def hex_to_rgba_hypr(hex_color: str, alpha_hex: str = "FF") -> str:
    hex_color = hex_color.lstrip("#").upper()
    return f"rgba({hex_color}{alpha_hex})"


def load_wal_colors():
    with open(WAL_COLORS) as f:
        return json.load(f)


# -----------------------------
# Run wal
# -----------------------------
def run_wal(wallpaper_path: Path):
    subprocess.run(["wal", "-i", str(wallpaper_path)], check=True)


# -----------------------------
# Hyprland colors
# -----------------------------
def update_hyprcolors(colors):
    background = colors["special"]["background"]
    foreground = colors["special"]["foreground"]

    color_background = hex_to_rgba_hypr(background, "FF")
    color_active = hex_to_rgba_hypr(foreground, "FF")
    color_inactive = hex_to_rgba_hypr(foreground, "80")

    content = f"""$colorBackground = {color_background}
$colorActiveBorder = {color_active}
$colorInactiveBorder = {color_inactive}
$colorShadow = rgba(1A1A1AEE)
"""

    with open(HYPR_COLORS, "w") as f:
        f.write(content)


# -----------------------------
# Kitty colors
# -----------------------------
def update_kitty_colors(colors):
    background = colors["special"]["background"]
    foreground = colors["special"]["foreground"]

    content = f"""background {background}
foreground {foreground}
"""

    with open(KITTY_COLORS, "w") as f:
        f.write(content)


# -----------------------------
# Waybar colors
# -----------------------------
def update_waybar_colors(colors):
    background = colors["special"]["background"]
    foreground = colors["special"]["foreground"]

    bg_rgba = hex_to_rgba(background, 0.75)
    active_rgba = hex_to_rgba(foreground, 1.0)
    inactive_rgba = hex_to_rgba(foreground, 0.5)

    content = f"""@define-color colorBackground {bg_rgba};
@define-color colorActiveText {active_rgba};
@define-color colorInactiveText {inactive_rgba};
"""

    with open(WAYBAR_COLORS, "w") as f:
        f.write(content)


# -----------------------------
# Hyprpaper wallpaper update
# -----------------------------
def path_to_tilde(path: Path) -> str:
    """
    Convert /home/user/... → ~/...
    """
    home = str(Path.home())
    path_str = str(path)
    if path_str.startswith(home):
        return path_str.replace(home, "~", 1)
    return path_str


def update_hyprpaper(wallpaper_path: Path):
    if not HYPRPAPER_CONF.exists():
        return

    display_path = path_to_tilde(wallpaper_path)

    lines = HYPRPAPER_CONF.read_text().splitlines()
    new_lines = []

    for line in lines:
        if "path =" in line:
            indent = line.split("path")[0]
            new_lines.append(f"{indent}path = {display_path}")
        else:
            new_lines.append(line)

    HYPRPAPER_CONF.write_text("\n".join(new_lines))


# -----------------------------
# Reload programs
# -----------------------------
def reload_programs():
    subprocess.run(["hyprctl", "reload"],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    subprocess.run(["kitty", "@", "set-colors", "-a", str(KITTY_COLORS)],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    subprocess.run(["pkill", "waybar"],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    subprocess.Popen(["waybar"])

    subprocess.run(
        ["pkill", "hyprpaper"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    subprocess.Popen(["hyprpaper"])


# -----------------------------
# Rofi colors
# -----------------------------
def update_rofi_colors(colors):
    background = colors["special"]["background"]
    foreground = colors["special"]["foreground"]

    color0 = colors["colors"]["color0"]
    color1 = colors["colors"]["color1"]
    color2 = colors["colors"]["color2"]
    color3 = colors["colors"]["color3"]

    content = f"""* {{
    background:     {background}FF;
    background-alt: {color0}FF;
    foreground:     {foreground}FF;
    selected:       {color3}FF;
    active:         {color2}FF;
    urgent:         {color1}FF;
}}
"""

    with open(ROFI_COLORS, "w") as f:
        f.write(content)

    print("Rofi colors updated.")



# -----------------------------
# Main
# -----------------------------
def main():
    if len(sys.argv) != 2:
        print("Usage: set_theme.py /path/to/wallpaper")
        sys.exit(1)

    wallpaper = Path(sys.argv[1]).expanduser().resolve()

    if not wallpaper.exists():
        print("Wallpaper not found:", wallpaper)
        sys.exit(1)

    # 1. Run wal
    run_wal(wallpaper)

    # 2. Load colors
    colors = load_wal_colors()

    # 3. Update configs
    update_hyprcolors(colors)
    update_kitty_colors(colors)
    update_waybar_colors(colors)
    update_rofi_colors(colors)
    update_hyprpaper(wallpaper)

    # 4. Reload programs
    reload_programs()

    print("Theme applied:", wallpaper)


if __name__ == "__main__":
    main()
