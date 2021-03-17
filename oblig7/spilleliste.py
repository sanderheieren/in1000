from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        fil = open(filnavn)

        for linje in fil:
            print(linje)


spilleliste = Spilleliste('topp 40')
spilleliste.lesFraFil('musikk.txt')
