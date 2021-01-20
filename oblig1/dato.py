# Programmet skal stille bruker om to ulike datoer og sjekke om datoene kommer kronologisk

# 1, skal lese inn to ulike datoer fra bruker, heltall for dag og måned
dato = input('Skriv inn en dato: (DD/MM)\n')
forsteDag = int(dato.split('/')[0])
forsteMnd = int(dato.split('/')[1])
nyDato = input('Skriv inn en ny dato: (DD/MM)\n')
andreDag = int(nyDato.split('/')[0])
andreMnd = int(nyDato.split('/')[1])

if (forsteMnd < andreMnd or (forsteMnd == andreMnd and forsteDag < andreDag)):
    print('Riktig rekkefølge!')
elif (forsteMnd == andreMnd and forsteDag == andreDag):
    print('Samme dato!')
else:
    print('Feil rekkefølge!')
