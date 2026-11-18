Server Inventory Tool
1. Projektet
Ett python program som hanterar och kontrollerar servrar. Genom detta program kan man lägga till, ta bort eller kontrollera om en server svarar på ping. Det sparar informationen som är nödvändigt till en server bland annat ip-adress, miljo,roll,status och senast kontrollerade datum. Det kan användas på två sätt. för det första som interaktiva meny och för det andra med hjälp av kommandot utan att starta menyn. När man lägger en ny server får den statusen unknown och efter ping kontroll antingen up eller down status värde. Dessutom kan man inte lägga till en servers namn som redan finns. Den har även restriktioner för prod miljä och frågar igen om man vill ta bort prod miljö. 

2.Funktioner

a) Visa alla servrar
b) Lägga till en server
c) Ta bort en server
d) Finns en fil
e) Giltig miljo
f) läsa servrar från json
g) spara servrar från json
h) Exportera rapporter till csv

3. Installation och krav
Det behövs
i) Python3
ii) Kommandot ping
iii) En Linux terminal eller container
iv) projektets python filer

jag har utvecklat min projekt i en Linux miljö med hjälp av podman och använder fedora image i min container där python3 och paketet iputils är installerad. iputils krävs för att man kunna köra ping kommandot annars får man filnotfounderror. 

4. Starta programmet
Öpnna terminalen och gå till projektmappen.
Programmet körs med kalle python3.
kalle är ett alias som jag har skapat för att köra python i min podman container.Det är specifikt för min egen miljö. 
Starta menyn genom: kalle python3 main.py
Om python3 ch ping är installerad på datorn kan programmet startas direkt med kommandot python3 main.py
När programmet körs visas följande meny
=== SERVER INVENTORY TOOL ===
1. Visa alla servrar
2. Visa servrar i en viss miljo
3. Lägg till en server
4. Ta bort en server
5. Kontrollera en server
6. Kontrollera alla servrar
7. Exportera CSV
8. Avsluta
Man borde skriva en siffra mellan 1-8 och om man skriva något fel programmet visar fel meddelandet och man får försöka igen.

5. Använda Kommandot
Programmet använde modulen argparse och kan köras olika kommandot.

a) visa alla servrar:
   kalle python3 main.py --lista

b) visa en specifikt miljo server:
   kalle python3 main.py --lista --miljo prod

c) kontrollera en server:
   kalle python3 main.py --kontrollera web01

d) kontrollera alla servrar:
   kalle python3 main.py --kontrollera-alla

e) exportera CSV:
   kalle python3 main.py --export

f) visa hjälp meny:
   kalle python3 main.py --help

6. Data lagring
Varje servers information lagras som en dictionary i en list på följande sätt.
{   
   "namn":"web01",
   "adress":"127.0.0.1",
   "miljo":"prod",
   "roll":"webbserver",
   "status":"unkown",
   "senast_kontrollerad":""
}
på det sättet lagras alla servrar i en lista och när programmet startas läses informationen från json filen. Denna filen updateras varje gång en ny server läggas till eller tas bort eller kontrolleras. Om json filen finns inte programmet kan startas med en tomt lista.

7. Miljövariable
Programmet använder servrar.json som standard värde men kan man använda en annan fil också genom miljövariablen INVENTORY_DATAFIL. och då man gör så..
INVENTORY_DATAFIL=test.json python3 main.py eller kan man sätta den i själva programmet också. När programmet körs i main ( fil_namn=os.getenv("INVENTORY_DATAFIL","servrar.json") om vi har inte satt ett värde för inventory data fil då blir värde servrar.json för att det är ett default värde som vi satte.

8. Kontrollera servrar med ping
Jag använde subprocess för att kunna kontrollera ping i kontroller.py. Programmet skickar en ping request till serverns adress och kontrollerar resultatets exitkod. Om returkoden är 0 blir serverns status up för att lyckades och Om blir 1 det är down och misslyckades. Programet sparar även datum och tid för den senaste kontrollen i formatet 2026-11-17 18:30. Jag har även hanterat det med try och except att om kommandot tar för lång tid programmet kastar inte fel. Efter en kontroll kan exitkoden visas i terminal med hjälp av echo $? 

9. Exportera CSV rapporter
Programmet kan skapa csv rapport genom meny om man väljer 7 eller genom kommandot python3 main.py --export
Om mappen inte finns programmet skapar den med hjälp av pathlib och rapportens filnamn innehåller datum och tid till exempel rapporter/inventering_2026-11-17_183000.csv
CSV filen består av följande kolumner namn, adress, miljo, roll, status, senast_kontrollerad. 

10. Projektstruktur
main.py - Startar programmet och hanterar kommando
meny.py - Hanterar den vanliga menyn.
lagring.py Läser oc sparar JSON.
kontroller.py - Kontrollerar servrar med ping.
rapporter.py - Skapar csv-rapporter med serverinformation.
servrar.json . inhåller den sparade servrar.
readme.md - beskriver projektet.
redogorelse.md - innehåller förklaring av kod och svar på frågor.
.gitignore - används för att undvika skicka känsliga data eller vissa filer till git repo.

11. Utvecklingsmiljä och hjälpmedel
a) Python3.
b) Linux.
c) Podman
d) Git
e) GitHub

Jag har använt presentationer, klassens mini projekt, AI som stöd under utveckling.
