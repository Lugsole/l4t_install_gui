import gi
#from .GUIMenuPart import toGUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
gi.require_version('Handy', '1')
from gi.repository import Handy
import os
from .config import pkgdatadir
import l4t_install_gui.GUIMenuPart

class guiMenuGroup(Handy.ExpanderRow):
    def __init__(self, itemIn):
        super().__init__()
        sub_items = Gtk.ListBox()
        self.icon_path = itemIn.get_icon()
        for item in itemIn.items:
            sub_item = Gtk.ListBoxRow()
            sub_item.add(l4t_install_gui.GUIMenuPart.toGUI(item))
            sub_item.set_activatable(False)
            sub_item.show()
            self.add(sub_item)
        if self.icon_path is not None:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                    filename=os.path.join(pkgdatadir,self.icon_path),
                    width=32,
                    height=32,
                    preserve_aspect_ratio=True)
            self.icon = Gtk.Image.new_from_pixbuf(pixbuf)
            #icon = Gtk.Image.new_from_file("test.png")
            self.icon.set_pixel_size(1)
            self.icon.show()
            self.icon.set_can_focus(False)
        sub_items.show()
        self.set_property("title", itemIn.title)
        self.set_property("subtitle", itemIn.subtitle)

        if self.icon_path is not None:
            self.add_prefix(self.icon)
        self.show()

