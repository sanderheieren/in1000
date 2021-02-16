# Lager program som spør brukerer om tall, når de taster inn 0 slutter jeg å spørre
# Skal legge inn i liste, og skrive ut alle, senere skal tallene summeres

# 1, 2, 3 Får inn tall, lagrer, og skriver ut

listeMedTall = []


def spørBrukerOmTall():
    tall = int(input('Skriv inn et vilkårlig tall (0 for å avslutte):\n'))
    while(int(tall) != 0):
        listeMedTall.append(tall)
        tall = int(input('Nytt tall (0 for å avslutte):\n'))
    print("\nTallene i listen er: ")
    for number in range(len(listeMedTall)):
        print(f"{number + 1}: {listeMedTall[number]}")


spørBrukerOmTall()

# Lager ny variabel, som skal holde den summerte verdien til alle tallene

minSum = 0

for number in range(len(listeMedTall)):
    minSum = minSum + listeMedTall[number]

print(f"\nsummen av alle tallene i listen er: {minSum}\n")

minsteTall = float('inf')
størsteTall = float('-inf')
print(størsteTall < 50)
for x in range(len(listeMedTall)):
    if listeMedTall[x] < minsteTall:
        minsteTall = listeMedTall[x]

for x in range(len(listeMedTall)):
    if listeMedTall[x] > størsteTall:
        størsteTall = listeMedTall[x]

print(f'Det minste tallet i listen er: {minsteTall}')
print(f'Det største tallet i listen er: {størsteTall}')
