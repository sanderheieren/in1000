# Self referer til instansen av klassen/objektet
class Teller:
    def __init__(self):
        self._teller = 0

    def økTeller(self):
        self._teller += 1
    
    def hentTeller(self):
        return self._teller

# instans av Teller-objekt
teller1 = Teller()
teller1.økTeller()
teller1.økTeller()
# teller1 sin teller vil nå være 2
print(teller1.hentTeller())

# ny instans av Teller-objekt
teller2 = Teller()
# teller2 sin teller vil være 0
print(teller2.hentTeller())
# så teller2 vil ikke påvirke telleren til teller1, fordi 'self' referer bare de spesfikke instansene

