# Dette programmet skal lage ulike regnefunksjoner, og skal ta hensyn til skop og skal skrive ut resultatet
# det skal også bruke assert for å sørge for at riktig input blir gitt av bruker

# 1 addisjonfunksjon med to paramtere

def addisjon(num1, num2):
    return num1 + num2

# 2, to nye funksjoner og bruker assert for å teste


def subtraksjon(num1, num2):
    return num2 - num1


def divisjon(num1, num2):
    if num2 == 0:
        return "Kan ikke dele på 0"
    return num1 / num2


assert addisjon(1, 2) == 3
assert addisjon(-4, -5) == -9
assert addisjon(-4, 9) == 5

assert subtraksjon(1, 2) == 1
assert subtraksjon(-4, -5) == -1
assert subtraksjon(-4, 9) == 13

assert divisjon(1, 2) == 0.5
assert divisjon(-4, -5) == 4/5
assert divisjon(-4, 9) == -4/9

# 3 ny funksjon, og nye assert tester


def tommer_til_cm(antall_tommer):
    assert antall_tommer > 0, 'Tommer må være større enn 0'
    return antall_tommer * 2.54


assert tommer_til_cm(1) == 2.54
assert tommer_til_cm(2) == 5.08

# 4 ny funksjon, input fra bruker, bruke funksjonene lagd tidligere for å besvare brukerinput


def skriv_beregninger():
    print("Utregninger:")
    num1 = float(input("Skriv inn tall 1: "))
    num2 = float(input("Skriv inn tall 2: "))
    sum = addisjon(num1, num2)
    sub = subtraksjon(num1, num2)
    div = divisjon(num1, num2)
    res = "Resultat av"
    regneResultat = f"\n{res} summering: {sum}\n{res} subtraksjon: {sub}\n{res} divisjon: {div}"
    print(regneResultat)
    print("\nKonvertering fra tommer til cm:")
    tommer = float(input("Skriv inn et tall: "))
    tommerResultat = f"Resultat tommer til cm: {tommer_til_cm(tommer)}"
    print(tommerResultat)
    return regneResultat + "\n" + tommerResultat
# returenerer stringen for å teste i assert, men fant ikke helt ut hvordan jeg skulle gjøre det.. men jeg bare lot det stå


assert skriv_beregninger()
