import sys
import hashlib
import json
import os
from colorama import Fore, init  # https://pypi.org/project/colorama/

# https://docs.python.org/3/tutorial/index.html

# Initieer colorama
init()

# Bestanden voor gebruikers en wachtwoorden
USERS_FILE = 'users.json'

# Controleer of het users-bestand bestaat, anders maak het aan
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as file:
        json.dump({}, file)


# Functie om een wachtwoord te hashen
def hash_wachtwoord(wachtwoord):
    return hashlib.sha256(wachtwoord.encode()).hexdigest()


# Functie om een nieuwe gebruiker aan te maken
def nieuwe_gebruiker():
    while True:  # Blijf herhalen totdat een unieke gebruikersnaam wordt ingevoerd
        print(Fore.LIGHTBLUE_EX + "Voer 'q' in om terug te gaan naar het inlogscherm.")
        gebruikersnaam = input("Kies een gebruikersnaam: ").lower()  # Niet hoofdlettergevoelig

        if gebruikersnaam == 'q':
            print(Fore.YELLOW + "Terug naar het inlogscherm...")
            return False  # Terug naar het inlogscherm

        wachtwoord = input("Kies een wachtwoord: ")
        wachtwoord_hash = hash_wachtwoord(wachtwoord)

        with open(USERS_FILE, 'r+') as file:
            users = json.load(file)
            if gebruikersnaam in users:
                print(Fore.RED + "Gebruikersnaam bestaat al. Probeer een andere.")
            else:
                users[gebruikersnaam] = wachtwoord_hash
                file.seek(0)
                json.dump(users, file)
                print(Fore.GREEN + "Gebruiker succesvol aangemaakt.")
                return True  # Stop met vragen zodra de gebruiker succesvol is aangemaakt


# Functie om in te loggen
def login(automatisch=False, gebruikersnaam=None):
    if automatisch:
        print(Fore.GREEN + "Automatisch ingelogd na het aanmaken van een account.")
        # Hier wordt geen wachtwoord gevraagd, omdat het een automatische login is
    else:
        gebruikersnaam = input("Gebruikersnaam: ").lower()  # Niet hoofdlettergevoelig

    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
        if gebruikersnaam not in users:
            print(Fore.RED + "Gebruiker bestaat niet.")
            return False

    # Wachtwoord vragen en blijven vragen tot het correct is
    while True:
        if not automatisch:
            wachtwoord = input("Wachtwoord: ")
            wachtwoord_hash = hash_wachtwoord(wachtwoord)
            if users[gebruikersnaam] == wachtwoord_hash:
                print(Fore.GREEN + "Inloggen succesvol.")
                return True
            else:
                print(Fore.RED + "Onjuist wachtwoord. Probeer het opnieuw.")
        else:
            # Automatisch inloggen na aanmaken account
            return True


# Functie voor het dagboekspel
def dagboek_spel():
    from Sprint2dagboek.Sprint2dagboek import main as dagboek_main
    dagboek_main()


# Toon het hoofdmenu
def toon_menu():
    print(Fore.LIGHTCYAN_EX + """
██╗    ██╗███████╗██╗     ██╗  ██╗ ██████╗ ███╗   ███╗    ██████╗ ██╗     ██╗                                                                     
██║    ██║██╔════╝██║     ██║ ██╔╝██╔═══██╗████╗ ████║    ██╔══██╗██║     ██║                                                                     
██║ █╗ ██║█████╗  ██║     █████╔╝ ██║   ██║██╔████╔██║    ██████╔╝██║     ██║                                                                     
██║███╗██║██╔══╝  ██║     ██╔═██╗ ██║   ██║██║╚██╔╝██║    ██╔══██╗██║██   ██║                                                                     
╚███╔███╔╝███████╗███████╗██║  ██╗╚██████╔╝██║ ╚═╝ ██║    ██████╔╝██║╚█████╔╝                                                                     
 ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═════╝ ╚═╝ ╚════╝                                                                      

████████╗██╗███╗   ██╗██╗   ██╗███████╗████████╗ ██████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗         ██╗██╗   ██╗██╗     ██╗██╗   ██╗███████╗██╗
╚══██╔══╝██║████╗  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝         ██║██║   ██║██║     ██║██║   ██║██╔════╝██║
   ██║   ██║██╔██╗ ██║ ╚████╔╝ ███████╗   ██║   ██║   ██║██████╔╝█████╗      ██████╔╝ ╚████╔╝          ██║██║   ██║██║     ██║██║   ██║███████╗██║
   ██║   ██║██║╚██╗██║  ╚██╔╝  ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██╔══██╗  ╚██╔╝      ██   ██║██║   ██║██║     ██║██║   ██║╚════██║╚═╝
   ██║   ██║██║ ╚████║   ██║   ███████║   ██║   ╚██████╔╝██║  ██║███████╗    ██████╔╝   ██║       ╚█████╔╝╚██████╔╝███████╗██║╚██████╔╝███████║██╗
   ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝    ╚═╝        ╚════╝  ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝

    """)
    print(Fore.GREEN + "1. Speel 'Raad het getal!'")
    print(Fore.GREEN + "2. Speel 'Galgje'")
    print(Fore.GREEN + "3. Speel 'Dagboekspel'")
    print(Fore.RED + "4. Afsluiten")
    keuze = input(Fore.WHITE + "Voer je keuze in: ")
    return keuze


