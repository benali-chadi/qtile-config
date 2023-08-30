from libqtile.config import Group, Key
from libqtile.lazy import lazy
from myKeys import keys
from common import mod

group_icons = [
                "✔",
                " ",
                " ",
                "🧪",
                " ",
                " ",
                "📖",
               ]
groups_spawn = [
    [
        '/home/chadi/Downloads/Obsidian-1.1.16.AppImage',
        '/home/chadi/Downloads/syncthing/syncthing-linux-amd64-v1.23.4/syncthing'
    ], 
    ['alacritty', 'qutebrowser'],
    [], [], [], [],
]
# groups = [Group(i) for i in "123456789"]
groups = [
   Group(i, label=g, layout="monadtall", spawn=s ) for i, g, s in zip("123456", group_icons, groups_spawn)
]
# groups = [Group(i) for i in group_icons]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
