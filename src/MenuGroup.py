class menuGroup:
    def __init__ (self, title="No Title", subtitle="", items=[], icon=None):
        self.title = title
        self.subtitle = subtitle
        self.items = items
        self.icon = icon
    def get_title(self):
        return self.title

