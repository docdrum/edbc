'''
Created on 5 Feb 2021

@author: cstft
'''

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
    
