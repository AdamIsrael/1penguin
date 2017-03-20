#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator

from onepassword import Keychain

import os
import signal


APPINDICATOR_ID = '1penguin'
DEFAULT_KEYCHAIN_PATH = "~/Dropbox/1Password/1Password.agilekeychain"


class AskPassword(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Search")


        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.input = Gtk.Entry()
        self.input.set_invisible_char('*')
        self.input.set_visibility(False)

        # Process the password if the user hits enter
        self.input.connect("activate", self.on_unlock_clicked)
        self.input.connect("key-release-event", self.on_keypress)

        self.grid.add(self.input)

        self.unlock = Gtk.Button(label="Unlock")
        self.unlock.connect("clicked", self.on_unlock_clicked)
        # self.unlock.connect("keys-changed", self.on_keypress)

        self.grid.attach_next_to(
            self.unlock,
            self.input,
            Gtk.PositionType.BOTTOM,
            1,
            2
        )

    def on_keypress(self, event, data):
       pass

    def on_unlock_clicked(self, widget):
        """Attempt to unlock the keychain."""
        print("Unlocking!")
        print(widget)

        my_keychain = Keychain(path=DEFAULT_KEYCHAIN_PATH)
        my_keychain.unlock(widget.get_text())

        self.close()

    def on_cancel_clicked(self, widget):
        print("Nevermind")
        self.close()


class SearchWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Search")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")


def build_menu():
    menu = Gtk.Menu()

    menu.append(new_menu_item('test', askpass))
    menu.append(new_menu_item('Search', menu_search))
    menu.append(Gtk.SeparatorMenuItem())

    menu.append(new_menu_item('Favorites', noop))
    menu.append(new_menu_item('Password Generator', noop))
    menu.append(new_menu_item('Preferences', noop))

    # menu.append(new_menu_item('Lock', noop))
    # menu.append(new_menu_item('Unlock', noop))
    menu.append(Gtk.SeparatorMenuItem())
    menu.append(new_menu_item('Quit', quit))

    menu.show_all()
    return menu


def test(item):
    """Test 1Pass functionality"""

    print(item)
    pass


def new_menu_item(name, callback):
    item = Gtk.MenuItem(name)
    item.connect('activate', callback)
    return item


def askpass(item):
    print("Asking for password")
    win = AskPassword()
    win.show_all()


def menu_search(item):
    win = SearchWindow()
    # win.connect("delete-event", Gtk.main_quit)
    win.show_all()

def noop():
    pass


def quit(source):
    Gtk.main_quit()


def main():
    indicator = appindicator.Indicator.new(
        APPINDICATOR_ID,
        Gtk.STOCK_DIALOG_AUTHENTICATION,
        appindicator.IndicatorCategory.SYSTEM_SERVICES
    )

    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    indicator.set_menu(build_menu())

    # Allow control-c
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    Gtk.main()


if __name__ == "__main__":
    main()
