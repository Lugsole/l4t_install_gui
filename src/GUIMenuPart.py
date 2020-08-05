import l4t_install_gui.GUIMenuItem
import l4t_install_gui.GUIMenuGroup

import l4t_install_gui.MenuItem
import l4t_install_gui.MenuGroup

def toGUI(item):
    if isinstance(item, l4t_install_gui.MenuItem.menuItem):
        return l4t_install_gui.GUIMenuItem.guiMenuItem(item)
    elif isinstance(item, l4t_install_gui.MenuGroup.menuGroup):
        return l4t_install_gui.GUIMenuGroup.guiMenuGroup(item)
