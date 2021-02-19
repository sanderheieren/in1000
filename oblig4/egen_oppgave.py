# Dette programmet skal holde styr på, legge til og skrive ut venners bursdager

bursdager = {}


def leggTilBursdag(navn, bursdag):
    bursdager[navn] = bursdag
    print(f"{navn} lagt til med bursdag {bursdag}")


def skrivUtBursdag(navn):
    if not navn in bursdager:
        print(f'{navn} finnes ikke i din vennekrets')
        return
    print(f'{navn} har bursdag {bursdager[navn]}')


def skrivUtAlleBursdager():
    for navn, bursdag in bursdager.items():
        print(f'{navn} har bursdag {bursdag}')


def hentKommando():
    print('\nVelkommen til dine venners bursdagssystem!\n')
    print('Her kommer dine ulike kommandoer du kan utføre:')
    print("'1' - legger til eller endrer nåværende bursdag")
    print("'2' - skriver ut bursdag for en bestemt venn")
    print("'3' - viser alle dine venners bursdag")
    print("'0' - gå ut av programmet\n")
    return input('Hva vil du gjøre?\n')


while(True):
    kommando = hentKommando()

    # Legg til
    if kommando == "1":
        navn = input('Skriv inn NAVN på hvem du vil legge til/endre på:\n')
        bursdag = input(f'Når har {navn} bursdag?:\n')
        leggTilBursdag(navn, bursdag)

    # Skriv ut enkelt
    elif kommando == "2":
        navn = input('Hvem sin bursdag vil du se?\n')
        skrivUtBursdag(navn)

        # Skriv ut alle sin bursdag
    elif kommando == "3":
        skrivUtAlleBursdager()

    elif kommando == '0':
        break

        print()
