from sang import Sang
from spilleliste import Spilleliste


def hovedprogram():
    adagio = Sang('Albinoni', 'Adagio', 'adagio.wav')
    ode_to_joy = Sang('Beethoven', 'Ode to joy', 'ode_to_joy.wav')
    spilleliste = Spilleliste('Min favorittmusikk')
    spilleliste.leggTilSang(adagio)
    spilleliste.leggTilSang(ode_to_joy)
    spilleliste.spillAlle()


hovedprogram()
