# Dotfiles

A minimal, modern Wayland desktop environment built around **Hyprland** with dynamic theming powered by **pywal**. This configuration provides a fast, responsive, and visually cohesive desktop experience with seamless color synchronization across all components.

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

---

## Overview

This dotfiles repository contains configurations for a complete desktop environment stack:

- **Hyprland**: A modern Wayland compositor with dynamic tiling and floating window management
- **Kitty**: GPU-accelerated terminal emulator with true color support
- **Fish**: User-friendly shell with excellent autocomplete and syntax highlighting
- **Oh My Posh**: Cross-platform prompt engine with customizable themes
- **Waybar**: Highly customizable Wayland status bar with system information
- **Rofi**: Fast, lightweight application launcher and menu system
- **Pywal**: Automatic color palette generation from wallpapers

The setup uses **pywal** to extract color palettes from wallpapers and automatically apply them across all components, creating a unified visual theme that adapts to your wallpaper.

---

## System Requirements

### Operating Systems
- **Linux** with Wayland support (tested on Arch)

### Dependencies
| Category        | Requirement                                                            |
| --------------- | ---------------------------------------------------------------------- |
| **GPU Drivers** | NVIDIA (with proprietary drivers), AMD, or Intel GPU drivers          |
| **Display**     | Wayland-compatible display with at least 1920x1080 resolution         |
| **Python**      | Python 3.8+ (for pywal color generation script)                       |
| **Font**        | JetBrainsMono Nerd Font (or customize in configs)                     |

### Hardware (Recommended)
- Multi-monitor setup (tested with 2x 1920x1080)
- USB mouse/keyboard for Hyprland input configuration
- Audio device (for Waybar audio controls)

---

## Quick Start

### Minimal Setup (30 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/bahadirmaktav/dotfiles.git
cd dotfiles

# 2. Install required packages
# For Arch/Manjaro:
sudo pacman -S hyprland hyprlock hyprpaper kitty fish rofi waybar python-pywal

# For Ubuntu/Debian:
sudo apt install hyprland hyprlock hyprpaper kitty fish rofi waybar python3-pywal

# 3. Install fonts
sudo pacman -S ttf-jetbrains-mono-nerd  # or download from nerd-fonts.com

