import random
from colorama import Fore, Style, init # https://pypi.org/project/colorama/ (kleur toevoeging)

init(autoreset=True)

# https://docs.python.org/3/tutorial/index.html

# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# nieuw deck te maken
def maak_deck():
    deck = []
    kleuren = ['♥️', '♦️', '♣️', '♠️']
    waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Dame', 'Heer', 'Aas']
    for kleur in kleuren:
        for waarde in waarden:
            deck.append(f'{waarde} {kleur}')
    random.shuffle(deck)
    return deck


# waarde van een hand te berekenen
def bereken_waarde(hand):
    waarde = 0
    azen = 0
    waardes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Boer': 10, 'Dame': 10, 'Heer': 10, 'Aas': 11}
    for kaart in hand:
        kaart_waarde = kaart.split(' ')[0]
        waarde += waardes[kaart_waarde]
        if kaart_waarde == 'Aas':
            azen += 1
    while waarde > 21 and azen:
        waarde -= 10
        azen -= 1
    return waarde


# kaart te trekken
def trek_kaart(deck):
    return deck.pop()


# spel te spelen
def speel_blackjack():
    while True:
        deck = maak_deck()
        speler_hand = [trek_kaart(deck), trek_kaart(deck)]
        dealer_hand = [trek_kaart(deck), trek_kaart(deck)]

        print(Fore.CYAN + f'Jouw kaarten: {speler_hand} (waarde: {bereken_waarde(speler_hand)})')
        print(Fore.BLUE + f'Dealer\'s zichtbare kaart: {dealer_hand[0]} (waarde: {bereken_waarde([dealer_hand[0]])})')

        # controleer of de speler meteen 21 heeft met de eerste twee kaarten
        if bereken_waarde(speler_hand) == 21:
            print(Fore.GREEN + 'Gefeliciteerd! Je hebt meteen 21 en wint!')
            if opnieuw_spelen():
                continue
            else:
                break

        while True:
            # vraag om invoer en strip witruimte
            actie = input(
                Fore.LIGHTBLUE_EX + 'Wil je een kaart trekken of passen? (t/p): ' + Style.RESET_ALL).strip().lower()

            if actie == 't':
                speler_hand.append(trek_kaart(deck))
                print(Fore.CYAN + f'Jouw kaarten: {speler_hand} (waarde: {bereken_waarde(speler_hand)})')

                # Controleer of de speler 21 heeft bereikt na het trekken van een kaart
                if bereken_waarde(speler_hand) == 21:
                    print(Fore.GREEN + 'Gefeliciteerd! Je hebt precies 21 en wint!')
                    break
                elif bereken_waarde(speler_hand) > 21:
                    print(Fore.RED + 'Je hebt meer dan 21 punten. Je verliest!')
                    break
            elif actie == 'p':
                break
            else:
                print(Fore.RED + 'Ongeldige invoer. Probeer opnieuw.')

        # controleer na het trekken van kaarten of we het spel opnieuw moeten starten
        if bereken_waarde(speler_hand) >= 21:
            if opnieuw_spelen():
                continue
            else:
                break

        # dealer speelt
        while bereken_waarde(dealer_hand) < 17:
            dealer_hand.append(trek_kaart(deck))

        print(Fore.BLUE + f'Dealer\'s kaarten: {dealer_hand} (waarde: {bereken_waarde(dealer_hand)})')

        # winnaar bepalen
        speler_waarde = bereken_waarde(speler_hand)
        dealer_waarde = bereken_waarde(dealer_hand)

        if dealer_waarde > 21 or speler_waarde > dealer_waarde:
            print(Fore.GREEN + 'Gefeliciteerd! Je wint!')
        elif speler_waarde < dealer_waarde:
            print(Fore.RED + 'Helaas, de dealer wint.')
        else:
            print(Fore.YELLOW + 'Gelijkspel!')

        # vraag om opnieuw te spelen
        if not opnieuw_spelen():
            break


def opnieuw_spelen():
    while True:
        opnieuw = input(Fore.CYAN + "Wil je opnieuw spelen? (j/n): ").strip().lower()
        if opnieuw == 'j':
            return True
        elif opnieuw == 'n':
            return False
        else:
            print(Fore.RED + 'Ongeldige invoer. Voer "j" of "n" in.')


if __name__ == '__main__':
    speel_blackjack()
