# Dette programmet skal lage to ulike funksjoner som vil returnere et tall,
# og en annen skal telle antall forekomster av en bokstav

# 1 Definerer funksjon, og sørger for riktig input

def adder(tall1, tall2):
    if(isinstance(tall1, int) and isinstance(tall2, int)):
        print(f"Resultatet av {tall1} + {tall2} er: {tall1 + tall2} ")
        return tall1 + tall2
    print('Ikke gyldig verdi. Sørg for å gi to HELTALL')


adder(-3, 40)
adder(4, 20)

tekst = input('Vær vennlig og skriv inn en vilkårlig tekstreng:\n')
bokstav = input(
    'Skriv inn en bokstav, og jeg skal finne antall forekomster av bokstaven.(Det skilles mellom stor og liten bokstav):\n')

# Definere funksjon som skal telle antall bokstaver i en tekst, med feilsøking


def tellForekomst(minTekst, minBokstav):
    if(len(minTekst) == 0 or len(minBokstav) == 0):
        print('Her skjedde det noe feil. Prøv igjen\n')
        nyTekst = input('Vær vennlig og skriv inn en vilkårlig tekstreng:\n')
        nyBokstav = input(
            'Skriv inn en bokstav, og jeg skal finne antall forekomster av bokstaven.(Det skilles mellom stor og liten bokstav):\n')
        tellForekomst(nyTekst, nyBokstav)
        return
    total = 0
    for letter in minTekst:
        if(letter == minBokstav):
            total += 1
    if(total == 1):
        print(f'{minBokstav} kom {total} gang i "{minTekst}"')
    else:
        print(f'{minBokstav} kom {total} ganger i "{minTekst}"')
    return total


tellForekomst(tekst, bokstav)
