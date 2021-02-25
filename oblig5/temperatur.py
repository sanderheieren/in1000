# 2 lese data fra fil, om temperatur

# 1 leser inn fra fil, lager ordbok og returnerer
def les_inn_temperatur(filnavn):
    fil = open(filnavn)
    temperatur = {}
    for linje in fil:
        liste = linje.split(",")
        mnd = liste[0]
        temp = float(liste[1])
        temperatur[mnd] = temp
    return temperatur


# print(les_inn_temperatur("max_temperatures_per_month.txt"))

# 2 skal finne varmeste dagen i hver mnd og oppdatere ordbok underveis


def finn_varmerekord(varmesteTempPerMnd, filMedDagligeTemp):
    fil = open(filMedDagligeTemp)
    oppdatertVarmesteTempPerMnd = varmesteTempPerMnd.copy()
    for linje in fil:
        liste = linje.split(",")
        mnd = liste[0]
        dato = liste[1]
        temp = float(liste[2])
        if (temp > varmesteTempPerMnd[mnd]):
            oppdatertVarmesteTempPerMnd[mnd] = temp
            print(
                f'Ny varmerekord på {dato} {mnd}: {temp} grader Celisus. Gammel varmerekord var {varmesteTempPerMnd[mnd]} grader Celsius.')

    return oppdatertVarmesteTempPerMnd


varmeRekordForHverMnd = les_inn_temperatur("max_temperatures_per_month.txt")
listeMedVarmesteTemp = finn_varmerekord(
    varmeRekordForHverMnd, "max_daily_temperature_2018.txt")
print(listeMedVarmesteTemp)
