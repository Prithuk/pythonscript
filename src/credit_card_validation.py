

from datetime import datetime

def validateCard(expDate):
    if expDate > datetime.now().date():
        return 'Valid'
    else:
        raise RuntimeError('Card has Expired')
