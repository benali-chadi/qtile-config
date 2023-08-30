from libqtile.config import Screen
from libqtile import bar, widget, qtile

#### MOUSE CALLBACKS ####

def open_htop():
    qtile.cmd_spawn('alacritty -e htop')

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.7),
                widget.GroupBox(),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/notion.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/var/lib/snapd/snap/notion-snap/current/notion-snap')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/steam.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('steam')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/discord.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('discord')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/discord-ptb.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/home/chadi/Downloads/DiscordPTB/DiscordPTB')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/telegram.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('telegram-desktop')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/obsidian.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/home/chadi/Downloads/Obsidian-1.1.16.AppImage')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/inkscape.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/home/chadi/Downloads/Inkscape-0e150ed-x86_64.AppImage')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.BatteryIcon(),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
		widget.Image(
		    filename='~/Downloads/icons/headphones.png',
		    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('playmymusic')},
		),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                widget.Image(
                    filename='~/Downloads/icons/sound_icon.png',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                ),
                widget.Volume(),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                widget.MemoryGraph(
                    type='line',
                    mouse_callbacks = {'Button1': open_htop}
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                #widget.Systray(),
		        widget.Net(intterface="enp4s"),
                widget.NetGraph(
		        	intterface="enp4s",
			        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('gnome-control-center')},
		        ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p',
		            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('alacritty')},),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                ),
                widget.QuickExit(),
            ],
            26,
	    background="#2f206e",
        ),
    ),
]
