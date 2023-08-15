from libqtile import layout, hook
from libqtile.log_utils import logger
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy
from screens import screens, topbar
from keybinding import keys, mod
from layouts import layouts
from groups import groups
from os import path
import subprocess

home = path.expanduser("~")
logger.setLevel('INFO')

def set_wallpaper():
    subprocess.call([home + "/.config/qtile/wall.sh"])

set_wallpaper()

@hook.subscribe.screens_reconfigured
def ss_reconfigured():
    from libqtile import qtile
    qtile.cmd_reload_config()


@hook.subscribe.client_new
def dialogs(window):
    if (
        window.window.get_wm_type() == "dialog"
        or window.window.get_wm_transient_for()
        or window.name == "splash"
    ):
        window.floating = True


@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + "/.config/qtile/autostart.sh"])


widget_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
