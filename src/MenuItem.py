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
    def run_command(self, _):
        try:
            for command in self.commands:
                comm = shlex.split(command)
                print("running",comm)
                subprocess.run(comm, check=True)
        except subprocess.CalledProcessError:
            print("bad exit code")
    def get_subtitle(self):
        return self.subtitle
    def set_subtitle(self, subtitle):
        self.subtitle = subtitle
    def get_icon(self):
        return self.icon
    def set_icon(self, icon):
        self.icon = icon

    
