# 4 quiz spørsmål om teknologier som brukes ofte i web browseren
riktige_svar = 0
antall_spm = 0


def sporsmaal(spm):
    global antall_spm
    antall_spm += 1
    print('_______________')
    print(spm)
    return input()


def riktig():
    print('Bra, det var riktig!')


def feil():
    print('Det var dessverre ikke riktig.')


print('Velkommen til Web Quiz 101')

if sporsmaal('Hvilket programmeringspråk kjører i web browseren?').lower() == "javascript":
    riktige_svar += 1
    riktig()
else:
    feil()

if sporsmaal('Hva står det kjente styling-programmet "CSS" for?').lower() == "cascading style sheets":
    riktige_svar += 1
    riktig()
else:
    feil()

if sporsmaal('Hva står HTML for?').lower() == "hypertext markup language":
    riktige_svar += 1
    riktig()
else:
    feil()

if sporsmaal('I hvilket år ble JavaScript lansert?') == "1996":
    riktige_svar += 1
    riktig()
else:
    feil()

print('______________________')
print(f"Du klarte å oppnå {riktige_svar} / {antall_spm} poeng!")
if riktige_svar == 0:
    print("Øvelse gjør mester")
elif riktige_svar == 4:
    print("Alt riktig!")
elif riktige_svar >= 2:
    print("Dette var ok, men du kan bedre")
else:
    print('Bedre enn gjennomsnittet')
