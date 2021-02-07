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

from util.dse.dsebase import DSEBase
from util.dse.dseerror import DSEError

class DSE5(DSEBase):
    def __init__(self):
        super(DSE5, self).__init__(20)
        self.keys = ["ABCDEFG",
                     "HIJKLM",
                     "NOPQRS",
                     "TUVWXYZ",
                     "0123456789-"]

