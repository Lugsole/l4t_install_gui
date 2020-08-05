
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
gi.require_version('Handy', '1')
from gi.repository import Handy

class guiMenuItem(Handy.ActionRow):
    checkmark = Gtk.Image()
    icon = Gtk.Image()
    button = Gtk.Button()
    def __init__ (self, itemIn):
        super().__init__()
        self.title = itemIn.get_title()
        self.run_command = itemIn.run_command
        self.icon_path = itemIn.get_icon()

        if self.icon_path is not None:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                    filename="test.png",
                    width=32,
                    height=32,
                    preserve_aspect_ratio=True)
            self.icon = Gtk.Image.new_from_pixbuf(pixbuf)
            #icon = Gtk.Image.new_from_file("test.png")
            self.icon.set_pixel_size(1)
            self.icon.show()
            self.icon.set_can_focus(False)
        checkmark = Gtk.Image()
        checkmark= Gtk.Image.new_from_icon_name("emblem-ok-symbolic",Gtk.IconSize.MENU)
        checkmark.set_can_focus(False)

        if False:
            checkmark.show()

        button = Gtk.Button(self.title, label="Run")
        button.set_can_focus(False)
        button.show()
        button.connect(
            'clicked',
            self.run_command)

        if self.icon_path is not None:
            self.add(
                    self.icon)
        self.add(
                button)
        self.add(
                checkmark)
        self.set_can_focus(False)
        self.set_property("title", itemIn.title)
        self.set_property("subtitle", itemIn.subtitle)
        self.show()
