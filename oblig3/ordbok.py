# Dette programmet skal lage en ordbok som inneholder ulike varer i en butikk
# samt den respektive prisen. Varenavnet er nøkklen, mens prisen er innholdet
# i form av float (flyttall)

# 1, Definerer(?)/Lager en ordbok som inneholder ulike varer + prisen deres.

varer = {
    "melk": 14.90,
    "yoghurt": 12.90,
    "pizza": 39.90
}

# Printer ut inneholdet
print(f"Inneholdet i varene er:\n{varer}")

# 2, Definerer prosedyre for å legge til varer i 'varer'-ordbok


def leggTilVareNavn():
    vareNavn = input('Skriv inn navnet på varen: ')
    varePris = float(input(f'Hvor mye koster {vareNavn}? '))
    print()
    varer[vareNavn] = varePris


leggTilVareNavn()
leggTilVareNavn()

# Printer ut resultat etter input fra bruker
print(varer)
