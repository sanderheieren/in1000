# Sander Heieren, Oblig 1, IN1000

# Programmet skal lagre variabler og gjøre beslutninger basert på if-tester
# Her skal vi spørre brukeren om to variabler og også finne differansen mellom heltallsverdiene
# samt spørre brukeren om navnet deres

# 1,2,3 Får navn av bruker, og printer ut resultatet
navn = input('Oppgi ditt navn:\n')
print(f"Hei {navn}")

# 4, deklarerer to helltallsverdier som variabler og printer ut på egne liner
print("\nOppgave 4 & 5:")
a = 3
b = 10
print(f"variabel a: {a}\nvariabel b: {b}")

# 5, beregner differansen av de to variablene (a og b) og lagrer i en ny variabel
differanse = a - b
print(f"Differanse: {differanse}")

# 6, ber brukeren oppgi et nytt navn og sammenkobler det gamle med det nye i en ny variabel
print("\nOppgave 6:")
nyttNavn = input('Oppgi et nytt navn:\n')
sammen = navn + nyttNavn
print(f"Det gamle og nye navnet sammen er:\n'{sammen}'")

# 7, legger til ordet 'og' mellom de to navnene som er gitt, og endrer verdien av sammen-variablen
# det er ulike måter og oppnå dette på, men synes denne virker mest effektiv og oversiktelig
print("\nOppgave 7:")
sammen = f"{navn} og {nyttNavn}"
print(f"Etter endring er den nye teksten:\n'{sammen}'")
