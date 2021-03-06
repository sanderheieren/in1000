# 1 Oppgaven skal opprette en ny person, som vil inneholde informasjon om vedkommendes navn og alder
# og hva slags hobbyer denne personen har. Det skal være mulig å legge til hobbyer,
# samt skrive ut hva hobbyene til personen er. Det er ikke mulig å legge inn hobbyer som allerede er i
# hobby-listen. I hovedprogrammet opprettes det en person vha input fra bruker, samt deres hobbyer.

# 2, besvarelse:
class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def leggTilHobby(self, hobby):
        if hobby.lower() not in self._hobbyer:
            print(f"{hobby.lower()} er lagt til")
            self._hobbyer.append(hobby.lower())
        else:
            print(f"{hobby.lower()} finnes allerede")

    def skrivHobbyer(self):
        for index, hobby in enumerate(self._hobbyer):
            print(f"Hobby #{index + 1} - {hobby}")

    def skrivUt(self):
        print(f"Navn: {self._navn}\nAlder: {self._alder}")
        print("HOBBYER:")
        self.skrivHobbyer()


def hovedprogram():
    print('Hei! Vi vil gjerne vite ditt navn og din alder, og hva slags hobbyer du har :)')
    navn = input('Hva heter du (fornavn)?\n>>> ')
    alder = int(input('Hvor gammel er du?\n>>> '))
    person = Person(navn, alder)
    print('\nHOBBY TIME\nDu har følgende valg:')
    kommando = input('(n) legg til ny hobby\n(q) avslutte\n>>> ')
    while kommando != 'q':
        hobby = input('Oppgi en ny hobby:\n>>> ')
        person.leggTilHobby(hobby)
        kommando = input(
            '(n) for å legge til ny hobby\n(q) for å avslutte\n>>> ')
    person.skrivUt()
    print('Takk for denne gang')


hovedprogram()
