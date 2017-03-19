<pre id="taag_font_DeltaCorpsPriest1" style="float:left;" class="fig-ansi" contenteditable="true">
████████▄   ▄██████▄      ███        ▄████████  ▄█   ▄█          ▄████████    ▄████████ 
███   ▀███ ███    ███ ▀█████████▄   ███    ███ ███  ███         ███    ███   ███    ███ 
███    ███ ███    ███    ▀███▀▀██   ███    █▀  ███▌ ███         ███    █▀    ███    █▀  
███    ███ ███    ███     ███   ▀  ▄███▄▄▄     ███▌ ███        ▄███▄▄▄       ███        
███    ███ ███    ███     ███     ▀▀███▀▀▀     ███▌ ███       ▀▀███▀▀▀     ▀███████████ 
███    ███ ███    ███     ███       ███        ███  ███         ███    █▄           ███ 
███   ▄███ ███    ███     ███       ███        ███  ███▌    ▄   ███    ███    ▄█    ███ 
████████▀   ▀██████▀     ▄████▀     ███        █▀   █████▄▄██   ██████████  ▄████████▀  
                                                    ▀                                   </pre>


| 𝓢𝓸𝓶𝓮 𝓼𝓮𝓽𝓽𝓲𝓷𝓰𝓼 𝓯𝓸𝓻 𝓲3, 𝓐𝔀𝓮𝓼𝓸𝓶𝓮, 𝓜𝓸𝓷𝓼𝓽𝓮𝓻, 𝓑𝓼𝓹𝔀𝓶 𝓪𝓷𝓭 𝓼𝓮𝓿𝓮𝓻𝓪𝓵 𝓼𝓬𝓻𝓲𝓹𝓽𝓼. |
| ------------------------------------------------------------------------------------------ |


<img alt="dotfiles" width="200" src="https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/dotfiles-logo.png">

* [X] See [I3](https://i3wm.org/)
* [X] See [Awesome](https://awesome.naquadah.org/)
* [X] See [Monster](https://github.com/c00kiemon5ter/monsterwm)
* [X] See [Bspwm](https://github.com/baskerville/bspwm)

> For more [screenshots](https://github.com/Sup3r-Us3r/MyDotfiles/tree/master/Screenshots) of my system.


### See some screenshot of these customizations.

`I3wm`
![I3][screenshot1]

`Awesomewm`
![Awesome][screenshot2]

`Monsterwm`
![Monster][screenshot3]

`Bspwm`
![Bspwm][screenshot4]

`My script slideshow`
![Slideshow][screenshot5]

`My Theme and Icons`
![ThemeAndIcons][screenshot6]

| 𝓨𝓸𝓾'𝓵𝓵 𝓯𝓲𝓷𝓭 𝓽𝓱𝓮𝓶 𝓲𝓷 .𝓽𝓱𝓮𝓶𝓮𝓼 𝓪𝓷𝓭 .𝓲𝓬𝓸𝓷𝓼 |
| ---------------------------------------------------- |

---

[screenshot1]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot5.png
[screenshot2]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot9.png
[screenshot3]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot8.png
[screenshot4]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot13.png
[screenshot5]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/script-slide.gif
[screenshot6]:https://raw.githubusercontent.com/Sup3r-Us3r/MyDotfiles/master/Screenshots/screenshot14.png

### Installation and dependencies

### `For I3wm:`
```sh
$ sudo pacman -S i3 lm_sensors mpc feh hddtemp nitrogen mpd ncmpcpp conky scrot zsh git
$ yaourt -S i3blocks ttf-inconsolata ttf-font-awesome ttf-dejavu terminus-font-ttf terminus-font dmenu2 lemonbar-git i3-gaps-git

```

### `For Awesomewm:`
```sh
$ sudo pacman -S awesome lua conky git
$ mkdir ~/.config/awesome
$ cd ~/.config/awesome && rm -rf lain/
$ git clone https://github.com/copycat-killer/lain.git
$ cp rc.lua.holo rc.lua 
/// Example rc.lua.holo more there are others within the directory ~/.config/awesome only give cp rc.lua.theme rc.lua

```

### `For Monsterwm:`
```sh
$ sudo pacman -S git conky
$ cd ~/.config/
$ git clone https://github.com/c00kiemon5ter/monsterwm.git
$ cd monsterwm
$ cp config.def.h config.h
$ nano config.h
$ make
$ sudo make clean install
/// To use the bar just run: conky -c ~/.config/monsterwm/bar
```

### `For Bspwm:`
```sh
$ sudo pacman -S bspwm sxhkd lm_sensors mpc hddtemp nitrogen mpd ncmpcpp scrot git
$ yaourt -S yabar-git ttf-inconsolata ttf-font-awesome ttf-dejavu terminus-font-ttf terminus-font dmenu2
$ mkdir ~/.config/bspwm
$ cd ~/.config/bspwm
$ touch bspwmrc && nano bspwmrc ///Paste this = https://github.com/Sup3r-Us3r/MyDotfiles/blob/master/.config/bspwm/bspwmrc
$ sudo chmod +x bspwmrc
$ mkdir ~/.config/sxhkd
$ cd ~/.config/sxhkd
$ touch sxhkdrc && nano sxhkdrc ///Paste this = https://github.com/Sup3r-Us3r/MyDotfiles/blob/master/.config/sxhkd/sxhkdrc

```

### Installation and configuration Mpd & Ncmpcpp

### `Mpd:`
```sh
$ sudo pacman -S mpd
$ sudo systemctl stop mpd
$ sudo systemctl disable mpd
$ mkdir -p ~/.mpd/playlists
$ touch ~/.mpd/{mpd.db,mpd.log,mpd.pid,mpdstate}
$ nano ~/.mpd/mpd.conf
/// Paste this = http://pastebin.com/2AqeAtXU | But remember to replace "ghost" for your username and the directory of musics.

```

### `Ncmpcpp:`
```sh
$ sudo pacman -S ncmpcpp
$ mkdir ~/.ncmpcpp
$ nano ~/.ncmpcpp/config
/// Paste this = http://pastebin.com/0QARNzKH

```

### Controls

| Key | Description |
| --- | ----------- |
| <kbd>1</kbd>| List |
| <kbd>2</kbd>| List |
| <kbd>3</kbd>| List |
| <kbd>4</kbd>| List |
| <kbd>6</kbd>| List |
| <kbd>8</kbd>| Visualizer |
| <kbd>space</kbd>| Change visualizer |
| <kbd>=</kbd>| Clock |
| <kbd>z</kbd>| Random Music |
| <kbd>p</kbd>| Pause/Play |
| <kbd>r</kbd>| Repeat mode on/off |
| <kbd>enter</kbd>| Play Music |

### `Note in English`
I taught how to install, configure, and meet the general dependencies, it is you use my settings and replace the standards.

### `Note in Portuguese`
Eu ensinei como instalar, configurar e satisfazer as dependências de modo geral, cabe você usar minhas configurações e substituir pelas padrões. 
