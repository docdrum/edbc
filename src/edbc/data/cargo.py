'''
Created on 6 Feb 2021

@author: cstft
'''
from edbc.data.edbcdataobject import EdbcDataObject

class Cargo(EdbcDataObject):
    def __init__(self, fake=False):
        self.items = []
        if fake:
            self.items.append([276, 18]) # LTD
            self.items.append([83, 13]) # Painite
            self.items.append([75, 214]) # Biowaste
            self.items.append([999, 23]) # Limpets
        else:
            raise NotImplementedError
            
    def getName(eddb_id):  # @NoSelf
        try:
            return {
                # fakes
                999: 'limpets',
                # chemicals
                1: 'Explosives',
                2: 'Hydrogen Fuel',
                277: 'Hydrogen Peroxide',
                360: 'Agronomic Treatment',
                # consumer items
                # foods
                # industrial materials
                # legal drugs
                # machinery
                # medicines
                # metals
                # minerals
                276: 'Low Temperature Diamonds',
                83: 'Painite',
                # salvage
                # slavery
                # technology
                # textiles
                # waste
                75: 'Biowaste',
            }[eddb_id].upper()
        except:
            return f"(unknown id: {eddb_id})"
            