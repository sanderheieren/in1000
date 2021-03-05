from hund import Hund


def hovedprogram():
    hund = Hund(10, 30)
    hund.spring()
    print(hund.hentVekt())
    hund.spis(4)
    print(hund.hentVekt())
    hund.spring()
    print(hund.hentVekt())
    hund.spis(15)
    print(hund.hentVekt())


hovedprogram()