# 4. Deploy configurations
cp -r .config/* ~/.config/

# 5. Set Fish as default shell
chsh -s /usr/bin/fish
```

Then **log out and back in** to start Hyprland.

---

## Installation

### Step 1: Install Dependencies

Choose your distribution and install all required tools:

<details>
<summary><b>Arch Linux / Manjaro</b></summary>

```bash
sudo pacman -S \
  hyprland hyprlock hyprpaper \
  kitty rofi waybar \
  fish oh-my-posh \
  python-pywal \
  ttf-jetbrains-mono-nerd \
  pavucontrol
```

</details>

<details>
<summary><b>Ubuntu / Debian</b></summary>

```bash
sudo apt update && sudo apt install \
  hyprland hyprlock hyprpaper \
  kitty rofi waybar \
  fish fonts-jetbrains-mono \
  oh-my-posh python3-pywal \
  pavucontrol
```

Note: Hyprland may need to be installed from testing/unstable repos or built from source.

</details>

<details>
<summary><b>Fedora / RHEL</b></summary>

```bash
sudo dnf install \
  hyprland hyprlock hyprpaper \
  kitty rofi waybar \
  fish python3-pywal \
  java-fonts \
  pavucontrol
```

</details>

### Step 2: Clone and Deploy Configurations

```bash
# Clone this repository
git clone https://github.com/bahadirmaktav/dotfiles.git
cd dotfiles

# Option A: Copy files directly (non-destructive)
cp -r .config/* ~/.config/

# Option B: Use GNU Stow (creates symlinks for easier updates)
# First install stow: sudo pacman -S stow (or apt install stow)
stow .
```

**Option B (Stow) is recommended** as it allows you to update this repo and have changes reflected immediately in your home directory.

### Step 3: Configure Hardware

Edit `.config/hypr/hyprland.conf` to match your setup:

```bash
# Find your monitor names
wlr-randr  # or alternatively: hyprctl monitors

# Update the monitor configuration
monitor=DP-1,preferred,1920x0,1
monitor=HDMI-A-2,preferred,0x0,1
```

### Step 4: Set Default Shell

```bash
# Change default shell to Fish
chsh -s /usr/bin/fish

# Log out and log back in for changes to take effect
```

### Step 5: Install and Configure Oh My Posh

```bash
# Oh My Posh is usually auto-installed with package managers
# If not, install manually:
curl -s https://ohmyposh.dev/install/linux.sh | bash -s -- -d ~/local/bin

# The config is already set up at: .config/oh-my-posh/huvix.omp.json
```

---

## Configuration

### Directory Structure

```
.config/
├── fish/                 # Fish shell configuration
│   ├── config.fish      # Main shell config
│   ├── conf.d/          # Auto-load configs
│   ├── functions/       # Custom functions
│   └── completions/     # Custom completions
├── hypr/                 # Hyprland window manager
│   ├── hyprland.conf    # Main compositor config
│   ├── hyprcolors.conf  # Generated color variables
│   ├── hyprlock.conf    # Lock screen config
│   └── hyprpaper.conf   # Wallpaper daemon config
├── kitty/                # Terminal emulator
│   ├── kitty.conf       # Main terminal config
│   └── kitty_colors.conf # Generated color scheme
├── rofi/                 # Application launcher
│   ├── launcher.rasi    # Launcher theme
│   ├── powermenu.rasi   # Power menu theme
│   └── colors.rasi      # Generated colors
├── waybar/               # Status bar
│   ├── config.jsonc     # Bar configuration
│   ├── style.css        # Styling
│   └── colors.css       # Generated colors
├── oh-my-posh/           # Shell prompt configuration
│   └── huvix.omp.json   # Prompt theme
└── wal/
    └── scripts/
        └── set_theme.py  # Color generation script
```

### Component Details

#### Hyprland (Window Manager)

**Key Settings** in `hyprland.conf`:
- **Monitor setup**: Configure dual/multi-monitor with `monitor=` directives
- **GPU support**: NVIDIA/AMD drivers preconfigured
- **Gaps & borders**: Adjustable window spacing and borders (`gaps_in=4`, `gaps_out=8`)
- **Animations**: Smooth transitions (bezier curves, animations enabled)
- **Dwindle layout**: Tiling algorithm for automatic window arrangement

**Edit monitors:**
```bash
# List connected displays
hyprctl monitors

# Update in hyprland.conf
monitor=DP-1,preferred,1920x0,1  # Right monitor at 1920px offset
monitor=HDMI-A-2,preferred,0x0,1 # Left monitor at 0px offset
```

#### Kitty (Terminal)

**Features**:
- GPU-accelerated rendering for smooth scrolling
- True color (24-bit) support
- Font: JetBrainsMono Nerd Font (size 10)
- Drop-down opacity via pywal integration

**Customize**:
```bash
# Change font size (in ~.config/kitty/kitty.conf)
font_size 10.0

# Font options
font_family family="JetBrainsMono Nerd Font Mono"
```

#### Fish Shell

**Advantages over Bash/ZSH**:
- Syntax highlighting as you type
- Smart autocompletion
- Friendly error messages
- No startup script bloat

**Config location**: `~/.config/fish/config.fish`

#### Waybar (Status Bar)

**Modules displayed**:
- **Left**: Application launcher
- **Center**: Workspace indicators
- **Right**: CPU, Memory, Disk, Temperature, Audio, Clock, Power menu

**Multi-monitor note**: Currently configured for `DP-1` (right monitor). Edit `config.jsonc` to adjust for your setup.

#### Rofi (Application Launcher)

**Features**:
- Application launcher (`drun`)
- Command runner (`run`)
- File browser (`filebrowser`)
- Power menu with shutdown/reboot/logout

**Keybinds**:
- `Super+R`: Open launcher
- `Super+M`: Open power menu

#### Oh My Posh (Shell Prompt)

Current theme: `huvix.omp.json`

Shows:
- Current directory
- Git branch and status
- Python virtual environment
- Execution time and exit status

**Customize theme**: Edit `~/.config/oh-my-posh/huvix.omp.json` or download themes from [ohmyposh.dev](https://ohmyposh.dev).

---

## Usage

### Dynamic Color Theming with Pywal

The most powerful feature of this setup is automatic theme generation from wallpapers.

#### How It Works

1. **Pywal** analyzes your wallpaper and extracts a cohesive color palette
2. **set_theme.py** applies these colors to all configuration files
3. **Components reload** automatically (Hyprland, Kitty, Waybar, Rofi)

#### Apply a New Theme

```bash
# Apply colors from a wallpaper
python ~/.config/wal/scripts/set_theme.py ~/Pictures/my_wallpaper.jpg

# The script automatically:
# - Generates colors with pywal
# - Updates Hyprland color variables
# - Updates Kitty terminal colors
# - Updates Waybar status bar colors
# - Updates Rofi launcher colors
# - Sets wallpaper in hyprpaper
# - Reloads all affected applications
```

#### What Gets Updated

| Component | File Updated          | What Changes              |
| --------- | --------------------- | ------------------------- |
| Hyprland  | `hyprcolors.conf`     | Border colors, shadows    |
| Kitty     | `kitty_colors.conf`   | Terminal background, text |
| Waybar    | `colors.css`          | Bar background, modules   |
| Rofi      | `colors.rasi`         | Launcher/Menu colors      |
| Wallpaper | `hyprpaper.conf`      | Active wallpaper path     |

---