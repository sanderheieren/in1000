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

# 2, Definerer prosedyre for å skrive ut måltider til gitt beboer.


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

# 3
"""
a)
Hvis ikke noe som helst annen data skal lagres enn brukernavnet ville jeg brukt en mengde. Det fungerer
selvsagt også med en liste, men i en mengde vil alle verdiene være unike. Det kan være en fare for duplikater
om det ville bli brukt en liste. Mengde er også mer effektiv enn lister.

b)
Antar her at det er gitt vi er 'inne' i innlevering 3, og derfor ville jeg ha brukt en ordbok
for å relatere brukernavnet med en poengscore. Dersom man også må definere hva slags samling 'innleverning 3' er,
ville jeg ha hatt alle de ulike innleveringene i en liste, hvor hvert element er en ordbok med
med brukernavnet og den respektive scoren
[
    'innlevering1': {
        'brukernavn1': poengscore,
        'brukernavn1': poengscore,
    },
    ...
    'innlevering3': {
        ...
        'brukernavn70': poengscore,
        'brukernavn71': poengscore,
    },
    ...
]
Om dette er den faktiske beste måten å strukturere det på er vel mer om datastruktur og sånt,
men i første omgang ville jeg ha startet den sånn.

c)
Her ville jeg brukt en liste, og forskjellen her i forhold til oppgave a) er at
du kan vinne flere ganger, og dermed kan navnet duplikeres mener jeg. Er du heldig vinner du
100 millioner to ganger ila et år :). 

d)
Her ville jeg ha brukt en mengde. Dette er igjen for å unngå duplikater, og det er raskere å sjekke opp.
"""
