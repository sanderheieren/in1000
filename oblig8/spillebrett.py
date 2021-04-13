import random
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0

        self._rutenett = []

        for i in range(self._rader):
            celler = []
            for j in range(self._kolonner):
                celler.append(Celle())
            self._rutenett.append(celler)
        
        self._generer()

    def tegnBrett(self):
        for _ in range(10):
            print()

        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self._rutenett[i][j].hentStatusTegn(), end="")
            print()
        
    
    def _generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                tall = random.randint(0,100)
                if tall <= 33:
                    self._rutenett[i][j].settLevende()


    def oppdatering(self):
        pass

    def finnNabo(self, rad, kolonne):
        naboCeller = []
        # nabotopper for cellen
        if rad != 0:
            naboCeller.append(self._rutenett[rad - 1][kolonne])
            try:
                naboCeller.append(self._rutenett[rad - 1][kolonne + 1])
            except IndexError:
                pass
            if kolonne != 0:
                naboCeller.append(self._rutenett[rad - 1][kolonne - 1])

        # venstrenaboer for cellen
        if kolonne != 0:
            naboCeller.append(self._rutenett[rad][kolonne - 1])
            try:
                naboCeller.append(self._rutenett[rad + 1][kolonne - 1])
            except IndexError:
                pass

        # resterende naboer for cellen
        try:
            naboCeller.append(self._rutenett[rad + 1][kolonne + 1])
        except IndexError:
            pass
        try:
            naboCeller.append(self._rutenett[rad + 1][kolonne])
        except IndexError:
            pass
        try:
            naboCeller.append(self._rutenett[rad][kolonne + 1])
        except IndexError:
            pass

        return naboCeller
       

    def finnAntallLevende(self):
        pass