from edbc.data.pilot import Pilot
from edbc.data.edbcdataobject import EdbcDataObject
from edbc.data.cargo import Cargo

class EdbcData(EdbcDataObject):
    def __init__(self, fake=False):
        self.pilot = Pilot(fake)
        self.cargo = Cargo(fake)
