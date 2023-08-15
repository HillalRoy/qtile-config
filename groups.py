from libqtile.config import Group, Key
from libqtile.lazy import lazy
from keybinding import keys, mod


group_labels = ["", "", "", "", "", "", "", "", "ﬁ"]

groups = [Group(i) for i in group_labels]

for i, g in enumerate(groups, 1):
    keys.extend(
        [
            Key(
                [mod],
                str(i),
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(g.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
        ]
    )
