import re

pw = ('Prse5ygl')

def passcheck(strong):
    if re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{8,}',compass):
        return True
    else:
        return False
