#!/usr/bin/python3
#! -*- coding: utf-8 -*-

"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""

Counter_ID = 0
Abfrage = True
User_List = []
Nutzer_Konten = []

class Produkte:

    def __init__(self, Name, Preis, Anzahl):
        self.Name = Name
        self.Peis = Preis
        self.Anzahl = Anzahl


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

class Snacc:

    def __init__(self):
        pass

    def Einzahlung(self, Bname):
        """
        Einzahlen auf persönliches Konto

        :param Bname: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        Kontostand = Bname.Get_Konto()

        try:
            Konto_Cache = round(float(input("Wie viel wollen sie einzahlen?")),2)

            if Konto_Cache > 0:
                Kontostand = Kontostand + Konto_Cache
                Bname.Set_Konto(Kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")

    def Kaufen(self, Bname):
        """
        Kaufen der Produkte
        :param Bname zur Addressierung des zu belastenden Kontos
        :return: Kontostand und Produkt-Vorrat
        """


def Nutzer_Erstellung():
    """
    Einrichten der Nuter in ihre Klasse
    """
    Save = []

    Read = open("Snack_Speicher.txt", "r")
    for Lines in Read:
        Save.append(Lines)

    Save = Save[0].split("\n")
    Save = Save[0].split(", ")
    
    for Counter in range(0,len(Save),3):
        Save[Counter] = Nutzer(Save[Counter], Save[Counter+1], Save[Counter+2])

def Produkt_Erstellung():
    """
    Erstellen der Produkte
    :return:
    """
    Save = []

    Read = open("Snack_Speicher.txt", "r")
    for Lines in Read:
        Save.append(Lines)

    Save = Save[1].split(", ")
    print(Save)

    for Counter in range(0, len(Save), 3):
        Save[Counter] = Produkte(Save[Counter], Save[Counter + 1], Save[Counter + 2])

    

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

                    Bname_In = Nutzer(Bname_In, Pw_Cache, Konto_Value)

                    User_List.pop(Com+2)
                    User_List.pop(Com+1)
                    User_List.pop(Com)

                    print(User_List)
                    break

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
                    Abfrage = False
                    print("Ihr Konto wurde erstellt!")

    else:
        print("Keine gütlige Angabe!")
        exit()

    #Erstellung Automat
    Automat = Snacc()

    #Erstellung der Nutzer
    Nutzer_Erstellung()

    #Erstellung der Produkte
    Produkt_Erstellung()

    while True:

        Input_Cache = input("""\nWillkommen beim Snacc! \n Eingeloggt als: {0}
        Was wollen sie tun?
            Einzahlen   [1]
            Kaufen      [2]
            Beenden     [3]\n""" .format(Bname_In.Get_Bname()))



        if Input_Cache == "1":
            print(Bname_In.Get_Konto())  #Maybe Dictonary to convert Str into "Code"
            Automat.Einzahlung(Bname_In)
            print(Bname_In.Get_Konto())

        elif Input_Cache == "2":
            Automat.Kaufen(Bname_In)








