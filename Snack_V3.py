#!/usr/bin/python3
#! -*- coding: utf-8 -*-

"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""

import sys

Counter_ID = 0
Abfrage = True
User_List = []
Nutzer_Konten = []
Produkt_Auswahl = ["Insulin", "Kekse", "Buch"]
Preise = [4.50, 2.30, 1.69]
Anz = []

class Produkte:

    def __init__(self, Name, Preis, Anzahl):
        self.Name = Name
        self.Preis = Preis
        self.Anzahl = Anzahl

        Produkt_Auswahl.append(self.Name)
        print(Produkt_Auswahl)

    def Get_Preis(self):
        return self.Preis


class Nutzer:

    def __init__(self, Bname, Pw, Konto = 0):

        self.Bname = Bname
        self.Pw = Pw
        self.Konto = Konto

        Nutzer_Konten.append(self.Bname)

    def Set_Konto(self, Konto):
        self.Konto = Konto

    def Get_Konto(self):
        return self.Konto

    def Get_Bname(self):
        return self.Bname

    def Get_Pw(self):
        return self.Pw

class Snacc:

    def __init__(self):
        pass

    def Einzahlung(self, Bname):
        """
        Einzahlen auf persönliches Konto

        :param Bname: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        Kontostand = float(Bname.Get_Konto())

        try:
            Konto_Cache = round(float(input("Wie viel wollen sie einzahlen? \n")), 2)

            if Konto_Cache > 0:
                Kontostand = round(float(Kontostand + Konto_Cache), 2)
                Bname.Set_Konto(Kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")


    def Kaufen(self, Bname, Prod, Anzahl):
        """
        Kaufen der Produkte
        :param Bname:
        :param Prod:
        :param Anzahl:
        :return:
        """
        Kontostand = Bname.Get_Konto()

        for Pro in range(0, len(Prod)):
            print("{0}  Preis: {1}€  Rest: {2}   [{3}]" .format(Prod[Pro], Preise[Pro], Anzahl[Pro], Pro ))

        try:
            Auswahl = int(input("""Was wollen sie kaufen? \n"""))
        except ValueError:
            sys.exit()

        if Kontostand >= Preise[Auswahl]:
            if Anz[Auswahl] > 0:

                Anz[Auswahl] = Anz[Auswahl] - 1
                Kontostand = round(Kontostand - Preise[Auswahl], 2)

                print("Sie haben {0} gekauft \n Restguthaben: {1}€ \n"
                      .format(Prod[Auswahl], Kontostand))
                Bname.Set_Konto(Kontostand)

            else:
                print("Leider nicht mehr vorrätig! \n")

        else:
            print("Sie haben nicht genug Geld!\n")




def Produkt_Menge():
    """
    Erstellen der Produkte Mengen
    :return:
    """
    Save = []

    Read = open("Snack_Speicher.txt", "r")
    for Lines in Read:
        Save.append(Lines)

    Save = Save[1].split(", ")

    for Count in range(0,len(Save)):
        Save[Count] = int(Save[Count])

    print(Save)
    return Save




def Speichern(Benutzername, Comt, Anzahlen):
    """
    Speichern der Benutzer und Mengen
    :param Benutzername:
    :param Comt:
    :param Anzahlen:
    :return:
    """
    Save = []

    Balance = Benutzername.Get_Konto()

    Leser = open("Snack_Speicher.txt", "r")

    for Lines in Leser:
        Save.append(Lines)

    Leser.close()

    Save = Save[0].split(", ")

    Leser = open("Snack_Speicher.txt", "w")

    if Comt >= 0:
        Save[Comt + 2] = Balance

        for i in Save:
            End = len(Save) - 1
            if i == Save[End]:
                Leser.write("{0}" .format(i))
            else:
                Leser.write("{0}, " .format(i))


    else:
        Save.append(Benutzername.Get_Bname())
        Save.append(Benutzername.Get_Pw())
        Save.append(Benutzername.Get_Konto())


    Save = Anzahlen

    for i in Save:
        End = len(Save) - 1
        if i == Save[End]:
            Leser.write("{0}" .format(i))
        else:
            Leser.write("{0}, " .format(i))

    Leser.close()
    sys.exit(201)



    

if __name__ == "__main__":

    Boot = input("Haben sie bereits ein Konto? j/n \n")

    if Boot == "j":
        Bname_In = input("Username: ")
        Pw_In = input("Passwort: ")

        Reader = open("Snack_Speicher.txt","r")
        for Line in Reader:
            User_List.append(Line)

        User_List = User_List[0].split("\n")
        User_List = User_List[0].split(", ")
        print(User_List)

        for Com in range(len(User_List)):

            Name_Cache = User_List[Com]

            if Name_Cache == Bname_In:
                Pw_Cache = User_List[Com+1]

                if Pw_In == Pw_Cache:
                    Counter_ID = Com
                    print("Richtige Daten!\n")

                    Konto_Value = User_List[Com+2]

                    Bname_In = Nutzer(Bname_In, Pw_Cache, round(float(Konto_Value),2))

                    User_List.pop(Com+2)
                    User_List.pop(Com+1)
                    User_List.pop(Com)

                    print(User_List)
                    break

                else:
                    print("Falsches Passwort!")
                    exit()

            elif Name_Cache != Bname_In and Com == len(User_List)+1:
                print("Kein gültiger Benutzername!")
                exit()


    elif Boot == "n":
        while Abfrage == True:
            Bname_In = input("Neuer Username: ")
            Pw_In = input("Neues Passwort: ")

            Reader = open("Snack_Speicher.txt", "r")
            for Line in Reader:
                User_List.append(Line)

            User_List = User_List[0].split(", ")
            print(User_List)

            for Com in range(0,len(User_List)):

                Name_Cache = User_List[Com]

                if Name_Cache == Bname_In:
                    print("Name existiert bereits! \n")

                elif Name_Cache != Bname_In and Com == len(User_List)-1:
                    Bname_In = Nutzer(Bname_In, Pw_In)
                    Com = -1
                    Abfrage = False
                    print("Ihr Konto wurde erstellt!")

    else:
        print("Keine gütlige Angabe!")
        exit()

    #Erstellung Automat
    Automat = Snacc()

    #Erstellung der Nutzer
    #Nutzer_Erstellung()

    #Erstellung der Produkte
    Anz = Produkt_Menge()

    while True:

        Input_Cache = input("""\nWillkommen beim Snacc! \n Eingeloggt als: {0}
        Guthaben: {1}€
        Was wollen sie tun?
            Einzahlen   [1]
            Kaufen      [2]
            Beenden     [3]\n""" .format(Bname_In.Get_Bname(), Bname_In.Get_Konto()))



        if Input_Cache == "1":
            Automat.Einzahlung(Bname_In)
            print("Ihr neuer Kontostand: {0}€ \n" .format(Bname_In.Get_Konto()))

        elif Input_Cache == "2":
            Automat.Kaufen(Bname_In, Produkt_Auswahl, Anz)

        elif Input_Cache == "3":
            Speichern(Bname_In, Counter_ID, Anz)








