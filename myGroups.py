from libqtile.config import Group, Key, ScratchPad, DropDown
from libqtile.lazy import lazy
from myKeys import keys
from common import mod, terminal

### Workspaces
group_icons = [
                "𝟭 ✔",
                "𝟮  ",
                "𝟯  ",
                "𝟰 🪧",
                "𝟱  ",
                "𝟲  ",
               ]
groups_spawn = [
    [
        '/home/chadi/Downloads/Obsidian-1.1.16.AppImage',
        '/home/chadi/Downloads/syncthing/syncthing-linux-amd64-v1.23.4/syncthing'
    ], 
    ['alacritty', 'qutebrowser'],
    [], [], [], [],
]

groups = [
   Group(i, label=g, layout="monadtall", spawn=s ) for i, g, s in zip("123456", group_icons, groups_spawn)
]

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

### Scratchpad

groups.extend([
    ScratchPad('scratchpad', [
            DropDown(
                "terminal",
                terminal,
                x=0.15,
                y=0.2,
                height=0.6,
                width=0.7,
                opacity=0.9,
                on_focus_lost_hide=True
            ),
            DropDown(
                'htop',
                terminal + ' -e htop',
                x=0.15,
                y=0.2,
                height=0.6,
                width=0.7,
                opacity=0.9,
                on_focus_lost_hide=True
            ),
            DropDown(
                'sound control',
                'pavucontrol',
                height = 0.8,
                width = 0.8,
                x = 0.1,
                y = 0.1,
                on_focus_lost_hide = False,
                opacity = 0.85,
                warp_pointer = False,
            ),
            DropDown(
                'freetube',
                'freetube',
                height = 0.4,
                width = 0.3,
                x = 0.7,
                y = 0.002,
                on_focus_lost_hide = False,
                opacity = 0.85,
                warp_pointer = False,
            ),
    ])
])

keys.extend([
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key([], 'F10', lazy.group['scratchpad'].dropdown_toggle('htop')),
    Key([], 'F9', lazy.group['scratchpad'].dropdown_toggle('sound control')),
    Key([], 'F8', lazy.group['scratchpad'].dropdown_toggle('freetube')),
])
