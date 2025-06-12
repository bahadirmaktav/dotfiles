#!/bin/bash

CHOICE=$(echo -e "Shutdown\nReboot\nSuspend\nLogout" | wofi --dmenu --prompt "Power")

case "$CHOICE" in
  Shutdown)
    systemctl poweroff
    ;;
  Reboot)
    systemctl reboot
    ;;
  Suspend)
    systemctl suspend
    ;;
  Logout)
    hyprctl dispatch exit
    ;;
  *)
    # Cancel or unknown choice, do nothing
    ;;
esac
