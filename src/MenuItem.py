import gi
import shlex
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class menuItem:
    def __init__ (self, title="NoTitle", commands=["ls"]):
        self.title = title
        self.commands = commands
    def get_title(self):
        return self.title
    def run_command(self, _):
        for command in self.commands:
            comm = shlex.split(command)
            print("running",comm)
            subprocess.run(comm)
    def get_gtk(self):
            button = Gtk.Button(self.title, label=self.title)
            button.show()
            button.connect(
                'clicked',
                self.run_command)
            return button

    
