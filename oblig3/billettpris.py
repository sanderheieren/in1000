# Dette programmet skal beregne prisen på billetten avhengig av kjøperens alder

# 1,2 Lager prosedyre som spør bruker om alder, denne logikken vil bli brukt for
# å finne ut hvor mye de må betale for billeten

def prisForKjoper():
    alder = int(input('Hva er alder på kjøperen? '))
    billettPris = 0
    if alder < 0 or alder > 150:
        print('Skriv inn gyldig alder')
        prisForKjoper()
        return
    if alder <= 17:
        billettPris = 30
    elif alder < 63:
        billettPris = 50
    else:
        billettPris = 35
    print(f"Prisen på billetten for en som er {alder} år er: {billettPris}kr.")


for x in range(3):
    prisForKjoper()

# Det er kanskje en feil ved den om jeg ikke sjekker for riktig input på alderen, men det gjør jeg jo så
# vet ikke hva oppgaven referer til med dette spørsmålet (det ble ikke presisert at man skulle sjekke for dette
# , men jeg synes det er hensiktmessig å ta med denne logikken i prosedyren uansett som standar).

# En annen feil som jeg ser, er hvordan rekkefølgen a, b og c blir definert i oppgaven
# om man følger den logikken, vil en som er 63 eller over få prisen til en som er over 17
# slik at man aldri kommer ned til prisen for en pensjonist. Men det er vel kanskje
# dette dere er på utkikk etter.
