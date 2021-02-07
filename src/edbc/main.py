#!/usr/bin/env python
"""
Copyright (C) 2021  DocDrum


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# text area: 16 rows, 46 columns
import kivy
from kivy.uix.gridlayout import GridLayout
from edbc.statusscreen import StatusScreen
from edbc.inventoryscreen import InventoryScreen
from edbc.data.edbcdata import EdbcData

kivy.require('2.0.0')
from kivy.app import App

def NoAction():
        pass

class Edbc(GridLayout):
    def __init__(self, **kwargs):
        super(Edbc, self).__init__(**kwargs)
        self.click1 = NoAction
        self.click2 = NoAction
        self.click3 = NoAction
        self.click4 = NoAction
        self.click5 = NoAction
        self.click6 = NoAction
        self.click7 = NoAction
        self.click8 = NoAction
        self.click9 = NoAction
        self.click10 = NoAction
        self.click11 = NoAction
        self.click12 = NoAction
        self.click13 = NoAction
        self.click14 = NoAction
        self.click15 = NoAction
        self.click16 = NoAction
        self.click17 = NoAction
        self.click18 = NoAction
        self.click19 = NoAction
        self.click20 = NoAction

    def set_screen(self, text_screen):
        scr = text_screen
        self.ids.main_screen.text = scr

    def connectButtons(self, app):
        self.click1 = app.button1
        self.click2 = app.button2

class EdbcApp(App):
    def button1(self):
        self.showStatusScreen()

    def button2(self):
        self.showInventoryScreen()

    def __init__(self, **kwargs):
        super(EdbcApp, self).__init__(**kwargs)
        self.data = EdbcData(fake=True)
        self.statusScreen = StatusScreen(data=self.data)
        self.inventoryScreen = InventoryScreen(data=self.data)
        self.edbc = None

    def showStatusScreen(self):
        self.statusScreen.setUI(self.edbc)
        self.edbc.set_screen(self.statusScreen.get())

    def showInventoryScreen(self):
        self.inventoryScreen.setUI(self.edbc)
        self.edbc.set_screen(self.inventoryScreen.get())

    def build(self):
        self.edbc = Edbc()
        self.edbc.connectButtons(self)
        self.showStatusScreen()
        return self.edbc

if __name__ == "__main__":
    EdbcApp().run()
