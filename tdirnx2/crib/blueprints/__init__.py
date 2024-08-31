import os
import importlib
dd = [g for g in os.listdir(__name__.replace('.','/') + '/') if g != "__pycache__" and g !="__init__.py"]

def dmodup(de):
    dmod = importlib.import_module('.' +str(de),__name__)
    return (de,dmod.blueprint)

bps = [dmodup(x) for x in dd]

# #print(dd)
# for d in dd:
#     #print(d)
#     dmod = importlib.import_module('.' +str(d),__name__)
#     #print(dmod.__name__)
#     bps.append((d,dmod.blueprint))