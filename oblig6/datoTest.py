from dato import Dato


def hovedprogram():
    dato = Dato(15, 10, 2021)
    print(dato.hentAar())
    print(dato.sjekkDato())
    datoFormat = dato.printDato()
    print(datoFormat)
    # 3g
    dato.lesInnDato()


hovedprogram()
