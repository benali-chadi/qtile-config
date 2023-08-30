# from typing import List  # noqa: F401
#
# from libqtile import bar, layout, widget, qtile
# from libqtile.config import Click, Drag, Group, Key, Match, Screen
# from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

from libqtile import hook
# import os
import subprocess

# my imports
# from common import *
from myKeys import *
from myGroups import *
from myScreens import *
from myLayouts import *


@hook.subscribe.startup
def autostart():
    # subprocess.call(['/home/chadi/.config/qtile/autostart.sh'])
    processes = [
            ['feh', '--bg-scale', '/home/chadi/Downloads/luffy.jpg'],
            ]
    for p in processes:
        subprocess.Popen(p)

