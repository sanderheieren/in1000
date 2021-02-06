# Dette programmet skal sjekke om en beboer spier tre måltider på en spesifikk dag
# Skal bruke en ordbok for å ta vare på navn som er nøkkelen, og en liste med tre måltider
# som vil være verdien

# 1 lager ordbok for beboer samt tre måltider i lister

måltiderForBeboer = {
    "sander": ['eple', 'laks', 'salat'],
    "tommy": ['pære', 'kylling', 'potet'],
    "berit": ['druer', 'potet', 'gulerot'],
    "torid": ['banan', 'bønner', 'rødbet'],
}

# Definerer prosedyre for å skrive ut måltider til gitt beboer.


def fåMåltiderForBeboer():
    print(
        f"Du kan se måltider til følgende beboere:\n{måltiderForBeboer.keys()}")
    navnPåBeboer = input("Hvem vil du se måltidene til? ")
    if navnPåBeboer.lower() in måltiderForBeboer.keys():
        print(
            f"Måltidene for {navnPåBeboer} er:\n{måltiderForBeboer[navnPåBeboer]}")
    else:
        print(
            f"Det finnes ikke noen måltider for {navnPåBeboer}, dessverre...")


# Kaller på prosedyren
fåMåltiderForBeboer()
