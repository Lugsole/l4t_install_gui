# window.py
#
# Copyright 2020 Lugsole
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GObject, GLib, Gtk, Gio
gi.require_version('Handy', '1')
from gi.repository import Handy
import yaml
from .config import pkgdatadir
from .GUIMenuPart import toGUI
from .GenMenu import genMenu
import os

Handy.init()

class L4tInstallGuiWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'L4tInstallGuiWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Scroll = Gtk.ScrolledWindow()
        self.add(Scroll)
        Scroll.show()
        Scroll.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)
        vp = Gtk.Viewport()
        Scroll.add(vp)
        vp.show()
        self.clamp = Handy.Clamp()
        self.clamp.set_property("can_focus", False)
        self.clamp.set_property("margin-bottom", 8)
        self.clamp.set_property("margin-start", 8)
        self.clamp.set_property("margin-end", 8)
        self.clamp.set_property("margin-top", 8)
        self.clamp.set_property("expand", True)
        self.clamp.set_property("maximum-size", 400)
        self.clamp.set_property("tightening-threshold", 300)
        self.clamp.show()
        vp.add(self.clamp)
        self.book_list = Handy.PreferencesGroup()


        self.book_list.set_property("expand", True)
        self.book_list.set_property("can_focus", False)
        self.clamp.add(self.book_list)
        self.book_list.show()
        yaml_file_name = os.path.join(pkgdatadir, "test.yaml")
        with open(yaml_file_name) as file:
            obj = yaml.load(file, Loader=yaml.FullLoader)
            objects = genMenu(obj)
            if isinstance(objects, list):
                for item in objects:
                    self.book_list.add(toGUI(item))
            elif isinstance(objects, menuGroup):
                self.book_list.add(toGUI(objects))
        self.maximize()


    def show_page(self, button, page, book, chapter):
        print("Done")
