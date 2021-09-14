from time import sleep

def addere():

    tall1 = input("\nSkriv inn et tall:   ")
    tall2 = input("Skriv inn et annet tall:   ")

    try:
        int(tall1)
        int(tall2)
    
    except ValueError:
        print("\nBegge verdiene må være et tall")
        sleep(2)
        addere()
    
    else:

        sum = int(tall1) + int(tall2)

        print("\nSummen av " + str(tall1) + " og " + str(tall2) + " er " + str(sum))
        sleep(2)
        main()

def multiplisere():
    
    tall1 = input("\nSkriv inn et tall:   ")
    tall2 = input("Skriv inn et annet tall:   ")

    try:
        int(tall1)
        int(tall2)
    
    except:
        print("\nBegge verdiene må være et tall")
        sleep(2)
        multiplisere()

    else:

        produkt = int(tall1) * int(tall2)

        print("\nProduktet av " + str(tall1) + " og " + str(tall2) + " er " + str(produkt))
        sleep(2)
        main()


def main():
        
    print("\nVil du addere eller multiplisere?")
    print("\n   1 - Addere")
    print("   2 - Multiplisere")
    print("   0 - Avslutt")

    valg = input("\nSvar: ")

    try:
        int(valg)

    except ValueError:

        print("\nDu må skrive inn et tall!")
        sleep(2)
        main()

    else:

        valg = int(valg)

        if valg == 1:
            addere()

        elif valg == 2:
            multiplisere()

        elif valg != 0:

            print("\nVelg et av alternativene over!")
            sleep(2) 

if __name__ == "__main__":
    main()
