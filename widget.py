from libqtile import widget
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget import modify
from widgets.nvidia import NvidiaGPU
from qtile_extras.widget.decorations import RectDecoration



colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"],
]
decor = {
    "decorations": [
        RectDecoration(colour="#355E3B", radius=13, filled=True, padding_y=0)
    ],
}


def get_widgets(net=False):
    cust_spacer = widget.Spacer(length=5)

    w = [
        widget.Image(
            # font=font1,
            filename="~/.config/qtile/icons/python.png",
            padding=0,
            fontsize=16,
            mouse_callbacks={"Button1": lazy.reload_config()},
            **decor,
        ),
        cust_spacer,
        widget.Clock(
            foreground=colors[6],
            fontsize=14,
            format="    %d/%m/%y   %I:%M %p  ",
            # format="%A, %B %d - %I:%M %p",
            **decor,
        ),
        cust_spacer,
        widget.Backlight(
            foreground=colors[4],
            fontsize=14,
            backlight_name="intel_backlight",
            padding=0,
            change_command="xbacklight -set {0}",
            format="    {percent:2.0%}  ",
            # fontsize=16,
            **decor,
        ),
        widget.Spacer(),
        widget.GroupBox(
            fontsize=16,
            # margin_y=2,
            # margin_x=10,
            padding_y=0,
            padding_x=4,
            borderwidth=4,
            disable_drag=True,
            active=colors[5],
            inactive=colors[7],
            rounded=False,
            # highlight_color=colors[5],
            highlight_method="text",
            this_current_screen_border=colors[6],
            other_current_screen_border=colors[5],
            this_screen_border=colors[4],
            foreground=colors[2],
            **decor,
        ),
        widget.Spacer(),
        widget.CurrentLayout(
            fmt="  {}  ",
            fontsize=12,
            foreground=colors[2],
            **decor,
        ),
        cust_spacer,
    ]

    if net:
        w.extend(
            [
                widget.Net(
                    # interface="enp6s0",
                    format="  Net: {down} ↓↑ {up}  ",
                    foreground=colors[3],
                    **decor,
                ),
                cust_spacer,
            ]
        )
    w.extend(
        [
            modify(
                NvidiaGPU,
                foreground=colors[8],
                fontsize=12,
                sensors=["utilization.gpu", "temperature.gpu"],
                format="  GPU {utilization_gpu}% {temperature_gpu}°C  ",
                **decor,
            ),
            cust_spacer,
            widget.CPU(
                foreground=colors[4],
                fontsize=12,
                format="  CPU: {load_percent:3.0f}%  ",
                **decor,
            ),
            cust_spacer,
            # widget.ThermalSensor(
            #     foreground=colors[4],
            #     fromat="{temp:.1f}{unit}",
            #     **decor,
            # ),
            # cust_spacer,
            widget.Battery(
                fontsize=12,
                foreground=colors[7],
                format="  {char} {percent:2.0%}  ",
                charge_char="󰂄",
                discharge_char="󰂂",
                empty_char="󰂎",
                full_char="󰁹",
                unknown_char="󱈑",
                update_interval=60,
                **decor,
            ),
            cust_spacer,
            widget.TextBox(
                text="  ",
                fontsize=14,
                foreground="#d36969",
                mouse_callbacks={"Button1": lazy.spawn('/home/hillalkr/.local/bin/powermenu')},
                **decor,
            ),
        ]
    )
    return w
