from libqtile.config import Screen
from libqtile import bar, widget, qtile

from common import terminal

colors = [["#292d3e", "#292d3e"],  # panel background
           # background for current screen tab
           ["#434758", "#434758"],
           ["#ffffff", "#ffffff"],  # font color for group names
           # border line color for current tab
           ["#bc13fe", "#bc13fe"],  # Group down color
           # border line color for other tab and odd widgets
           ["#8d62a9", "#8d62a9"],
           ["#668bd7", "#668bd7"],  # color for the even widgets
           ["#e1acff", "#e1acff"],  # window name

           ["#000000", "#000000"],
           ["#AD343E", "#AD343E"],
           ["#f76e5c", "#f76e5c"],
           ["#F39C12", "#F39C12"],
           ["#F7DC6F", "#F7DC6F"],
           ["#f1ffff", "#f1ffff"],
           ["#4c566a", "#4c566a"], ]
#### MOUSE CALLBACKS ####

def open_htop():
    qtile.cmd_spawn('alacritty -e htop')

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=12,
                    margin_y=2,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[-2],
                    inactive=colors[-1],
                    # rounded=True,
                    rounded=False,
                    # highlight_color=colors[9],
                    # highlight_method="line",
                    highlight_method='block',
                    urgent_alert_method='block',
                    # urgent_border=colors[9],
                    this_current_screen_border=colors[9],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0],
                    disable_drag=True
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/notion.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/var/lib/snapd/snap/notion-snap/current/notion-snap')},
		),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/steam.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('steam')},
		),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/telegram.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('telegram-desktop')},
		),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/obsidian.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/home/chadi/Downloads/Obsidian-1.1.16.AppImage')},
		),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/inkscape.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/home/chadi/Downloads/Inkscape-0e150ed-x86_64.AppImage')},
		),
                widget.Sep(
                    linewidth = 2,
                    padding = 10,
                ),
                widget.Prompt(
                    font="Ubuntu Mono",
                    padding=10,
                    foreground=colors[2],
                    background=colors[1]
                ),
                widget.WindowName(),

                widget.TextBox(
                    text='◢',
                    fontsize=34,
                    padding=0,
                    background=colors[0],
                    foreground=colors[9],
                ),
                widget.BatteryIcon(
                    background=colors[9],
                    padding=3,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("terminator -e /home/chadi/myScripts/show-bat")},
                ),
                widget.TextBox(
                    text='◢',
                    background=colors[9],
                    foreground=colors[11],
                    fontsize=37,
                    padding=0,
                ),
                widget.TextBox(
                    text="🖬",
                    foreground=colors[7],
                    background=colors[11],
                    padding=0,
                    fontsize=14
                ),
                widget.Memory(
                    foreground=colors[7],
                    background=colors[11],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        terminal + ' -e htop')},
                    padding=5
                ),
                widget.TextBox(
                    text='◢',
                    background=colors[11],
                    foreground=colors[10],
                    padding=0,
                    fontsize=37
                ),
                widget.Image(
                    filename='~/Downloads/icons/sound_icon.png',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    foreground=colors[7],
                    background=colors[10],
                ),
                widget.Volume(
                    foreground=colors[7],
                    background=colors[10],
                ),
                widget.TextBox(
                    text='◢',
                    background=colors[10],
                    foreground=colors[9],
                    padding=0,
                    fontsize=40
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[0],
                    background=colors[9],
                    padding=0,
                    scale=0.7
                ),
                widget.CurrentLayout(
                    foreground=colors[7],
                    background=colors[9],
                    padding=5
                ),
                widget.TextBox(
                    text='◢',
                    foreground=colors[3],
                    background=colors[9],
                    padding=0,
                    fontsize=37
                ),
                widget.Clock(
                    foreground=colors[7],
                    background=colors[3],
                    format="%B %d  [ %H:%M ]",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors[0],
                    background=colors[3]
                ),
            ],
            size=20,
	    background=colors[0],
        ),
    ),
]
