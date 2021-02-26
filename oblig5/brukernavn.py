# Program for å legge til nye UiO brukernavn i en samling og gi
# dem e-post.

# 1, lager tom liste

uioBrukere = {}

# 2, lager funksjon som tar inn string og skal returnere et uio-brukernavn


def lag_brukernavn(fulltNavn):
    fornavn = fulltNavn.split()[0].lower()
    forsteBokstavAvEtternavn = fulltNavn.split()[1][0:1].lower()
    return fornavn + forsteBokstavAvEtternavn

# 3, funksjon som lager epost for respektiv bruker


def lag_epost(brukernavn, suffix):
    return f"{brukernavn}@{suffix}"

# 4, skrive noe


def print_eposter(ordbok):
    for brukernavn in ordbok:
        epost = lag_epost(brukernavn, ordbok[brukernavn])
        print(f"{brukernavn} har epost: {epost}")


brukernavn = lag_brukernavn("sander heieren")
epost = lag_epost(brukernavn, "student.matnat.uio.no")
print_eposter({"olan": "ifi.uio.no", "karian": "student.matnat.uio.no"})

brukerInput = input(
    "(i) for legge til epost\n(p) printe eposter\n(s) avslutte\n>>> ")
while brukerInput != "s":
    if(brukerInput == "i"):
        navn = input("Skriv inn fullt navn (fornavn etternavn):\n")
        suffix = input("Skriv inn suffix for epost:\n")
        brukernavn = lag_brukernavn(navn)
        uioBrukere[brukernavn] = suffix
    elif(brukerInput == "p"):
        print_eposter(uioBrukere)
    brukerInput = input("\n(i)\n(p)\n(s)\n>>> ")

print("Takk for denne gang")
