# Dette skal programmet skal telle antall ord, og forekomster av ord basert på tekstinput
# fra bruker

# 1, funksjon som returerer antall bokstaver i et ord

def antallBokstaverIOrd(ord):
    if len(ord) == 0:
        print('Angi minst 1 bokstav')

    total = 0
    for x in range(len(ord)):
        total = total + 1
    return total


def unikeOrdISetning(setning):
    ord = setning.split()
    unikeOrd = {}
    for x in range(len(ord)):
        if ord[x] in unikeOrd:
            unikeOrd[ord[x]] += 1
        else:
            unikeOrd[ord[x]] = 1

    return unikeOrd


setningFraBruker = input('>>>Skriv en setning:\n>>>')
unikeOrd = unikeOrdISetning(setningFraBruker)
antallOrd = 0
for x in unikeOrd:
    antallOrd += unikeOrd[x]
print(f'>>>Det er {antallOrd} ord i setningen din.')
for x in unikeOrd:
    antallGanger = unikeOrd[x]
    print(
        f">>>Ordet '{x}' forekommer {antallGanger} ganger, og har {antallBokstaverIOrd(x)} bokstaver")
