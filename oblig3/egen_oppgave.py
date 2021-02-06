# Dette programmet skal ta for seg en quiz, mye likt som forrige oblig

riktige_svar = 0
antall_spm = 0

svarAlt = ["a", "b", "c", "d"]

quizData = [
    {
        "question": "Which language runs in a web browser?",
        "a": "Java",
        "b": "C",
        "c": "Python",
        "d": "JavaScript",
        "correct": "d",
    },
    {
        "question": "What does CSS stand for?",
        "a": "Central Style Sheets",
        "b": "Cascading Style Sheets",
        "c": "Cascading Simple Sheets",
        "d": "Cars SUVs Sailboats",
        "correct": "b",
    },
    {
        "question": "What does HTML stand for?",
        "a": "Hypertext Markup Language",
        "b": "Hypertext Markdown Language",
        "c": "Hyperloop Machine Language",
        "d": "Helicopters Terminals Motorboats Lamborginis",
        "correct": "a",
    },
    {
        "question": "What year was JavaScript launched?",
        "a": "1996",
        "b": "1995",
        "c": "1994",
        "d": "none of the above",
        "correct": "b",
    },
]


def sporsmaal(spm, spmNr):
    print(spm)
    global antall_spm
    antall_spm += 1
    for x in range(len(svarAlt)):
        print(f"{svarAlt[x]}: {quizData[spmNr][svarAlt[x]]}")
    return input()


def riktig():
    print('Bra, det var riktig!\n')


def feil():
    print('Det var dessverre ikke riktig.\n')


print('Velkommen til Web Quiz 101')

for x in range(len(quizData)):
    svar = sporsmaal(quizData[x]['question'], x)
    if svar.lower() == quizData[x]['correct']:
        riktige_svar += 1
        riktig()
    else:
        feil()

print('_______________')
print(f"Du klarte å oppnå {riktige_svar} / {antall_spm} poeng!")
if riktige_svar == 0:
    print("Øvelse gjør mester")
elif riktige_svar == 4:
    print("Alt riktig!")
elif riktige_svar <= 2:
    print("Dette var ok, men du kan bedre")
else:
    print('Ikke så gærnt!')
