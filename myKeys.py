from libqtile.config import Key
from libqtile.lazy import lazy
from common import mod, terminal

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    
    # Launche Applications
    Key([mod, "shift"], "f", lazy.spawn("firefox"),
        desc="Launch Firefox"),
    Key([mod], "c", lazy.spawn("vscodium")),
    Key([mod], "q", lazy.spawn("qutebrowser")),

    # Take Screenshot
    Key([], "Print", lazy.spawn("scrot -s -e 'mv $f ~/screenshots/'")),

    # Media hotkeys
    Key([mod], 'F3', lazy.spawn('amixer -q sset Master 5%+')),
    Key([mod], 'F2', lazy.spawn('amixer -q sset Master 5%-')),
    Key([mod], 'F1', lazy.spawn('amixer -D pulse set Master 1+ toggle')),
    
    # More Window Stuff
    Key([mod], 'f', lazy.window.toggle_floating()),
    Key([mod], 'm', lazy.window.toggle_fullscreen()),
    Key([mod], 'n', lazy.window.toggle_minimize()),

    # Move Between Workspaces
    Key([mod], 'Right', lazy.screen.next_group()),
    Key([mod], 'Left', lazy.screen.prev_group()),

    # Brigtness
    Key([mod], 'F5', lazy.spawn('xbacklight -dec 5')),
    Key([mod], 'F6', lazy.spawn('xbacklight -inc 5')), 

    # Switch Monitors
    Key([mod], 'period', lazy.next_screen(), desc="Next monitor"),
]
