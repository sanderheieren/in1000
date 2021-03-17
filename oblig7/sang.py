# Dette programmet skal definere klassen 'Sang' og by på metoder i grensesnittet slik
# at det kan spilles sang, finne artister, titler osv.

# 1 Klassedefinsjon av Sang
class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

# 2 metode som spiller av sangen
    def spill(self):
        print(f'Spiller {self._tittel} av {self._artist}')

# 3 metode som sjekker artist
    def sjekkArtist(self, navn):
        navnDeler = navn.lower().split()
        for navner in navnDeler:
            if len(navner) > 1 and navner in self._artist.lower():
                return True
        return False

    def sjekkTittel(self, tittel):
        return self._tittel.lower() == tittel.lower()

    def sjekkArtistOgTittel(self, artist, tittel):
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)

    def __str__(self):
        return f"{self._tittel} av {self._artist}"
