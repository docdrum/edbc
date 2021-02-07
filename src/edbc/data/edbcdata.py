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

from edbc.data.pilot import Pilot
from edbc.data.edbcdataobject import EdbcDataObject
from edbc.data.cargo import Cargo

class EdbcData(EdbcDataObject):
    def __init__(self, fake=False):
        self.pilot = Pilot(fake)
        self.cargo = Cargo(fake)
