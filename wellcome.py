#! /bin/python3
#JulenCamps
#https://github.com/julencamps/myqtile

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class mainwindow(Gtk.Window):
    def __init__(self, buttontitle):
        super().__init__(title="MyQtile")
        self.connect("destroy", Gtk.main_quit)

        self.grid = Gtk.Grid()

    def on_button_clicked(self, buttontitle):
        secwin = mainwindow("2")
        secwin.show_all()

mainwin = mainwindow("hello")
mainwin.show_all()
Gtk.main()