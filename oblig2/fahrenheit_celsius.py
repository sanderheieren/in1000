# Dette programmet skal konvertere temperatur gitt av brukeren fra den amerikanske
# målenheten fahrenheit til den mer anvendelige målenheten, celius, som brukes verden over.

# 1 Skal definere en variabel og gi en verdi til denne variablen (i fahrenheit)
fahrenheitTemp = 101

# 2 Printer ut temperaturen i fahrenheit
print(fahrenheitTemp)

# 3 Ny variabel, denne skal variablen skal ta vare på denne samme temperaturen, bare i celius
celiusTemp = (fahrenheitTemp - 32) * (5 / 9)

# 4 Printer ut samme temperatur, men nå med celius som målenhet
print(celiusTemp)

# 5 Samme type logikk, bare at nå får jeg input fra bruker, viktig å sørge for at variabelen får
# riktig datatype, fordi alt fra input er egentlig en string
fahrenheitTemp = float(input('Oppgi temperatur i fahrenheit: '))
print((fahrenheitTemp - 32) * (5 / 9))
