'''
Created on 5 Feb 2021

@author: cstft
'''
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
    
