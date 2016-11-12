# My dotfiles <3

<img alt="dotfiles" width="200" src="https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/dotfiles-logo.png">

### Some settings for i3wm, Awesomewm, Monsterwm, Bspwm and several scripts.


* See [I3](https://i3wm.org/)
* See [Awesome](https://awesome.naquadah.org/)
* See [Monster](https://github.com/c00kiemon5ter/monsterwm)
* See [Bspwm](https://github.com/baskerville/bspwm)

> For more [screenshots](https://github.com/Sup3r-Us3r/MyDotfiles/tree/master/Screenshots) of my system.


### See some screenshot of these customizations.

I3wm
![I3][screenshot1]

Awesomewm
![Awesome][screenshot2]

Monsterwm
![Monster][screenshot3]

Bspwm
![Bspwm][screenshot4]

My script slideshow
![Slideshow][screenshot5]

[screenshot1]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot5.png
[screenshot2]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot9.png
[screenshot3]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot8.png
[screenshot4]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot13.png
[screenshot5]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/script-slide.gif

### Installation and dependencies

For I3wm:
```sh
$ sudo pacman -S i3 lm_sensors mpc feh hddtemp nitrogen mpd ncmpcpp conky git
$ yaourt -S i3blocks ttf-inconsolata ttf-font-awesome ttf-dejavu terminus-font-ttf

```

For Awesomewm:
```sh
$ sudo pacman -S awesome lua conky git
$ mkdir ~/.config/awesome
$ cd ~/.config/awesome && rm -rf lain/
$ git clone https://github.com/copycat-killer/lain.git
$ cp rc.lua.holo rc.lua 
/// Example rc.lua.holo more there are others within the directory ~/.config/awesome only give cp rc.lua.theme rc.lua

```

For Monsterwm:
```sh
$ sudo pacman -S git conky dzen2
$ cd ~/.config/
$ git clone https://github.com/c00kiemon5ter/monsterwm.git
$ cd monsterwm
$ cp config.def.h config.h
$ nano config.h
$ make
$ sudo make clean install

```

For Bspwm:
```sh
$ sudo pacman -S bspwm sxhkd lm_sensors mpc hddtemp nitrogen mpd ncmpcpp git
$ yaourt -S yabar-git ttf-inconsolata ttf-font-awesome ttf-dejavu terminus-font-ttf
$ mkdir ~/.config/bspwm
$ cd ~/.config/bspwm
$ touch bspwmrc && nano bspwmrc ///Paste this = https://github.com/Sup3r-Us3r/dotfiles/blob/master/config/bspwm/bspwmrc
$ sudo chmod +x bspwmrc
$ mkdir ~/.config/sxhkd
$ cd ~/.config/sxhkd
$ touch sxhkdrc && nano sxhkdrc ///Paste this = https://github.com/Sup3r-Us3r/dotfiles/blob/master/config/sxhkd/sxhkdrc

```

### Installation and configuration Mpd & Ncmpcpp

Mpd:
```sh
$ sudo pacman -S mpd
$ sudo systemctl stop mpd
$ sudo systemctl disable mpd
$ mkdir -p ~/.mpd/playlists
$ touch ~/.mpd/{mpd.db,mpd.log,mpd.pid,mpdstate}
$ nano ~/.mpd/mpd.conf
/// Paste this = http://pastebin.com/2AqeAtXU | But remember to replace "ghost" for your username and the directory of musics.

```

Ncmpcpp:
```sh
$ sudo pacman -S ncmpcpp
$ mkdir ~/.ncmpcpp
$ nano ~/.ncmpcpp/config
/// Paste this = http://pastebin.com/0QARNzKH

```

### Note in English
I taught how to install, configure, and meet the general dependencies, it is you use my settings and replace the standards.

### Note in Portuguese
Eu ensinei como instalar, configurar e satisfazer as dependências de modo geral, cabe você usar minhas configurações e substituir pelas padrões.
