'''
Created on 6 Feb 2021

@author: cstft
'''

class EdbcDataObject:
    def __setattr__(self, attr, val):
        if isinstance(val, str):
            val = val.upper()
        super(EdbcDataObject, self).__setattr__(attr, val)