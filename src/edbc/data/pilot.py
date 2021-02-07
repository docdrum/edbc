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
