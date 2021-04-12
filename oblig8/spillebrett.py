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

    def finnNabo(self, x, y):
        nabo = []
        if x != 0:
            nabo.append(self._rutenett[y][x-1])
            try:
                nabo.append(self._rutenett[y+1][x-1])
            except IndexError:
                pass
            if y != 0:
                nabo.append(self._rutenett[y-1][x-1])

        if y != 0:
            try:
                nabo.append(self._rutenett[y-1][x+1])
            except IndexError:
                pass
            nabo.append(self._rutenett[y-1][x])

        try:
            nabo.append(self._rutenett[y][x+1])
        except IndexError:
            pass
        try:
            nabo.append(self._rutenett[y+1][x+1])
        except IndexError:
            pass
        try:
            nabo.append(self._rutenett[y+1][x])
        except IndexError:
            pass

        for naboen in nabo:
            print(naboen)

        return nabo

        # trenger jeg denne?celle = self._rutenett[rad-1][kolonne-1]
        # naboCeller = []
        # if rad == 0:
        #     if kolonne == 0:
        #         naboCeller.extend([self._rutenett[rad + 1][kolonne], self._rutenett[rad][kolonne + 1], self._rutenett[rad + 1][kolonne + 1]])
        #     elif kolonne == self._kolonner - 1:
        #         naboCeller.extend([self._rutenett[rad + 1][kolonne], self._rutenett[rad][kolonne - 1], self._rutenett[rad + 1][kolonne - 1]])
        #     else:
        #         naboCeller.extend([self._rutenett[rad + 1][kolonne], self._rutenett[rad][kolonne + 1], self._rutenett[rad + 1][kolonne + 1], self._rutenett[rad][kolonne - 1], self._rutenett[rad + 1][kolonne - 1]])
        #   #  return

        # if rad == self._rader - 1:
        #     if kolonne == 0:
        #         naboCeller.extend([self._rutenett[rad - 1][kolonne], self._rutenett[rad][kolonne + 1], self._rutenett[rad + 1][kolonne + 1]])
        #     elif kolonne == self._kolonner - 1:
        #         naboCeller.extend([self._rutenett[rad - 1][kolonne], self._rutenett[rad][kolonne - 1], self._rutenett[rad - 1][kolonne - 1]])
        #     else:
        #         naboCeller.extend([self._rutenett[rad][kolonne - 1], self._rutenett[rad][kolonne + 1], self._rutenett[rad - 1][kolonne], self._rutenett[rad - 1][kolonne - 1], self._rutenett[rad - 1][kolonne + 1]])
        #   #  return

        # if kolonne == 0:
        #         naboCeller.extend([self._rutenett[rad][kolonne + 1], self._rutenett[rad + 1][kolonne], self._rutenett[rad - 1][kolonne], self._rutenett[rad + 1][kolonne + 1], self._rutenett[rad - 1][kolonne + 1]])
        #         # return
        # elif kolonne == self._kolonner - 1:
        #         naboCeller.extend([self._rutenett[rad][kolonne - 1], self._rutenett[rad + 1][kolonne], self._rutenett[rad - 1][kolonne], self._rutenett[rad - 1][kolonne - 1], self._rutenett[rad + 1][kolonne - 1]])
        #         # return

        # if len(naboCeller) == 0:
        #         naboCeller.extend([self._rutenett[rad - 1][kolonne - 1], self._rutenett[rad - 1][kolonne], self._rutenett[rad - 1][kolonne + 1], self._rutenett[rad][kolonne - 1], self._rutenett[rad][kolonne + 1], self._rutenett[rad + 1][kolonne - 1], self._rutenett[rad + 1][kolonne + 1], self._rutenett[rad + 1][kolonne]])
            


            




    
    def finnAntallLevende(self):
        pass