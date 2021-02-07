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

from edbc.textscreen import TextScreen

class StatusScreen(TextScreen):
    def __init__(self, data):
        super(StatusScreen, self).__init__(data)

    def buildScreen(self):
        super(StatusScreen, self).buildScreen()
        self.setButton(19, "OVR")

        self.setButton(14, "A..G")
        self.setButton(13, "H..M")
        self.setButton(12, "N..S")
        self.setButton(11, "T..Z")
        self.setButton(10, "0..9-")

        self.setText(0, 0, f"CMDR: {self.data.pilot.name}")
        self.setText(1, 0, f"SHIP: {self.data.pilot.ship}")
        self.setText(2, 0, f"CRED: {self.data.pilot.credits}" )
        self.setText(3, 0, f"SYS:  {self.data.pilot.current_system}")
