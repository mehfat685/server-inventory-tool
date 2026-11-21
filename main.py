import sys
import os
import argparse

from meny import starta_meny, visa_alla_servrar
from lagring import las_servrar, spara_servrar
from kontroller import kontrollera_server, kontrollera_alla
from rapporter import exportera_csv

def main():
#reads env and assign the default value if it is not set
    fil_namn=os.getenv("INVENTORY_DATAFIL","servrar.json")
    servrar = las_servrar(fil_namn)

    parser = argparse.ArgumentParser(description = "Server Inventory Tool" )

    parser.add_argument("--lista", action="store_true")
    parser.add_argument("--miljo", choices=["dev","test","prod"])
    parser.add_argument("--kontrollera")
    parser.add_argument("--kontrollera-alla", action="store_true")
    parser.add_argument("--export", action="store_true")

    args = parser.parse_args()
    

    if args.lista:
        if args.miljo:
            print(f"{'Namn':<15} | {'Adress':<20} | {'Miljo':<10}")
            print("-" * 51)
            for server in servrar:
                if server["miljo"] == args.miljo:
                    print(f"{server['namn']:<15} | "
                          f"{server['adress']:<20} | "
                          f"{server['miljo']:<10}")
        else:
            visa_alla_servrar(servrar)
    elif args.kontrollera:
        for server in servrar:
            if server["namn"] == args.kontrollera:
                print(f"{'Namn':<15} | {'Status':<10}")
                print("-" * 28)

                status = kontrollera_server(server)
                spara_servrar(servrar,fil_namn)
 
                if status == "up":
                    sys.exit(0)
                else:
                    sys.exit(1)
        print("Servern finns inte!")
        sys.exit(1)
    elif args.kontrollera_alla:
        alla_uppe = kontrollera_alla(servrar)
        spara_servrar(servrar, fil_namn)
        if alla_uppe:
            sys.exit(0)
        else:
            sys.exit(1)
    elif args.export:
        exportera_csv(servrar)
    else:
        starta_meny(servrar,fil_namn)


if __name__ == "__main__":
    main()







