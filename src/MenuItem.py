import shlex
import subprocess


class menuItem:
    def __init__ (self, title="NoTitle", subtitle="", commands=[], icon=None):
        self.title = title
        self.commands = commands
        self.subtitle = subtitle
        self.icon = icon
    def get_title(self):
        return self.title
    def get_icon(self):
        return self.icon
    def run_command(self, _):
        for command in self.commands:
            comm = shlex.split(command)
            print("running",comm)
            subprocess.run(comm)

    
