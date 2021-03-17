from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        fil = open(filnavn)

        for linje in fil:
            data = linje.strip().split(';')
            artist = data[0]
            tittel = data[1]
            sang = Sang(artist, tittel)
            self._sanger.append(sang)
        fil.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)
            return True
        return False

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        sanger = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                sanger.append(sang)
        return sanger


# spilleliste = Spilleliste('topp 40')
# spilleliste.lesFraFil('musikk.txt')