# Hoofdprogramma4

def main():
    print(Fore.LIGHTCYAN_EX + """
██╗    ██╗███████╗██╗     ██╗  ██╗ ██████╗ ███╗   ███╗    ██████╗ ██╗     ██╗                                                                     
██║    ██║██╔════╝██║     ██║ ██╔╝██╔═══██╗████╗ ████║    ██╔══██╗██║     ██║                                                                     
██║ █╗ ██║█████╗  ██║     █████╔╝ ██║   ██║██╔████╔██║    ██████╔╝██║     ██║                                                                     
██║███╗██║██╔══╝  ██║     ██╔═██╗ ██║   ██║██║╚██╔╝██║    ██╔══██╗██║██   ██║                                                                     
╚███╔███╔╝███████╗███████╗██║  ██╗╚██████╔╝██║ ╚═╝ ██║    ██████╔╝██║╚█████╔╝                                                                     
 ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═════╝ ╚═╝ ╚════╝                                                                      

████████╗██╗███╗   ██╗██╗   ██╗███████╗████████╗ ██████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗         ██╗██╗   ██╗██╗     ██╗██╗   ██╗███████╗██╗
╚══██╔══╝██║████╗  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝         ██║██║   ██║██║     ██║██║   ██║██╔════╝██║
   ██║   ██║██╔██╗ ██║ ╚████╔╝ ███████╗   ██║   ██║   ██║██████╔╝█████╗      ██████╔╝ ╚████╔╝          ██║██║   ██║██║     ██║██║   ██║███████╗██║
   ██║   ██║██║╚██╗██║  ╚██╔╝  ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██╔══██╗  ╚██╔╝      ██   ██║██║   ██║██║     ██║██║   ██║╚════██║╚═╝
   ██║   ██║██║ ╚████║   ██║   ███████║   ██║   ╚██████╔╝██║  ██║███████╗    ██████╔╝   ██║       ╚█████╔╝╚██████╔╝███████╗██║╚██████╔╝███████║██╗
   ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝    ╚═╝        ╚════╝  ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝                                                                                                
    """)
    keuze = input(Fore.LIGHTBLUE_EX + "Ben je een nieuwe gebruiker (1) of wil je inloggen (2)? Voer 1 of 2 in: ")

    if keuze == '1':
        if nieuwe_gebruiker():  # Controleert of de gebruiker succesvol is aangemaakt
            gebruikersnaam = input(
                "Herhaal je gebruikersnaam om automatisch in te loggen: ").lower()  # Niet hoofdlettergevoelig
            login(automatisch=True, gebruikersnaam=gebruikersnaam)
            while True:
                keuze = toon_menu()
                if keuze == '1':
                    from Sprint1.sprint1 import nummer_raad_spel
                    nummer_raad_spel()
                elif keuze == '2':
                    from Sprint2galgje.galgje import galgje
                    galgje()
                elif keuze == '3':
                    dagboek_spel()
                elif keuze == '4':
                    print(Fore.GREEN + "Bedankt voor het gebruiken van TinyStore by Julius. Tot ziens!")
                    sys.exit()
                else:
                    print(Fore.RED + "Ongeldige invoer, probeer het opnieuw.")
        else:
            main()  # Als de gebruiker 'q' invoert, terug naar het hoofdmenu (inlogscherm)

    elif keuze == '2':
        if login():
            while True:
                keuze = toon_menu()
                if keuze == '1':
                    from Sprint1.sprint1 import nummer_raad_spel
                    nummer_raad_spel()
                elif keuze == '2':
                    from Sprint2galgje.galgje import galgje
                    galgje()
                elif keuze == '3':
                    dagboek_spel()
                elif keuze == '4':
                    print(Fore.GREEN + "Bedankt voor het gebruiken van TinyStore by Julius. Tot ziens!")
                    sys.exit()
                else:
                    print(Fore.RED + "Ongeldige invoer, probeer het opnieuw.")
    else:
        print(Fore.RED + "Ongeldige keuze. Programma wordt beëindigd.")


if __name__ == '__main__':
    main()
