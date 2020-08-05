import gi
#from .GUIMenuPart import toGUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Handy', '1')
from gi.repository import Handy

import l4t_install_gui.GUIMenuPart

class guiMenuGroup(Handy.ExpanderRow):
    def __init__(self, itemIn):
        super().__init__()
        sub_items = Gtk.ListBox()
        for item in itemIn.items:
            sub_item = Gtk.ListBoxRow()
            sub_item.add(l4t_install_gui.GUIMenuPart.toGUI(item))
            sub_item.set_activatable(False)
            sub_item.show()
            self.add(sub_item)
        sub_items.show()
        self.set_property("title", itemIn.title)
        self.set_property("subtitle", itemIn.subtitle)
        self.show()

