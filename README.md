# l4t_install_gui

## dependencies
* Meson
* Ninja
* Python GTK
* Libhandy

```sh
sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-pip ninja-build
sudo pip3 install pyyaml
sudo pip3 install meson
```

## Build
`meson --prefix /usr/local . _build`  
`ninja -C _build/`
## install
`ninja -C _build/ install`
