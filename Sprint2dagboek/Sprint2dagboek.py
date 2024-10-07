import csv
import os
from colorama import Fore, init # https://pypi.org/project/colorama/ (voor kleur in de terminal)
from datetime import datetime

# https://earthly.dev/blog/csv-python/
CSV_FILENAME = 'dagboek.csv'

if not os.path.exists(CSV_FILENAME):
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['datum', 'tekst'])

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def vraag_wachtwoord():
    wachtwoord = "geheim"
    while True:
        invoer = input(Fore.LIGHTBLUE_EX + "Voer het wachtwoord in om toegang te krijgen tot het dagboek: ")
        if invoer == wachtwoord:
            print(Fore.GREEN + "Wachtwoord correct, toegang verleend.")
            break
        else:
            print(Fore.RED + "Onjuist wachtwoord. Probeer het opnieuw.")

# vraagt aan de user voor welke datum hij/zij een nieuwe entry wilt maken
def vraag_datum():
    keuze = input(Fore.LIGHTBLUE_EX +"Wil je een actie uitvoeren voor vandaag (ja/nee)? ")
    if keuze.lower() == 'ja':
        return datetime.today().strftime(Fore.LIGHTBLUE_EX + '%Y-%m-%d')
    else:
        datum = input(Fore.LIGHTBLUE_EX + "Voer een datum in (YYYY-MM-DD): ")
        return datum

# hier wordt gedefinierd welke data op welke manier wordt geschreven in het bestand
def schrijf_tekst(datum):
    with open(CSV_FILENAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        bestaande_data = {row['datum']: row['tekst'] for row in reader}

# welke actie moet worden uitgevoerd als er al data staat voor gegeven datum
    if datum in bestaande_data:
        keuze = input(Fore.CYAN + "Er bestaat al een tekst voor deze datum. Wil je de tekst herschrijven (ja) of aanvullen (nee)? ")
        if keuze.lower() == 'ja':
            tekst = input(Fore.CYAN + f"Schrijf nieuwe tekst voor {datum}: ")
        else:
            tekst = bestaande_data[datum] + "\n" + input(Fore.LIGHTBLUE_EX + f"Vul aan voor {datum}: ")
    else:
        tekst = input(Fore.CYAN + f"Schrijf nieuwe tekst voor {datum}: ")

    bestaande_data[datum] = tekst

    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['datum', 'tekst'])
        for d, t in bestaande_data.items():
            writer.writerow([d, t])

# geeft de gebruiker de al geschreven tekst
def lees_tekst(datum):
    with open(CSV_FILENAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['datum'] == datum:
                print(Fore.MAGENTA + f"Dagboektekst van {datum}: {row['tekst']}")
                return
        print(Fore.RED + f"Geen tekst gevonden voor {datum}")

def main():
    vraag_wachtwoord()
    datum = vraag_datum()

    actie = input(Fore.LIGHTBLUE_EX + "Wil je lezen (1) of schrijven (2)? Voer 1 of 2 in: ")
    if actie == '1':
        lees_tekst(datum)
    elif actie == '2':
        schrijf_tekst(datum)
    else:
        print(Fore.RED + "Ongeldige keuze.")


if __name__ == "__main__":
    main() # (deze functie wordt aangeroepen via de TinyStore)
