from spillebrett import Spillebrett

def main():
    print('HEI!\nVelkommen til "Game of life"')
    rad = int(input('Oppgi antall rader:\n>>> '))
    kolonne = int(input('Oppgi antall kolonner:\n>>> '))
    brett = Spillebrett(rad, kolonne)
    brett.tegnBrett()
    print(f'Generajon: {brett.hentGenerajsonsNummer()} - Antall levende celler: {brett.finnAntallLevende()}')
    kommando = input('Press enter for å fortsette. Press q og trykk enter for å avslutte\n>>> ')
    while kommando != 'q':
        brett.oppdatering()
        brett.tegnBrett()
        print(f'Generajon: {brett.hentGenerajsonsNummer()} - Antall levende celler: {brett.finnAntallLevende()}')
        kommando = input('Press enter for å se neste generasjon. Press q og trykk enter for å avslutte\n>>> ')

main()