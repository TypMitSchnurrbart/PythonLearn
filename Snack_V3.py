#!/usr/bin/python3
#! -*- coding: utf-8 -*-

"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""
Counter_ID = 0
class Produkte:

    def __init__(self, Name, Preis, Anzahl):
        self.Name = Name
        self.Peis = Preis
        self.Anzahl = Anzahl

class Nutzer:

    def __init__(self, Bname, Pw,User_Id, Konto = 0):
        self.User_Id = User_Id

        self.Bname = Bname
        self.Pw = Pw
        self.Konto = Konto

    def Set_Konto(self, Konto):
        self.Konto = Konto

    def Get_Konto(self):
        return self.Konto

class Snacc:

    def __init__(self):
        pass

    def Einzahlung(self, User_Id):
        """
        Einzahlen auf persönliches Konto

        :param User_Id: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        Kontostand = User_Id.Get_Konto()

        try:
            Konto_Cache = round(float(input("Wie viel wollen sie einzahlen?")),2)

            if Konto_Cache > 0:
                Kontostand = Kontostand + Konto_Cache
                User_Id.Set_Konto(Kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")

if __name__ == "__main__":

    Bname_In = input("Username: ")
    Pw_In = input("Passwort: ")

    User_Value = Counter_ID                         #Fallunterscheidung in Neu oder Alt
    User_Value.Nutzer(Bname_In, Pw_In, Counter_ID)
    Counter_ID += 1

    while True:

        Input_Cache = input("""Willkommen beim Snacc!
        Was wollen sie tun?
            Einzahlen   [1]
            Kaufen      [2]
            Beenden     [3]""")

        if Input_Cache == "1":

        elif:







