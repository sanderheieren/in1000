# Dette er et beregningsprogram for skreddere, skal lese fra fil for å lage
# et konverteringsprogram for en skredder.


# funksjon som leser fra fil og legger i ordbok. går over hver vil og oppretter nøkkel og verdi for
# ordboken. bruker tidligere funksjon for å konvertere tommer til cm


def leggTilBeregninger(filNavn):
    innfil = open(filNavn)
    infoOmMål = {}
    for linje in innfil:
        målOmråde = linje.split()[0]
        målTommer = tommer_til_cm(float(linje.split()[1]))
        infoOmMål[målOmråde] = målTommer
    innfil.close()
    return infoOmMål


def tommer_til_cm(antall_tommer):
    assert antall_tommer > 0, 'Tommer må være større enn 0'
    return antall_tommer * 2.54


for mål, cm in leggTilBeregninger("egenoppgave.txt").items():
    print(mål, cm, "cm")
