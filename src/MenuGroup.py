class menuGroup:
    def __init__ (self, title="No Title", subtitle="", items=[], icon=None):
        self.title = title
        self.subtitle = subtitle
        self.items = items
        self.icon = icon
    def get_title(self):
        return self.title
    def get_subtitle(self):
        return self.subtitle
    def set_subtitle(self, subtitle):
        self.subtitle = subtitle
    def get_items(self):
        return self.items
    def set_items(self, items):
        self.items = items
    def get_icon(self):
        return self.icon
    def set_icon(self, icon):
        self.icon = icon

