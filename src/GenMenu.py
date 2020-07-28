
from .MenuItem import menuItem
from .MenuGroup import menuGroup

def genMenu(obj):
    #print(obj)
    if isinstance(obj, list):
        items = []
        for item in obj:
            items.append(genMenu(item))
        return items
    elif obj["type"] == "group":
        items = []
        for item in obj["subs"]:
            items.append(genMenu(item))
        if "subtitle" in obj and "title" in obj:
            return menuGroup(title=obj["title"], subtitle=obj["subtitle"], items=items)
        if "title" in obj:
            return menuGroup(title=obj["title"], items=items)
    elif obj["type"] == "item":
        return menuItem(obj["title"], obj["commands"])
    else:
        print("lost")
