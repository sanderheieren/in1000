# Dette programmet spør brukeren om de har lyst på en brus eller ei, og ved dette skal
# skal gjøres ved hjelp av if-sjekker

# 1, spør bruker om de kan tenke seg en brus, for å unngå case-sensitivity tar jeg alt til små bokstaver
# fordi det er mulig brukeren skriver "JA, Ja, etc.."
svar = input("Kunne du tenke deg en brus? (ja/nei)\n").lower()

# 2 basert på svaret ovenfor printer jeg ut ulike svar som spesifisert i oppgaven
if svar == "ja":
    print("Her har du en brus!")
elif svar == "nei":
    print("Den er grei,")
else:
    print("Det forstod jeg ikke helt.")
