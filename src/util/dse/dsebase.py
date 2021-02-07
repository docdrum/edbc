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

from util.dse.dseerror import DSEError

class DSEBase:
    def __init__(self, max_len):
        self.input = ''
        self.max_len = max_len
        self.wait_for_more = False
        self.current_count = 0
        self.current_button = -1

    def get(self):
        return self.input

    def currentChar(self):
        if self.current_button == -1:
            return None
        return self.keys[self.current_button][self.current_count]

    def pressButton(self, button_id):
        if button_id > len(self.keys):
            raise DSEError("invalid button id")
        if self.wait_for_more and self.current_button == button_id:
            self.current_count += 1
            if self.current_count >= len(self.keys[self.current_button]):
                self.current_count = 0
        elif self.wait_for_more:
            self.input = self.input + self.currentChar()
            self.current_count = 0
            self.current_button = button_id
        else:
            self.current_count = 0
            self.current_button = button_id
            self.wait_for_more = True

    def timeOut(self):
        self.wait_for_more = False
        self.input = self.input + self.currentChar()
        self.current_count = 0
        self.current_button = -1
