import os
import random
import datetime
from colorama import Fore, init # https://pypi.org/project/colorama/ (voor kleur in de terminal)

# https://docs.python.org/3/tutorial/index.html

init(autoreset=True)

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def laad_woorden(bestand):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bestand_pad = os.path.join(dir_path, bestand)
    try:
        with open(bestand_pad, 'r') as file: # leest het bestand dat de woorden voor gagje bevat
            woorden = file.read().splitlines()
        return woorden
    except FileNotFoundError: # error melding als het bestand niet gevonden kan worden
        print(Fore.RED + f"Kon het bestand {bestand} niet vinden :(")
        return []
    except Exception as e:
        print(Fore.RED + f"Er is een fout opgetreden: {e}")
        return []

# geeft de gebruiker de optie om een moeilijkheidsgraad te kiezen
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

# zorgt dat score wordt bijgehouden en definierd op welke manier de data moet worden opgeslagen
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

        print(Fore.CYAN + f"Je hebt {aantal_pogingen} pogingen om het woord te raden.") # print hoeveel pogingen de user heeft
        while aantal_pogingen > 0:
            print(Fore.CYAN + f"Status van het woord: {' '.join(geraden_woorden)}") # print welke letters uit het woord zijn geraden
            print(Fore.MAGENTA + f"Gebruikte letters: {', '.join(gebruikte_letters)}") # print welke letters zijn gegokt
            gok = input(Fore.CYAN + "Raad een letter of typ 'exit' om te stoppen: ").lower() # zorgt dat de user een gok kan doen of terug kan gaan naar main menu

            if gok == 'exit': # als user "exit" typt gaat hij terug naar main menu
                print(Fore.YELLOW + "Terugkeer naar het hoofdmenu...")
                return

            if gok in gebruikte_letters: # als user een letter dubbel probeert geeft de terminal dit aan
                print(Fore.RED + "Je hebt dit letter al geraden.")
                continue

            gebruikte_letters.append(gok)

            if gok in te_raden_woord: # als user goed gokt
                print(Fore.GREEN + "Goed geraden!")
                for i, letter in enumerate(te_raden_woord): # https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python (enumerate houdt bij hoevaak loops in een loop voorkomt)
                    if letter == gok:
                        geraden_woorden[i] = gok
            else:
                aantal_pogingen -= 1 # zorgt dat er 1 poging minder mogelijk is nadat gebruiker fout heeft gegokt
                print(Fore.RED + f"Fout! Je hebt nog {aantal_pogingen} pogingen over.")

            if '_' not in geraden_woorden: # als elke letter is vervangen met een _ nadat het correct is geraden is er geen _ meer in het woord te vinden. Als dit het geval is heeft de user alle letters dus geraden
                print(Fore.GREEN + f"Gefeliciteerd {naam}, je hebt het woord '{te_raden_woord}' geraden!")
                sla_score_op(naam, te_raden_woord, aantal_pogingen, geraden=True)
                break

            if aantal_pogingen == 0: # user heeft geen pogingen meer
                print(Fore.RED + f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}.")
                sla_score_op(naam, te_raden_woord, aantal_pogingen, geraden=False)

        if input(Fore.CYAN + "Type 'exit' om te stoppen of druk op Enter om opnieuw te spelen: ").lower() == 'exit':
            break

# galgje() (wordt uitgevoerd via de TinyStore)
