from libqtile import bar
from libqtile.config import Screen
from widget import get_widgets
from xrandr import list_monitor


def topbar(net=False):
    return bar.Bar(
        get_widgets(net=net),
        # opacity=0.8,
        size=26,
        length=bar.STRETCH,
        background=["#00000000", "#00000000"],  # colors[0],
        margin=[4, 8, 0, 8],
    )


screens = [Screen(top=topbar(net=i == 0)) for i in range(list_monitor())]
