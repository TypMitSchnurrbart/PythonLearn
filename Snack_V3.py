#!/usr/bin/python3
#! -*- coding: utf-8 -*-

"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten

Alexander Müller TIT'19
"""

import sys

COUNTER_ID = 0
ABFRAGE = 1
USER_LIST = []

PRODUKT_AUSWAHL = ["Insulin", "Kekse", "Buch"]
PREISE = [4.50, 2.30, 1.69]
ANZ = []


class Nutzer:
    """
    DOC-STRING
    """

    def __init__(self, b_name, passw, konto=0):
        """
        Konstruktor Nutzer
        :param b_name:
        :param passw:
        :param konto:
        """

        self.b_name = b_name
        self.passw = passw
        self.konto = konto

        #Nutzer_Konten.append(self.b_name)

    def set_konto(self, konto):
        """
        Setter Konto
        :param konto:
        :return:
        """
        self.konto = konto

    def get_konto(self):
        """
        Getter Konto
        :return: self.konto
        """
        return self.konto

    def get_bname(self):
        """
        Getter Username
        :return:
        """
        return self.b_name

    def get_pw(self):
        """
        Getter Username
        :return:
        """
        return self.passw

class Snacc:
    """
    DOC-STRING für PyLint
    """

    def __init__(self):
        """
        Kontruktor Snacc
        """

    def einzahlung(self, b_name):
        """
        Einzahlen auf persönliches Konto

        :param b_name: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        kontostand = float(b_name.get_konto())

        try:
            konto_cache = round(float(input("Wie viel wollen sie einzahlen? \n")), 2)

            if konto_cache > 0:
                kontostand = round(float(kontostand + konto_cache), 2)
                b_name.set_konto(kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")


    def kaufen(self, b_name, prod, anzahl):
        """
        Kaufen der Produkte
        :param b_name:
        :param prod:
        :param anzahl:
        :return:
        """
        kontostand = b_name.get_konto()

        for pro in range(0, len(prod)):
            print("{0}  Preis: {1}€  Rest: {2}   [{3}]"
                  .format(prod[pro], PREISE[pro], anzahl[pro], pro))

        try:
            auswahl = int(input("""Was wollen sie kaufen? \n"""))
        except ValueError:
            sys.exit()

        if kontostand >= PREISE[auswahl]:
            if ANZ[auswahl] > 0:

                ANZ[auswahl] = ANZ[auswahl] - 1
                kontostand = round(kontostand - PREISE[auswahl], 2)

                print("Sie haben {0} gekauft \n Restguthaben: {1}€ \n"
                      .format(prod[auswahl], kontostand))
                b_name.set_konto(kontostand)

            else:
                print("Leider nicht mehr vorrätig! \n")

        else:
            print("Sie haben nicht genug Geld!\n")




def produkt_menge():
    """
    Erstellen der Produkte Mengen
    :return: Speicher Liste save
    """
    save = []

    read = open("Snack_Speicher.txt", "r")
    for lines in read:
        save.append(lines)

    save = save[1].split(", ")

    for count in range(0, len(save)):
        save[count] = int(save[count])

    return save




def speichern(benutzername, comt, anzahlen):
    """
    Speichern der Benutzer und Mengen
    :param benutzername:
    :param comt:
    :param anzahlen:
    :return: -
    """
    save = []

    balance = benutzername.get_konto()

    leser = open("Snack_Speicher.txt", "r")

    for lines in leser:
        save.append(lines)

    leser.close()

    save = save[0].split("\n")
    save = save[0].split(", ")

    leser = open("Snack_Speicher.txt", "w")

    end = 1

    if comt >= 0:
        save[comt + 2] = balance

        for i in save:
            if end == len(save):
                leser.write("{0}\n" .format(i))
            else:
                leser.write("{0}, " .format(i))
            end += 1

    else:
        save.append("{0}".format(benutzername.Get_b_name()))
        save.append("{0}".format(benutzername.get_pw()))
        save.append("{0}".format(benutzername.get_konto()))

        for i in save:
            if end == len(save):
                leser.write("{0}\n" .format(i))
            else:
                leser.write("{0}, " .format(i))
            end += 1

    save = anzahlen
    end = 1

    for i in save:

        if end == len(save):
            leser.write("{0}" .format(i))
        else:
            leser.write("{0}, " .format(i))
        end += 1

    leser.close()
    sys.exit(201)


def refill(nachschub):
    """
    Refill der Produkte
    :param nachschub:
    :return: nachschub wieder auf 2 aufegfüllt
    """
    for i in range(0, len(nachschub)):
        nachschub[i] = 2
    return nachschub


if __name__ == "__main__":

    BOOT = input("Haben sie bereits ein Konto? j/n \n")

    if BOOT == "j":
        BNAME_IN = input("Username: ")
        PW_IN = input("Passwort: ")

        READER = open("Snack_Speicher.txt", "r")
        for Line in READER:
            USER_LIST.append(Line)

        USER_LIST = USER_LIST[0].split("\n")
        USER_LIST = USER_LIST[0].split(", ")

        for Com in range(len(USER_LIST)):

            Name_Cache = USER_LIST[Com]

            if Name_Cache == BNAME_IN:
                Pw_Cache = USER_LIST[Com+1]

                if PW_IN == Pw_Cache:
                    COUNTER_ID = Com
                    print("Richtige Daten!\n")

                    BNAME_IN = Nutzer(BNAME_IN, Pw_Cache, round(float(USER_LIST[Com + 2]), 2))

                    Com = len(USER_LIST)

                else:
                    print("Falsches Passwort!")
                    sys.exit(12)

            elif Name_Cache != BNAME_IN and Com == len(USER_LIST)+1:
                print("Kein gültiger Benutzername!")
                sys.exit(13)



    elif BOOT == "n":

        READER = open("Snack_Speicher.txt", "r")
        for Line in READER:
            USER_LIST.append(Line)

        USER_LIST = USER_LIST[0].split(", ")

        while ABFRAGE == 1:

            BNAME_IN = input("Neuer Username: ")
            PW_IN = input("Neues Passwort: ")

            for Com in range(0, len(USER_LIST), 3):

                Name_Cache = USER_LIST[Com]

                if Name_Cache == BNAME_IN:
                    print("Name existiert bereits! \n")

                    Com = len(USER_LIST)

                elif Name_Cache != BNAME_IN and Com == len(USER_LIST)-1:
                    BNAME_IN = Nutzer(BNAME_IN, PW_IN)
                    COUNTER_ID = -1
                    ABFRAGE = 2
                    print("Ihr Konto wurde erstellt!")

    else:
        print("Keine gütlige Angabe!")
        sys.exit(901)


    #Erstellung Automat
    AUTOMAT = Snacc()

    #Erstellung der Produkte
    ANZ = produkt_menge()

    while True:

        INPUT_CACHE = input("""\nWillkommen beim Snacc! \n Eingeloggt als: {0}
        Guthaben: {1}€
        Was wollen sie tun?
            Einzahlen   [1]
            Kaufen      [2]
            Beenden     [3]\n""" .format(BNAME_IN.get_bname(), BNAME_IN.get_konto()))



        if INPUT_CACHE == "1":
            AUTOMAT.einzahlung(BNAME_IN)
            print("Ihr neuer Kontostand: {0}€ \n" .format(BNAME_IN.get_konto()))

        elif INPUT_CACHE == "2":
            AUTOMAT.kaufen(BNAME_IN, PRODUKT_AUSWAHL, ANZ)

        elif INPUT_CACHE == "3":
            speichern(BNAME_IN, COUNTER_ID, ANZ)

        elif INPUT_CACHE == "RE":
            ANZ = refill(ANZ)
        else:
            print("Bitte geben sie nur die verfügbaren Optionen ein")
