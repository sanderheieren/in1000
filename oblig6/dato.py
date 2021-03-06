# Program om datoer

# 1, 2, 3
class Dato:
    def __init__(self, nyDag, nyMaanded, nyttAar):
        self._nyDag = nyDag
        self._nyMaanded = nyMaanded
        self._nyttAar = nyttAar

    def hentAar(self):
        return self._nyttAar

    def printDato(self):
        return f"{self._nyDag}/{self._nyMaanded}/{self._nyttAar}"

    def sjekkDato(self):
        if self._nyDag == 15:
            return "Loenningsdag!"
        elif self._nyDag == 1:
            return "Ny maaned, nye muligheter"
        else:
            return "Stå på"

# 2d
    def lesInnDato(self):
        nyDato = input("Oppgi ny dato (DD/MM/YYYY):\n>>>")
        datoListe = nyDato.split("/")
        dag = int(datoListe[0])
        mnd = int(datoListe[1])
        aar = int(datoListe[2])
        if(aar < self._nyttAar):
            print("Den nye oppgitte datoen kommer før dato-objektet")
            return
        if(aar > self._nyttAar):
            print("Den nye oppgitte datoen kommer etter dato-objektet")
            return
        if aar == self._nyttAar:
            if mnd < self._nyMaanded or (mnd == self._nyMaanded and dag < self._nyDag):
                print("Den nye oppgitte datoen kommer før dato-objektet")
            elif mnd == self._nyMaanded and dag == self._nyDag:
                print('Lik dato')
            else:
                print("Den nye oppgitte datoen kommer etter dato-objektet")
