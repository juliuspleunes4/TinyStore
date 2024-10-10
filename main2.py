import sys
import hashlib
import json
import os
from colorama import Fore, init  # https://pypi.org/project/colorama/

# https://docs.python.org/3/tutorial/index.html

init() # start colorama

huidige_gebruiker = None

# bestand voor accounts
USERS_FILE = 'users.json'

# controleer of het users-bestand bestaat (anders maak het aan)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as file:
        json.dump({}, file)

# https://stackoverflow.com/questions/62527331/what-does-hexdigest-do-in-python
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# functie om een wachtwoord te hashen
def hash_wachtwoord(wachtwoord):
    return hashlib.sha256(wachtwoord.encode()).hexdigest()


# functie om een nieuwe gebruiker aan te maken
def nieuwe_gebruiker():
    while True:  # blijft herhalen totdat een unieke gebruikersnaam wordt ingevoerd door user
        print(Fore.LIGHTBLUE_EX + "Voer 'q' in om terug te gaan naar het inlogscherm.") # als user bijv wilt inloggen en verkeerd typte
        gebruikersnaam = input("Kies een gebruikersnaam: ").lower()  # .lower zorgt dat het niet hoofdlettergevoelig is

        if gebruikersnaam == 'q':
            print(Fore.YELLOW + "Terug naar het inlogscherm...")
            return False  # terug naar het inlogscherm als gebruiker "q" typt

        wachtwoord = input("Kies een wachtwoord: ")
        wachtwoord_hash = hash_wachtwoord(wachtwoord) # hasht het wachtwoord zodat het veiliger is opgeslagen

        with open(USERS_FILE, 'r+') as file:
            users = json.load(file)
            if gebruikersnaam in users: # gebruikersnaam is al bezet
                print(Fore.RED + "Gebruikersnaam bestaat al. Probeer een andere.")
            else:
                users[gebruikersnaam] = wachtwoord_hash
                file.seek(0)
                json.dump(users, file)
                print(Fore.GREEN + "Gebruiker succesvol aangemaakt.")
                return True  # stop met vragen zodra account succesvol is aangemaakt


# functie om in te loggen als gebruiker al account heeft
def login(automatisch=False, gebruikersnaam=None):
    if automatisch:
        print(Fore.GREEN + "Automatisch ingelogd na het aanmaken van een account.")
        # hier wordt geen wachtwoord gevraagd, omdat het een automatische login is nadat gebruiker account had gemaakt
    else:
        gebruikersnaam = input("Gebruikersnaam: ").lower()  # .lower zorgt dat het niet hoofdlettergevoelig is

    # als user ongeldige gebruikersnaam invoert
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
        if gebruikersnaam not in users:
            print(Fore.RED + "Gebruiker bestaat niet.")
            return False, None

    # wachtwoord vragen en blijven vragen tot het correct is
    while True:
        if not automatisch:
            wachtwoord = input("Wachtwoord: ")
            wachtwoord_hash = hash_wachtwoord(wachtwoord)
            if users[gebruikersnaam] == wachtwoord_hash:
                print(Fore.GREEN + "Inloggen succesvol.")
                return True, gebruikersnaam
            else:
                print(Fore.RED + "Onjuist wachtwoord. Probeer het opnieuw.")
        else:
            # automatisch inloggen na aanmaken account
            return True, gebruikersnaam


# functie voor het oproepen van het dagboekspel
def dagboek_spel(gebruiker):
    from Sprint2dagboek.Sprint2dagboek import main as dagboek_main
    dagboek_main(gebruiker)


# toon het hoofdmenu
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


# hoofdprogrammaq

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

    # https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
    if keuze == '1':
        if nieuwe_gebruiker():  # controleert of de gebruiker succesvol is aangemaakt
            gebruikersnaam = input(
                "Herhaal je gebruikersnaam om automatisch in te loggen: ").lower()  # .lower zorgt dat het niet hoofdlettergevoelig is
            succes, gebruikersnaam = login(automatisch=True, gebruikersnaam=gebruikersnaam)
            if succes:
                huidige_gebruiker = gebruikersnaam
            while True:
                keuze = toon_menu()
                if keuze == '1':
                    from Sprint1.sprint1 import nummer_raad_spel
                    nummer_raad_spel()
                elif keuze == '2':
                    from Sprint2galgje.galgje import galgje
                    galgje()
                elif keuze == '3':
                    dagboek_spel(huidige_gebruiker)
                elif keuze == '4':
                    print(Fore.GREEN + "Bedankt voor het gebruiken van TinyStore by Julius. Tot ziens!")
                    sys.exit()
                else:
                    print(Fore.RED + "Ongeldige invoer, probeer het opnieuw.")
        else:
            main()  # Als de user "q" invoert ga terug naar de hoofdmenu (inlogscherm)

    elif keuze == '2':
            succes, gebruikersnaam = login()
            if succes:
                huidige_gebruiker = gebruikersnaam
            while True:
                keuze = toon_menu()
                if keuze == '1':
                    from Sprint1.sprint1 import nummer_raad_spel
                    nummer_raad_spel()
                elif keuze == '2':
                    from Sprint2galgje.galgje import galgje
                    galgje()
                elif keuze == '3':
                    dagboek_spel(huidige_gebruiker)
                elif keuze == '4':
                    print(Fore.GREEN + "Bedankt voor het gebruiken van TinyStore by Julius. Tot ziens!")
                    sys.exit()
                else:
                    print(Fore.RED + "Ongeldige invoer, probeer het opnieuw.")
    else:
        print(Fore.RED + "Ongeldige keuze. Programma wordt beëindigd.")


if __name__ == '__main__':
    main()
