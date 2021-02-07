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

from edbc.data.edbcdataobject import EdbcDataObject

class Pilot(EdbcDataObject):
    def __init__(self, fake=False):
        if fake:
            self.name = 'docdrum'
            self.credits = 123456789
            self.current_system = 'Shinrarta Dezhra'
            self.ship = 'Gorch Fock (Diamondback Explorer'
        else:
            raise NotImplementedError
