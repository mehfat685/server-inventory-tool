import csv
from pathlib import Path
from datetime import datetime

def exportera_csv(servrar):
    rapporter = Path("rapporter")
    rapporter.mkdir(exist_ok=True)

    nu = datetime.now()
    filnamn = f"inventering_{nu:%Y-%m-%d_%H%M%S}.csv"
    rapport = rapporter / filnamn


    kolumner = ["namn", "adress", "miljo", "roll","status","senast_kontrollerad"]

    with rapport.open("w", newline="",encoding="utf-8") as fil:
        writer = csv.DictWriter(fil, fieldnames=kolumner)
        writer.writeheader()
        writer.writerows(servrar)
    print(f"CSV-rapport skapad: {rapport}")

