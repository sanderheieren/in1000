from spillebrett import Spillebrett

def main():
    brett = Spillebrett(6,6)
    brett.tegnBrett()
    brett.finnNabo(4,4)
    brett.finnNabo(0,0)
    brett.finnNabo(0,4)
    brett.finnNabo(4,0)
    brett.finnNabo(2,2)


main()