# l4t_install_gui

## dependencies
* Meson
* Ninja
* Python GTK
* Libhandy

```sh
sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-pip ninja-build libglib1.0-dev
pip3 install pyyaml
pip3 install meson
```

### libhandy-1
```sh
wget https://gitlab.gnome.org/GNOME/libhandy/-/archive/master/libhandy-master.zip
unzip libhandy-master.zip
cd libhandy-master
echo last sucesfull commit test was: d22356ef5f0cc6c6080896ae5611677d59849f51
sudo apt get install -y gtk-doc-tools libgirepository1.0-dev libgladeui-dev libglib2.0-doc libgnome-desktop-3-dev libgtk-3-doc libgtk-3-dev libxml2-utils meson pkg-config valac cmake gtk+-3.0-dev 

sed 's/3.24.1/3.22.30/g' -i src/meson.build

meson --prefix /usr . _build
ninja -C _build/
ninja -C _build/ install
```

## Build
`meson --prefix /usr/local . _build`  
`ninja -C _build/`
## install
`ninja -C _build/ install`
