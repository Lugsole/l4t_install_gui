
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
        returning_item = menuGroup(items=items)
        if "title" in obj:
            returning_item = menuGroup(title=obj["title"], items=items)
        if "subtitle" in obj:
            returning_item.set_subtitle(obj["subtitle"])
        if "icon" in obj:
            returning_item.set_icon(obj["icon"])
        return returning_item
    elif obj["type"] == "item":
        returning_item = menuItem(commands=obj["commands"])
        if "title" in obj:
            returning_item = menuItem(title=obj["title"], commands=obj["commands"])
        if "subtitle" in obj:
            returning_item.set_subtitle(obj["subtitle"])
        if "icon" in obj:
            returning_item.set_icon(obj["icon"])
        return returning_item
    else:
        print("lost")
