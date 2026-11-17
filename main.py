
import os
from meny import starta_meny
from lagring import las_servrar


#reads env and assign the default value if it is not set
fil_namn=os.getenv("INVENTORY_DATAFIL","servrar.json")
servrar = las_servrar(fil_namn)
starta_meny(servrar,fil_namn)







