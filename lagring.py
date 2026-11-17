import json
from pathlib import Path

#read(load) servers from servrar.json file
def las_servrar(fil_namn):
    if fil_finns(fil_namn):
        with open(fil_namn,"r") as file:
            servrar = json.load(file)
        return servrar
    else:
        return []
#save servers in json format
def spara_servrar(main_server_lista,fil_namn):
    with open(fil_namn,"w") as file:
        json.dump(main_server_lista,file,indent=4)

#my own method1 checkes file existance
def fil_finns(file):
    return Path(file).exists()
        

