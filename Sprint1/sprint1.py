import random
from colorama import Fore, Style, init  # https://pypi.org/project/colorama/ (Kleurondersteuning in de terminal)

init(autoreset=True)

# https://docs.python.org/3/tutorial/index.html

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def nummer_raad_spel():
    while True:
        print(Fore.MAGENTA + "Welkom bij het nummer raad spel!")
        te_raden_nummer = random.randint(1, 50) # Willekeurig nummer tussen 1 en 50
        aantal_pogingen = 5 # Maximaal aantal pogingen
        print(Fore.MAGENTA + f"Je hebt {aantal_pogingen} pogingen om het juiste nummer te raden!")

        for poging in range(1, aantal_pogingen + 1):
            invoer = input(Fore.MAGENTA + f"Poging {poging}: Raad een nummer tussen 1 en 50 of type 'exit' om te stoppen: ")
            # https://docs.python.org/3/tutorial/controlflow.html#if-statements
            if invoer.lower() == 'exit': # Speler kan kiezen om te stoppen
                print(Fore.YELLOW + "Terugkeer naar het hoofdmenu...")
                return

            try:
                gok = int(invoer) # Controle of invoer een geldig nummer is
            except ValueError: # Foutmelding bij ongeldige invoer
                print(Fore.RED + "Voer alstublieft een geldig nummer in.")
                continue

            if gok == te_raden_nummer:
                print(Fore.GREEN + f"Gefeliciteerd! Je hebt het nummer {te_raden_nummer} geraden in {poging} pogingen!") # Correct geraden
                break
            elif gok < te_raden_nummer:
                print(Fore.CYAN + "Het nummer is hoger dan je gok.") # Melding dat verschijnt als correcte nummer hoger is dan gok
            else:
                print(Fore.CYAN + "Het nummer is lager dan je gok.") # Melding dat verschijnt als correcte nummer lager is dan gok

        if gok != te_raden_nummer and invoer.lower() != 'exit': # Bij geen juiste gok
            print(Fore.RED + f"Helaas, je hebt geen pogingen meer over. Het juiste nummer was {te_raden_nummer}.") # Incorrect geraden

        if input(Fore.CYAN + "Type 'exit' om te stoppen of druk op Enter om opnieuw te spelen: ").lower() == 'exit':
            break

# nummer_raad_spel() # (Deze functie wordt aangeroepen vanuit de TinyStore)
