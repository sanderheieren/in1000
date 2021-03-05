from motorsykkel import Motorsykkel


def hovedprogram():
    yamaha = Motorsykkel('Yamaha', 'AA12345', 4200)
    suzuki = Motorsykkel('Suzuki', 'AS54321', 2100)
    ducatti = Motorsykkel('Ducatti', 'AB51423', 150)
    yamaha.skrivUt()
    suzuki.skrivUt()
    ducatti.skrivUt()
    ducatti.kjor(10)
    print(ducatti.hentKilometerstand())


hovedprogram()
