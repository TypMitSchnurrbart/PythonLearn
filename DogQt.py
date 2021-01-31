#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import sys
import random

class Hund:

    #Konstruktor Klasse Hund
    def __init__(self, name, zufrieden, mass, sauber, hunger, ill):
        self.name = name
        self.zufrieden = zufrieden
        self.mass = mass
        self.sauber = sauber
        self.hunger = hunger
        self.ill = ill

    #Getter für Name
    def getName(self):
        return self.name

    #Getter und Setter für Zufrieden
    def getZufrieden(self):
        return self.zufrieden

    #Getter und Setter für Masse
    def getMass(self):
        return self.mass

    #Getter für Sauber
    def getSauber(self):
        return self.sauber

    #Getter für Hunger
    def getHunger(self):
        return self.hunger

    def getIll(self):
        return self.ill

    #Methoden
    def streicheln(self):
        self.zufrieden = self.zufrieden + 10
        self.mass = self.mass + 2
        self.sauber = self.sauber - 2
        self.hunger = self.hunger - 5

    def gassi(self):
        self.zufrieden = self.zufrieden + 5
        self.mass = self.mass - 5
        self.sauber = self.sauber - 10
        self.hunger = self.hunger - 15

    def futter(self):
        self.zufrieden = self.zufrieden + 5
        self.mass = self.mass + 15
        self.sauber = self.sauber - 5
        self.hunger = self.hunger + 30

    def waschen(self):
        self.zufrieden = self.zufrieden - 20
        self.mass = self.mass - 2
        self.sauber = self.sauber + 40
        self.hunger = self.hunger - 5

    def bact(self):
        self.ill = True

    def heal(self):
        self.ill = False

    def krank(self):
        self.zufrieden = self.zufrieden - random.randint(5,10)
        self.mass = self.mass - random.randint(5,16)
        self.sauber = self.sauber - random.randint(5,10)
        self.hunger = self.hunger - random.randint(5,15)




#Main Schleife
if __name__ == "__main__":

    #Erstellung des Hundes und Umgebungsvariablen
    hp = True   #Healthbar
    r = 0
    dr = 0      #Death Reason Wert
    he = 0      #Helper in Move Abfrage
    si = 0      #Sickness Wert
    kw = 15     #Krankheits Wahrscheinlichkeit kw/100
    kl = random.randint(1,3)       #Krankheitslänge kl+1 Runden

    tot_Z = 0
    tot_M_U = 20
    tot_M_O = 90
    tot_S = 0
    tot_H = 0

    try:
        name2 = input("Wie soll dein Hund heißen? ")
    except:
        print("Es ist ein Fehler aufgetreten!")

    #Hund Startwerte werden übergeben
    pet = Hund(name2, random.randint(30,60), 40, random.randint(30,60), random.randint(30,60), False)

    print("Und los gehts!")

    #Hauptschleife
    while hp == True:

        #Abfrage der Hund Attribute
        if pet.getZufrieden() >= tot_Z:
            if pet.getMass() >= tot_M_U and pet.getMass() <= tot_M_O:
                if pet.getSauber() >= tot_S:
                    if pet.getHunger() >= tot_H:

                        #Untersuchung ob Hund infiziert wurde
                        bac = random.randint(0,101)
                        if bac <= kw:
                            pet.bact()
                            si = kl

                        #Runden-Counter
                        r += 1

                        #Speicherung der Werte der letzten Runde
                        old_Z = pet.getZufrieden()
                        old_M = pet.getMass()
                        old_S = pet.getSauber()
                        old_H = pet.getHunger()

                        #Abfrage der Methoden
                        try:
                            move = input("\nWas willst du tun? Streicheln(1)? Gassi(2)? Füttern(3)? Waschen(4)?:  \n")
                        except:
                            print("Es ist ein Fehler aufgetreten!")
                            sys.exit(404)

                        #Auswertung der Methoden
                        if move == "1":
                            print(pet.getName(), " wird gestreichelt!")
                            pet.streicheln()
                            he = 1

                        elif move == "2":
                            print("Du gehst mit ", pet.getName(), " gassi!")
                            pet.gassi()
                            he = 1

                        elif move == "3":
                            print("Du fütterst ", pet.getName(),"!")
                            pet.futter()
                            he = 1

                        elif move == "4":
                            print("Du wäscht", pet.getName(), "!")
                            pet.waschen()
                            he = 1

                        #Falls etwas anderes als die Zahlen 1-4 eingegeben wurden
                        else:
                            print("Bitte Zahlen von 1-4 eingeben! Danke.")


                        #Abfrage ob Hund krank
                        if pet.getIll() == True and he == 1:
                            print("Dein Hund ist krank!")
                            pet.krank()


                        #Ausgabe der Hund Attribute
                        if he == 1:
                            dif_Z = pet.getZufrieden() - old_Z
                            dif_M = pet.getMass() - old_M
                            dif_S = pet.getSauber() - old_S
                            dif_H = pet.getHunger() - old_H

                            print("""Die Werte von {0} sind:
                            Zufriedenheit:  {1}         {6} 
                            Masse:          {2}kg       {7}kg
                            Sauberkeit:     {3}         {8}
                            Hunger:         {4}         {9}
                            Krank:          {5}
                            
                            Überlebte Runden: {10}     
                            """ .format(pet.getName(), pet.getZufrieden(), pet.getMass(), pet.getSauber(), pet.getHunger(), pet.getIll(),
                                        dif_Z, dif_M, dif_S, dif_H, r))

                        #Reset der Krankheit
                        if si > 0:
                            si = si - 1
                            print("Krank für ", si, "Runden")

                        elif si == 0:
                            pet.heal()

                    #Ergebnis falls Hunger Tod
                    else:
                        hp = False
                        dr = 4

                #Ergebnis falls Sauber Tod
                else:
                    hp = False
                    dr = 3

            #Ergebnis falls Mass Tod
            else:
                hp = False
                dr = 2
        #Ergebnis falls Zufrieden Tod
        else:
            hp = False
            dr = 1


    #Untersuchung des Todesereignisses
    if hp == False:
        if dr == 1:
            print(pet.getName(), " ist leider an seiner Traurigkeit gestorben.")
            sys.exit(11)

        elif dr == 2:
            print(pet.getName(), " ist leider an seiner Masse gestorben.")
            sys.exit(12)

        elif dr == 3:
            print(pet.getName(), " ist leider an seinem Dreck gestorben.")
            sys.exit(13)

        elif dr == 4:
            print(pet.getName(), " ist leider an seinem Hunger gestorben.")
            sys.exit(14)



