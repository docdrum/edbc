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

class DSE10(DSEBase):
    def __init__(self):
        super(DSE10, self).__init__(20)
        self.keys = [" -+0",
                     "1",
                     "ABC2",
                     "DEF3",
                     "GHI4",
                     "JKL5",
                     "MNO6",
                     "PQRS7",
                     "TUV8",
                     "WXYZ9"]

