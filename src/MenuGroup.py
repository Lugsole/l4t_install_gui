import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Handy', '0.0')
from gi.repository import Handy

class menuGroup:
    def __init__ (self, title="No Title", subtitle="", items=[]):
        self.title = title
        self.subtitle = subtitle
        self.items = items
    def get_title(self):
        return self.title
    def get_gtk(self):
        sub_items = Gtk.ListBox()
        sub_items.show()
        for item in self.items:
            sub_items.add(item.get_gtk())
        expand = Handy.ExpanderRow()
        expand.set_property("title", self.title)
        expand.set_property("subtitle", self.subtitle)

        expand.add(sub_items)
        expand.show()
        return expand

