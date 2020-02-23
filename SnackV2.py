#!/usr/bin/python3
#! -*- coding: utf-8 -*-

#Alexander Müller TIT'19

import sys

#Info Arrays
PRO = ["Insulin", "Zucker", "Popcorn", "Kekse", "Duplo", "Schnaps", "Joy", "Kraeuter",
       "Teller", "Milch"]
PREIS = [1.20, 0.30, 3.20, 4.50, 1.60, 1.00, 0.40, 2.20, 1.30, 2.50]
ANZ = [2, 1, 2, 2, 2, 2, 2, 2, 2, 2] 
KONTO = 15.58 #in Euro 

#Einzahlen
def ein():
    """
    Einzahlen von Geld auf Konto
    """
    global KONTO

    #Abfrage Einzahlen
    try:
        DIF = round(float(input("Wie viel wollen sie einzahlen?: ")), 2)
    except ValueError:
        print("Bitte geben sie einen gültigen Wert ein! ?\n")

    #Buchungs aufs KONTO
    if DIF >= 0:
        KONTO = KONTO + DIF
        print("Ihr KONTOstand beträgt: {0}€ \n" .format(KONTO))
    else:
        print("Bitte geben sie einen gültigen Wert ein! \n")


#Kaufen
def kauf():
    """
    Auswahl, Kauf und Ausgabe der Produkte

    """
    global KONTO

    #Darstellung Angebot
    for i in range(len(PRO)):
        print(PRO[i], "   PREIS:   ", PREIS[i], "€    Anzahl: ", ANZ[i], "  [{0}]" .format(i+1))


    #Eingabe Kauf Wunsch
    try:
        AUS = int(input("Was sollen sie Kaufen? \n"))
        AUS = AUS - 1
    except ValueError:
        print("Bitte geben sie nur gültige Werte ein!")
        kauf()


    #Abfrage gültier Eingabe Wert, also nicht -1
    if AUS >= 0:

        #Deckungs-Abfrage
        if KONTO < PREIS[AUS]:
            print("Sie haben leider nicht genug Geld! \n Laden sie zunächst auf! \n")

        else:

            #Vorrats-Abfrage
            if ANZ[AUS] == 0:
                print("Das Produkt ist leider nicht mehr vorrätig! \n")

            #Verrechnung mit dem KONTO und Abzug Vorrat, AUSgabe PROdukt
            else:
                KONTO = round(KONTO - PREIS[AUS], 2)
                print("Sie haben ein/e {0} für {1}€ gekauft! \n Kontostand:  {2}€\n"
                      .format(PRO[AUS], PREIS[AUS], KONTO))
                ANZ[AUS] = ANZ[AUS] - 1
    else:
        print("Bitte geben sie einen gültigen Wert ein!")


def save():
    """
    Speichern des Kontos und der Vorräte

    """

    SAV = []

    with open(__file__, "r") as f:
        for line in f:
            SAV.append(line)

    with open(__file__, "w") as f:
        SAV[12-1] = "ANZ = [{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}] \n" \
            .format(ANZ[0], ANZ[1], ANZ[2], ANZ[3], ANZ[4], ANZ[5], ANZ[6], ANZ[7], ANZ[8], ANZ[9])
        SAV[13-1] = "KONTO = {0} #in Euro \n" .format(KONTO)

        for i in range(len(SAV)):
            f.write(SAV[i])

    sys.exit(101)

def refill():
    """
    Refill der Vorraete

    return des Refill
    """
    global ANZ

    ANZ = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#Hauptschleife
if __name__ == "__main__":

    while True:

        #Eingangs Input
        B = input("""Snack-Automat! \nWas wollen sie machen? \nKontostand: {0}€
        Um etwas Einzuzahlen drücken sie die    [1]
        Um etwas zu bestellen drücken sie die   [2]
        Um Abzubrechen drücken sie die          [3]
        """ .format(KONTO))

        #Fallunterscheidung
        if B == "1":
            ein()
        elif B == "2":
            kauf()
        elif B == "3":
            save()
        elif B == "RE":
            refill()
        else:
            print("Bitte halten sie sich an die möglichen Eingaben!\n")
