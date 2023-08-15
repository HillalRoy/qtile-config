#!/usr/bin/env bash 

n_monitor=`xrandr --listmonitors | head -n1 | cut -d ":"  -f 2`

nargs="--bg-fill --randomize `echo ~/Pictures/aesthetic-wallpapers/images/*.jpg`"
args=''
for i in `seq $n_monitor`
do
    args="$args $nargs"
done

echo n_monitor $n_monitor
feh $args
