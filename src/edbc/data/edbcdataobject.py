class EdbcDataObject:
    def __setattr__(self, attr, val):
        if isinstance(val, str):
            val = val.upper()
        super(EdbcDataObject, self).__setattr__(attr, val)
