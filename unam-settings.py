#!/usr/bin/python3

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class init():
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('unam-settings.glade')
		self.win = self.builder.get_object('unam-settings-window')
		self.win.connect('delete-event', Gtk.main_quit)

		self.about = self.builder.get_object('about-dialog')

		self.btn_themes = self.builder.get_object('btn_themes')
		self.btn_themes.connect('clicked', self.btn_themes_click)

		self.btn_displays = self.builder.get_object('btn_displays')
		self.btn_displays.connect('clicked', self.btn_displays_click)

		self.btn_dock = self.builder.get_object('btn_dock')
		self.btn_dock.connect('clicked', self.btn_dock_click)

		self.btn_menus = self.builder.get_object('btn_menus')
		self.btn_menus.connect('clicked', self.btn_menus_click)

		self.btn_panel = self.builder.get_object('btn_panel')
		self.btn_panel.connect('clicked', self.btn_panel_click)

		self.btn_power = self.builder.get_object('btn_power')
		self.btn_power.connect('clicked', self.btn_power_click)

		self.btn_startup = self.builder.get_object('btn_startup')
		self.btn_startup.connect('clicked', self.btn_startup_click)

		self.btn_wallpaper = self.builder.get_object('btn_wallpaper')
		self.btn_wallpaper.connect('clicked', self.btn_wallpaper_click)

		self.btn_windows = self.builder.get_object('btn_windows')
		self.btn_windows.connect('clicked', self.btn_windows_click)

		self.btn_about = self.builder.get_object('btn_about')
		self.btn_about.connect('clicked', self.btn_about_click)

		# label = self.builder.get_object('lbl_settings_info')
		# label.set_text('command')

	### Buttons ###
	def btn_themes_click(self, button):
		os.system("lxappearance")

	def btn_displays_click(self, button):
		os.system("arandr")

	def btn_dock_click(self, button):
		os.system("plank --preferences")

	def btn_menus_click(self, button):
		os.system("obmenu")

	def btn_panel_click(self, button):
		os.system("tint2conf")

	def btn_power_click(self, button):
		os.system("xfce4-power-manager-settings")

	def btn_startup_click(self, button):
		os.system("gedit $HOME/.config/openbox/autostart")

	def btn_wallpaper_click(self, button):
		os.system("nitrogen")

	def btn_windows_click(self, button):
		os.system("obconf")

	def btn_about_click(self, button):
		self.about.show_all()
		result = self.about.run() 
		self.about.hide()

	### SHOW APP ###
	def run(self):
		self.win.show_all()
		Gtk.main()

if __name__ == '__main__':
	usettings = init()
	usettings.run()
