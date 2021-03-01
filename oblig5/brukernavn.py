# Program for å legge til nye UiO brukernavn i en samling og gi
# dem e-post.

# 1, lager tom liste

uioBrukere = {}

# 2, lager funksjon som tar inn string og skal returnere et uio-brukernavn

# 7, prøver meg på å lage unike brukernavn -- den funker, men vet ikke hvor 'pen' den er


def lag_brukernavn(ordbokMedUiOBrukere, fulltNavn):
    fornavn = fulltNavn.split()[0].lower()
    bokstavAvEtternavn = fulltNavn.split()[1][0:1].lower()
    brukernavn = fornavn + bokstavAvEtternavn
    bokstaver = bokstavAvEtternavn
    if brukernavn in ordbokMedUiOBrukere:
        n = 1
        n1 = n + 1
        bokstaver += fulltNavn.split()[1][n:n1]
        brukernavn = fornavn + bokstaver
        for uiobrukere in ordbokMedUiOBrukere:
            if brukernavn not in ordbokMedUiOBrukere:
                break
            else:
                n += 1
                n1 += 1
                brukernavn = brukernavn + fulltNavn.split()[1][n:n1]

    return brukernavn

# 3, funksjon som lager epost for respektiv bruker


def lag_epost(brukernavn, suffix):
    return f"{brukernavn}@{suffix}"


# 4, prosedyre som printer epost til spesifikk uio-bruker

def print_eposter(ordbok):
    for brukernavn in ordbok:
        epost = lag_epost(brukernavn, ordbok[brukernavn])
        print(f"{brukernavn} har epost: {epost}")


brukernavn = lag_brukernavn(uioBrukere, "sander heieren")
epost = lag_epost(brukernavn, "student.matnat.uio.no")
print_eposter({"olan": "ifi.uio.no", "karian": "student.matnat.uio.no"})

brukerInput = input(
    "(i) for legge til epost\n(p) printe eposter\n(s) avslutte\n>>> ")

# 5, løkke som går til bruker vil avlsutte, kan legge til og vise eposter
while brukerInput != "s":
    if(brukerInput == "i"):
        navn = input("Skriv inn fullt navn (fornavn etternavn):\n")
        suffix = input("Skriv inn suffix for epost:\n")
        brukernavn = lag_brukernavn(uioBrukere, navn)
        uioBrukere[brukernavn] = suffix
    elif(brukerInput == "p"):
        print_eposter(uioBrukere)
    brukerInput = input("\n(i)\n(p)\n(s)\n>>> ")

print("Takk for denne gang")
