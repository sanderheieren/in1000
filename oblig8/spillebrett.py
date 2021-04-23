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

    # Printer ut det generete brettet i terminalen
    def tegnBrett(self):
        # for _ in range(10):
        #     print()
        print("=================")
        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self._rutenett[i][j].hentStatusTegn(), end="")
            print()
        
    # Setter et tilfedig bord, 1/3 sjanse for at det er levende celle
    def _generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                tall = random.randint(0,2)
                if tall == 0:
                    self._rutenett[i][j].settLevende()

    # For hver generasjon, oppdateres brettet og er klar for å bli simulert for neste 'enter'-klikk
    def oppdatering(self):
        dødeCellerSomBlirLevende = []
        levendeCellerSomDør = []
        self._generasjonsnummer += 1

        for i in range(self._rader):
            for j in range(self._kolonner):
                cellen = self._rutenett[i][j]
                antallLevendeNaboer = 0
                naboListe = self.finnNabo(i,j)
                for nabo in naboListe:
                    if nabo.erLevende():
                        antallLevendeNaboer += 1
                
                if cellen.erLevende():
                    if antallLevendeNaboer < 2 or antallLevendeNaboer > 3:
                        levendeCellerSomDør.append(cellen)
                else:
                    if antallLevendeNaboer == 2 or antallLevendeNaboer == 3:
                        dødeCellerSomBlirLevende.append(cellen)
                
        for celle in dødeCellerSomBlirLevende:
            celle.settLevende()
        for celle in levendeCellerSomDør:
            celle.settDoed()
    
    def hentGenerajsonsNummer(self):
        return self._generasjonsnummer

    def finnNabo(self, rad, kolonne):
        naboCeller = []

        for i in range(-1,2):
            for j in range(-1,2):
                naboRad = rad + i
                naboSete = kolonne + j

                gyldig = True

                if i == 0 and j == 0:
                    gyldig = False

                if naboRad < 0 or naboRad >= self._rader:
                    gyldig = False

                if naboSete < 0 or naboSete >= self._kolonner:
                    gyldig = False
                
                if gyldig:
                    naboCeller.append(self._rutenett[naboRad][naboSete])

        return naboCeller
       
    
    def finnAntallLevende(self):
        antallLevende = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                    antallLevende += 1
        return antallLevende