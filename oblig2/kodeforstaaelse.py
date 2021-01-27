# Teorispørsmål:

# 1:
# Nei, dette er ikke lovlig kode. Enkelt og greit fordi det ikke er mulig å legge sammen
# en string og en tallverdi. Det er to ulike datatyper, og vi vil få en feilmelding.
# Koden er forøvrig 'lovlig' frem til print-setningen.

# 2:
# Vi får en feilmelding på linje 4, gitt at heltallet, b, er mindre enn 10. Ellers vil den
# aldri komme til print-setningen, og koden vil forsette som normalt.

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
