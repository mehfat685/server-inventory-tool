import subprocess
from datetime import datetime


def kontrollera_server(servrar):
   try:
       resultat = subprocess.run(
           ["ping", "-c", "1",servrar["adress"]],
           capture_output=True,
           text=True,
           timeout=5
        )
   
       if resultat.returncode == 0:
            servrar["status"] = "up"
       else:
            servrar["status"] = "down"
   except (FileNotFoundError, subprocess.TimeoutExpired):
       servrar["status"] = "down"

   servrar["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")

   print(f"{servrar['namn']:<15} | {servrar['status']:<10}")
   return servrar["status"]

def kontrollera_alla(servrar):
    alla_uppe = True
    print(f"{'Namn':<15} | {'status':<10}")
    print("-" * 28)
    for server in servrar:
        status = kontrollera_server(server)
        
        if status == "down":
            alla_uppe = False

    return alla_uppe

