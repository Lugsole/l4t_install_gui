# l4t_install_gui

## dependencies
* Meson
* Ninja
* Python GTK
* Libhandy

```sh
sudo apt-get install -y ninja-build
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

## Build
`meson --prefix /usr/local . _build`
`ninja -C _build/`
## install
`ninja -C _build/ install`
