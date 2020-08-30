cd /tmp

echo "fetching libhandy source"
wget https://gitlab.gnome.org/GNOME/libhandy/-/archive/master/libhandy-master.zip
echo "extracting libhandy source"
unzip libhandy-master.zip
echo "moving libhandy source"
cd libhandy-master
echo last sucesfull commit test was: d22356ef5f0cc6c6080896ae5611677d59849f51
echo "installing libhandy dependencies"
sudo apt install -y gtk-doc-tools libgirepository1.0-dev libgladeui-dev libglib2.0-doc libgnome-desktop-3-dev libgtk-3-doc libgtk-3-dev libxml2-utils meson pkg-config valac cmake gtk+-3.0-dev

echo "installing changing libhandy dependencies"
sed 's/3.24.1/3.22.30/g' -i src/meson.build

echo "configuring libhandy"
meson --prefix /usr . _build
echo "building libhandy"
ninja -C _build/
echo "installing libhandy"
sudo ninja -C _build/ install
echo "l4t_install_gui"
cd /tmp
echo "fetching l4t_install_gui source"
wget https://github.com/Lugsole/l4t_install_gui/archive/master.zip -O l4t_install_gui-master.zip
echo "extracting l4t_install_gui source"
unzip l4t_install_gui-master.zip
echo "moving l4t_install_gui source"
cd l4t_install_gui-master
echo "installing l4t_install_gui dependencies"
sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-pip ninja-build libglib1.0-dev
echo "installing l4t_install_gui pip dependencies 1"
pip3 install pyyaml
echo "installing l4t_install_gui pip dependencies 2"
pip3 install meson

echo "configuring l4t_install_gui"
meson --prefix /usr/local . _build
echo "building l4t_install_gui"
ninja -C _build/
echo "installing l4t_install_gui"
sudo ninja -C _build/ install
