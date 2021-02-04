# Dette programmet skal inneholde en liste som har styring på tall jeg velger selv
# samt input fra brukeren. Med disse tallene skal jeg gjøre litt manipulasjon for å
# vise jeg behersker det nye teamet om "Lister"

# 1 lager liste med tre vilkårlige tall
listeHeltall = [4, 2, 8]
# Legger til et tall på slutten av listen med metoden "append"
listeHeltall.append(10)
# Printer ut resultatet (vet ikke hvorfor den formaterer seg på ny linje i printen)
print(
    f"Første element i listen er: {listeHeltall[0]}.\nTredje element i lista er: {listeHeltall[2]}.")

# 2 Lager en ny, tom liste, og vil bruker skal oppgi 4 navn
navnListe = []

# Lager prosedyre fordi det er lik logik som blir gjentatt fire ganger
# Sørger for at ingen navn har stor bokstav, gjør det enklere i if-setningen
# Printer ut slik at bruker vet at navnet er lagt til


def leggTilIListe():
    navn = input("Legg til et navn:\n")
    navnListe.append(navn.lower())
    print(f"{navn} ble lagt til i listen")


for x in range(4):
    leggTilIListe()

# 3 Sjekker om brukeren har lagt til mitt navn i lista.
if "sander" in navnListe:
    print("Du husket meg!")
else:
    print('Glemte du meg?')

# 4, lager en ny liste bestående av summen av tallene i første liste samt
# hva det er multiplisert
# NB, det er inneforstått at jeg kan aksesere hver index plass og gjøre det manuelt
# men synes det gir mer mening å loope over og legge til på denne måten

sumOgMultipliser = []
sum = 0
multipliser = 1
for x in listeHeltall:
    sum = sum + x
    multipliser = multipliser * x

sumOgMultipliser.append(sum)
sumOgMultipliser.append(multipliser)

# Legger sammen gammel og ny liste og printer

opprinneligOgsumProd = listeHeltall + sumOgMultipliser
print(f"Den nye listen er: {opprinneligOgsumProd}")

# Lager funksjon for å fjerne siste element i liste


def fjernSisteElement(liste):
    liste.pop(len(liste) - 1)


# Kaller på funksjonen to ganger for å fjerne de to siste elementene
fjernSisteElement(opprinneligOgsumProd)
fjernSisteElement(opprinneligOgsumProd)
print(f"Oppdatert liste er: {opprinneligOgsumProd}")
