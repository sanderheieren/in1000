# Programmet skal stille bruker om to ulike datoer og sjekke om datoene kommer kronologisk

# 1, skal lese inn to ulike datoer fra bruker, heltall for dag og måned
print('Skriv inn en dato, først dag(DD), så mnd(MM)')
forsteDag = int(input("Dag(DD): "))
forsteMnd = int(input("Mnd(MM): "))

print('Skriv inn en ny dato, igjen, først dag(DD), så mnd(MM)')
andreDag = int(input("Dag(DD): "))
andreMnd = int(input("Mnd(MM): "))

if (forsteMnd < andreMnd or (forsteMnd == andreMnd and forsteDag < andreDag)):
    print('Riktig rekkefølge!')
elif (forsteMnd == andreMnd and forsteDag == andreDag):
    print('Samme dato!')
else:
    print('Feil rekkefølge!')
