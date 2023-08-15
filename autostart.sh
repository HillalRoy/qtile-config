#!/usr/bin/env bash 
lxsession & # x11 session manager
picom -b &
killall volumeicon &
nm-applet &

dunst & # Notification demon

~/.config/qtile/scripts/display &


sleep 3 && volumeicon &
ulauncher &
