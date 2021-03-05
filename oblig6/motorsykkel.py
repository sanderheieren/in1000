# Progam som skal modellere kjøring av en motorsykkel

# 1, 2, 3, 4. Skriver klassen med konstruktør og deklarerer de gitte attributene
# og metodene som trengs for å modellere kjøring av en motorsykkel

class Motorsykkel:
    def __init__(self, merke, regNr, kmStand):
        self._merke = merke
        self._regNr = regNr
        self._kmStand = kmStand

    def kjor(self, km):
        self._kmStand += km

    def hentKilometerstand(self):
        return self._kmStand

    def skrivUt(self):
        infoOmBil = f"Merke: {self._merke}\nRegistreringsnummer: {self._regNr}\nKilometerstand: {self._kmStand}\n"
        print(infoOmBil)
