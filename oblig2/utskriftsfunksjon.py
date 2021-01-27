# Sander Heieren, Oblig 2, IN1000

# Dette programmet skal ta inn navn og bosted fra terminalen (brukeren)
# Vi skal også brukte prosedyrer for å bli bedre kjent med kodeflyt, her er det bare om utskrifter

# 1, 2 får navn og bosted og legger all logikk inn i en egen prosedyre. Denne skal kalles 3 ganger.
def navnOgBosted():
    navn = input('Skriv inn navn: ')
    bosted = input('Hvor kommer du fra? ')
    print(f'Hei {navn}! Du er fra {bosted}.')


# Kaller på prosedyren 3 ganger
for x in range(3):
    navnOgBosted()
