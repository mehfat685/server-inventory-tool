from lagring import spara_servrar
from kontroller import kontrollera_server, kontrollera_alla
from rapporter import exportera_csv

def visa_meny():
    print("\n ==== SERVER INVENTORY TOOL ===")
    print(" 1. Visa alla servrar")
    print(" 2. Visa servrar i en viss miljo")
    print(" 3. Lägg till en server")
    print(" 4. Ta bort en server")
    print(" 5. Kontrollera en server")
    print(" 6. kontrollera alla servrar")
    print(" 7. Exportera CSV")
    print(" 8. Avsluta")

def starta_meny(servrar,fil_namn):
    while True:
        visa_meny()
        choice =input("Välja ett val: ")

        match choice:
           case "1":
               print("\n ==== All SERVERS ====")
               visa_alla_servrar(servrar)
           case "2":
               visa_servrar_miljo(servrar)
           case "3":
               lagg_till_servrar(servrar,fil_namn)
           case "4":
               ta_bort_server(servrar,fil_namn)
           case "5":
               namn = input("Ange serverns namn: ").strip()
               current_server = None
               for server in servrar:
                   if server["namn"] == namn:
                       current_server = server
                       break
               if current_server is None:
                   print("Servern finns inte!")
               else:
                   print(f"{'Namn':<15} | {'Status':<10}")
                   print("-" * 28)
                   kontrollera_server(current_server)
                   spara_servrar(servrar,fil_namn)
           case "6":
                   kontrollera_alla(servrar)
                   spara_servrar(servrar,fil_namn)
                   print("Alla servrar har kontrollerats!")
           case "7":
               exportera_csv(servrar)
           case "8":
               print("Hejdå!")
               break
           case _:
               print("Ogiltigt val. försök igen!")


def visa_alla_servrar(servrar):
     
     print(f"{'Namn':<15} | {'Adress':<20} | {'Miljo':<10} | {'Roll':<25} | {'status':<10}")
     print("-"*95)
     for server in servrar: 
         print(f"{server['namn']:<15} | "
               f"{server['adress']:<20} | "
               f"{server['miljo']:<10} | "
               f"{server['roll']:<25} | "
               f"{server['status']:<10}")

   
    

def visa_servrar_miljo(servrar):
    choice = input("Vilken miljo servrar vill du kolla (prod, dev, test): ")

    if giltig_miljo(choice):
        print(f"{'Namn':<15} | {'Miljo':<15}")
        print("-" * 28)
        for server in servrar:
            if choice == server["miljo"]: 
                print(f"{server['namn']:<15} | {server['miljo']}")
    else:
        print("Ogiltigt miljo!")
        return   

#my own method2 for checking miljo
def giltig_miljo(miljo):
    if miljo in ("prod","dev","test"):
        return True
    else:
        return False


#my own method3 for checking server's name existance
def server_namn_finns(servrar,namn):
    for server in servrar:
        if server["namn"] == namn:
            return True
    return False


def lagg_till_servrar(servrar,fil_namn):
    namn = input(f"{'Ange namn':<15}: " ).strip()
    
    if server_namn_finns(servrar,namn):
        print("Namnet finns redan!")
    else:
        adress = input(f"{'Ange adress':<15}: ")
        while True:
            miljo =input(f"{'Ange miljo':<15}: ")
            if giltig_miljo(miljo):
                break
            else:
                print("Ogiltigt miljo. Giltiga värde dev, prod, test. Försök igen!")
        role = input(f"{'Ange role':<15}: ")
        ny_server = {

               "namn":namn,
               "adress":adress,
               "miljo":miljo,
               "roll":role,
               "status":"unknown",
               "senast_kontrollerad":""
              }
        servrar.append(ny_server)
        spara_servrar(servrar,fil_namn)


def ta_bort_server(servrar,fil_namn):
    server_tas_bort = input("Ange serverns namn som ska tas bort: ")
    
    for server in servrar:
        if server["namn"] == server_tas_bort:
            print("Server hittades!")
  
            if server["miljo"] == "prod":
                print("Produktion Server!")
                svar = input("Är du säkert att du vill ta bort produktionsservern? svara med små bokstäver (ja/nej): ")
                if svar == "ja":
                    servrar.remove(server)
                    spara_servrar(servrar,fil_namn)
                    print("Produktions servern togs bort.")
                else:
                    print("Processen avslutas! Produktions servern behållas.")
            else:
                servrar.remove(server)
                spara_servrar(servrar,fil_namn)
                print("Servern togs bort.")
            return
    print("Servern finns inte!")
