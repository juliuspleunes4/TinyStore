import sys
from colorama import Fore, init  # https://pypi.org/project/colorama/

# LET OP!! DIT IS DE VEROUDERDE VERSIE! GEBRUIK MAIN2.PY!!!
# LET OP!! DIT IS DE VEROUDERDE VERSIE! GEBRUIK MAIN2.PY!!!
# LET OP!! DIT IS DE VEROUDERDE VERSIE! GEBRUIK MAIN2.PY!!!
# LET OP!! DIT IS DE VEROUDERDE VERSIE! GEBRUIK MAIN2.PY!!!
# LET OP!! DIT IS DE VEROUDERDE VERSIE! GEBRUIK MAIN2.PY!!!



# https://docs.python.org/3/tutorial/index.html

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
    print(Fore.RED + "3. Afsluiten")
    keuze = input(Fore.WHITE + "Voer je keuze in: ")
    return keuze


def main():
    while True:
        keuze = toon_menu()
        if keuze == '1':
            from Sprint1.sprint1 import nummer_raad_spel
            nummer_raad_spel()
        elif keuze == '2':
            from Sprint2galgje.galgje import galgje
            galgje()
        elif keuze == '3':
            print(Fore.GREEN + "Bedankt voor het gebruiken van TinyStore by Julius. Tot ziens!")
            sys.exit()
        else:
            print(Fore.RED + "Ongeldige invoer, probeer het opnieuw.")


if __name__ == '__main__':
    main()
