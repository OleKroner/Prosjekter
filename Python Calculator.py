from time import sleep

on = True

while on:
        
    print("\nHva vil du regne ut?:")
    print("\n   1 - Areal og Omkrets av firkant")
    print("   2 - Areal av trekant")
    print("\n   0 - Avslutt")

    valg = int(input("\nSvar: "))

    if valg == 1:

        høyde = int(input("\nHøyden: "))
        bredde = int(input("Bredden: "))

        areal = høyde * bredde
        omkrets = høyde * 2 + bredde * 2

        print("\nArealet er: " + str(areal))
        print("Omkretsen er: " + str(omkrets))

    elif valg == 2:
            
        grunnlinje = int(input("\nGrunnlinjen: "))
        høyde = int(input("Høyden: "))

        areal = (grunnlinje * høyde) / 2

        print("Arealet av trekanten er: " + str(areal))

    else:
        print("\nVelg et av alternativene over!")
    
    sleep(2)