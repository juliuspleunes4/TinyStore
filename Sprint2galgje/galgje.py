import os
import random
import datetime
from colorama import Fore, init

# https://docs.python.org/3/tutorial/index.html
init(autoreset=True)

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def laad_woorden(bestand):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bestand_pad = os.path.join(dir_path, bestand)
    try:
        with open(bestand_pad, 'r') as file:
            woorden = file.read().splitlines()
        return woorden
    except FileNotFoundError:
        print(Fore.RED + f"Kon het bestand {bestand} niet vinden :(")
        return []
    except Exception as e:
        print(Fore.RED + f"Er is een fout opgetreden: {e}")
        return []

def kies_willekeurig_woord(moeilijkheidsgraad):
    if moeilijkheidsgraad == 'makkelijk':
        woorden = laad_woorden('makkelijk.txt')
    elif moeilijkheidsgraad == 'gemiddeld':
        woorden = laad_woorden('gemiddeld.txt')
    elif moeilijkheidsgraad == 'moeilijk':
        woorden = laad_woorden('moeilijk.txt')
    else:
        return None
    return random.choice(woorden)

def sla_score_op(naam, woord, aantal_pogingen, geraden):
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('score.txt', 'a') as file:
        file.write(f"Naam: {naam}, Woord: {woord}, Geraden: {geraden}, Aantal pogingen: {aantal_pogingen}, Datum: {datum}\n")

def galgje():
    while True:
        print(Fore.CYAN + "Welkom bij Galgje!")
        naam = input(Fore.CYAN + "Wat is je naam?: ")
        moeilijkheidsgraad = ""
        while moeilijkheidsgraad not in ['makkelijk', 'gemiddeld', 'moeilijk']:
            moeilijkheidsgraad = input(Fore.GREEN + "Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
            if moeilijkheidsgraad == 'exit':
                print(Fore.YELLOW + "Terugkeer naar het hoofdmenu...")
                return
            if moeilijkheidsgraad not in ['makkelijk', 'gemiddeld', 'moeilijk']:
                print(Fore.RED + "Ongeldige moeilijkheidsgraad! Probeer opnieuw.")

        te_raden_woord = kies_willekeurig_woord(moeilijkheidsgraad)
        aantal_pogingen = len(te_raden_woord) + 2
        geraden_woorden = ['_'] * len(te_raden_woord)
        gebruikte_letters = []

        print(Fore.CYAN + f"Je hebt {aantal_pogingen} pogingen om het woord te raden.")
        while aantal_pogingen > 0:
            print(Fore.CYAN + f"Status van het woord: {' '.join(geraden_woorden)}")
            print(Fore.MAGENTA + f"Gebruikte letters: {', '.join(gebruikte_letters)}")
            gok = input(Fore.CYAN + "Raad een letter of typ 'exit' om te stoppen: ").lower()

            if gok == 'exit':
                print(Fore.YELLOW + "Terugkeer naar het hoofdmenu...")
                return

            if gok in gebruikte_letters:
                print(Fore.RED + "Je hebt deze letter al geraden.")
                continue

            gebruikte_letters.append(gok)

            if gok in te_raden_woord:
                print(Fore.GREEN + "Goed geraden!")
                for i, letter in enumerate(te_raden_woord):
                    if letter == gok:
                        geraden_woorden[i] = gok
            else:
                aantal_pogingen -= 1
                print(Fore.RED + f"Fout! Je hebt nog {aantal_pogingen} pogingen over.")

            if '_' not in geraden_woorden:
                print(Fore.GREEN + f"Gefeliciteerd {naam}, je hebt het woord '{te_raden_woord}' geraden!")
                sla_score_op(naam, te_raden_woord, aantal_pogingen, geraden=True)
                break

            if aantal_pogingen == 0:
                print(Fore.RED + f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}.")
                sla_score_op(naam, te_raden_woord, aantal_pogingen, geraden=False)

        if input(Fore.CYAN + "Type 'exit' om te stoppen of druk op Enter om opnieuw te spelen: ").lower() == 'exit':
            break

# galgje() (wordt uitgevoerd via de TinyStore)
