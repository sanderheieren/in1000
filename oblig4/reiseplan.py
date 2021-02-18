# Dette programmet skal lage en reiseplan ved hjelp av en nøstet liste,
# Vi lager en reiseplan fordi vi ikke kan reise noe nå, men når vi endelig kan igjen
# er vi forbredte med en solid reisplanlegger. Kjør!

# 1,2 legger inn reisemål, kler og dato fra bruker og legger i liste
steder = []
print('Hei og velkommen til Reiseplanlegger 2021\nDu skal legge inn dine 5 ønskede reisemål')
for x in range(5):
    reiseDestinasjon = input(f'Sted nr {x + 1}: ')
    steder.append(reiseDestinasjon)
print('\nFantastisk. Du har noen gode valg.\nNå skal vi legge inn klesplagg, og avreisedato.\n')
print('Vi begynner med klesplaggene.\n')

klesplagg = []
for x in range(5):
    kleder = input(f'Klesplagg nr {x + 1}: ')
    klesplagg.append(kleder)

avreiseDatoer = []
print('Du har god stil!\n\nNå skal vi legge til avreisedatoer (vinter, vår, sommer, høst)\n')
for x in range(5):
    dato = input(f'Avreisedato {x + 1}: ')
    avreiseDatoer.append(dato)

# 3, 4 Reisplan, som inkluderer info oppgitt tidligere. Skriver ut info

reiseplan = [steder, klesplagg, avreiseDatoer]

print('\nHer kommer all info om dine reiseplaner:\n')
for reise in reiseplan:
    print(reise)

print("\nHerlig. Nå skal vi generere noen reisemål for deg!\n")
# 5 (a, b, c) Skal få indeksplass av bruker, og skrive ut respektive plassen

i1 = int(input(f"Angi et tall mellom 1 og {len(reiseplan)}:\n")) - 1
if(i1 < 0 or i1 >= len(reiseplan)):
    print('Ugyldig input. Ingen reise på deg..')
    exit()

i2 = int(input(f"Angi et tall mellom 1 og {len(reiseplan[i1])}:\n")) - 1

if(i2 < 0 or i2 >= len(reiseplan[i1])):
    print('Ugyldig input. Ingen reise på deg..')
    exit()

print(f'\nDu skal på tur!! Husk dette: {reiseplan[i1][i2]}')
