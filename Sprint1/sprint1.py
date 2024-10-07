import random
from colorama import Fore, Style, init  # https://pypi.org/project/colorama/ (kleur toevoeging)

init(autoreset=True)

# https://docs.python.org/3/tutorial/index.html

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def nummer_raad_spel():
    while True:
        print(Fore.MAGENTA + "Welkom bij het nummer raad spel!")
        te_raden_nummer = random.randint(1, 50) # kiest willekeurig nummer tussen 1 en 50
        aantal_pogingen = 5 # maximaal aantal pogingen is 5
        print(Fore.MAGENTA + f"Je hebt {aantal_pogingen} pogingen om het juiste nummer te raden!")

        # houdt het aantal pogingen dat je nog hebt tijdens spelen bij
        for poging in range(1, aantal_pogingen + 1):
            invoer = input(Fore.MAGENTA + f"Poging {poging}: Raad een nummer tussen 1 en 50 of type 'exit' om te stoppen: ")
            # https://docs.python.org/3/tutorial/controlflow.html#if-statements
            if invoer.lower() == 'exit': # speler kan "exit" typen om terug te gaan naar main menu
                print(Fore.YELLOW + "Terugkeer naar het hoofdmenu...")
                return

            try:
                gok = int(invoer) # controleert of de user eene geldige invoer heeft gedaan
            except ValueError: # foutmelding bij ongeldige invoer
                print(Fore.RED + "Voer alstublieft een geldig nummer in.")
                continue

            if gok == te_raden_nummer:
                print(Fore.GREEN + f"Gefeliciteerd! Je hebt het nummer {te_raden_nummer} geraden in {poging} pogingen!") # correct gegokt
                break
            elif gok < te_raden_nummer:
                print(Fore.CYAN + "Het nummer is hoger dan je gok.") # melding dat wordt geprint als correcte nummer hoger is dan gok
            else:
                print(Fore.CYAN + "Het nummer is lager dan je gok.") # melding dat wordt geprint als correcte nummer lager is dan gok
        # https://www.datacamp.com/tutorial/not-equal-python
        if gok != te_raden_nummer and invoer.lower() != 'exit': # als user het niet geraden heeft
            print(Fore.RED + f"Helaas, je hebt geen pogingen meer over. Het juiste nummer was {te_raden_nummer}.") # incorrect geraden

        if input(Fore.CYAN + "Type 'exit' om te stoppen of druk op Enter om opnieuw te spelen: ").lower() == 'exit':
            break

# nummer_raad_spel() # (deze functie wordt aangeroepen vanuit de TinyStore)
