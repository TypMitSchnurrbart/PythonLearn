#!/usr/bin/env/python3
# ! -*- coding: utf-8 -*-

import math as m
import tkinter
from tkinter import *
import sys
import time
import multiprocessing

global WIDTH, HEIGHT
global maxItr, m_color, c_r, zoom
global xa, ya, rt, it, ir, bt, end, alt_xa, red, green, blue, first

WIDTH = 520                 # Breite des Bildes#
HEIGHT = 520                # Hoehe des Bildes
maxItr = 100                 # maximale Interationen
m_color = "#000000"         # in HexCode
c_r = [22, 181, 3]        # RGB in RGB
c_growth = [6, 8, 2]        #RGB Wachstum in Absolut
zoom = 1                    # ZoomFaktor

# Technische Variablen
xa = 0  # Pixel X-Achse
ya = 0  # Pixel Y-Achse

inv_xa = 0
inv_ya = 0

rt = 0  # Rechnugsträger RealTeil
it = 0  # Rechnungsträger ImgTeil

ir = 0  # Aktuelle Anzahl Iterationen
bt = 0  # Betrag der komplexen Zahl
end = False  # Erfolgspunkt

f_test = True
ir_cache = ""
z_cache = ""


def gui():

    global img
    global scale_HEIGHT, scale_WIDTH, ir_entry, z_entry
    global WIDTH, HEIGHT, f_test
    global window

    if f_test == True:
        window = Tk()
        window.title("Mandelbrot")

    #Scale Abfrage
    scale_HEIGHT = Scale(window, from_=360, to=910, label="Y - Achse", length=150, resolution=10, orient=HORIZONTAL)
    scale_WIDTH = Scale(window, from_=360, to=910, label="X - Achse", length=150, resolution=10, orient=HORIZONTAL)

    #Scale auf gewählten Wert setzen (Anzeige)
    scale_WIDTH.set(WIDTH)
    scale_HEIGHT.set(HEIGHT)

    # Erstellung der Widgets
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#FFFFFF")
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((0, 0), image=img, state="normal", anchor=tkinter.NW)
    button = Button(window, text="Start!", command=flow, width = 20)

    ir_entry = Entry(window, textvariable = StringVar)
    disc = Label(window, text="Mandelbrot \n Eigene Angaben:")
    ir_entry_label = Label(window, text="Iterationen: ")

    z_entry = Entry(window, textvariable = StringVar)
    z_entry_label = Label(window, text="Zoomfaktor: ")


    #Entrys auf Vorgänger-Wert
    ir_entry.insert(0,str(maxItr))
    z_entry.insert(0,str(1/zoom))


    #Erstellung und Platzierung Widgets
    scale_HEIGHT.grid(row = 1, column = 1, sticky = N)
    scale_WIDTH.grid(row = 2, column = 1, sticky = N)

    canvas.grid(row = 0, column = 0, sticky = W+E+N+S, rowspan=7)

    button.grid(row = 7, column = 1, sticky = W)

    ir_entry.grid(row = 3, column = 2, sticky = E)
    ir_entry_label.grid(row = 3, column = 1, sticky = W)
    disc.grid(row = 0, column = 1, sticky = N+E)

    z_entry.grid(row = 4, column = 2, sticky = E)
    z_entry_label.grid(row = 4, column = 1, sticky = W)


def m_pic():
    alt_xa = 0  # Hilfsvariable Geladen

    red = c_r[0]  # Übergabe der RGB Einstellungen
    green = c_r[1]
    blue = c_r[2]

    start_time = time.time()  # Start-Zeit

    # Hauptschleife; Iterationen für die Pixel
    for xa in range(1, WIDTH + 1):
        for ya in range(1, HEIGHT + 1):
            end = False
            bt = 0
            ir = 0

            # Konvertierung in kleinen Zahlen Bereich und Float:
            real_c = float((xa / WIDTH) * 3 * zoom - 2.2 * zoom)
            img_c = float((ya / HEIGHT) * 3 * zoom - 1.5 * zoom)

            # Iterationen
            while bt <= 2 and end == False:

                if bt == 0:
                    bt = 0
                    real_n = 0
                    img_n = 0
                else:
                    real_n = rt
                    img_n = it

                # Real Teil
                rt = (real_n * real_n + (-1 * (img_n * img_n))) + real_c
                # img Teil
                it = (real_n * img_n) * 2 + img_c

                # Betrag
                bt = m.sqrt(rt ** 2 + it ** 2)

                # End-Schleife
                if ir == maxItr:
                    end = True
                    # Pixel einfärben:
                    img.put(m_color, to=(xa, ya))
                    ir = 0
                    bt = 0

                # Geladen
                trans = abs(xa)
                if xa != alt_xa:
                    if trans % 10 == 0:
                        pro = WIDTH / 100
                        loe = round(trans / pro)
                        print("{0}% geladen".format(loe))

                # Hilfskonvertierung Geladen
                alt_xa = xa

                # Coloring
                # '''
                if bt > 2 and end == False:

                    for c_ir in range(0, ir + 1):
                        red += c_growth[0]
                        green += c_growth[1]
                        blue += c_growth[2]

                        if red >= 255:
                            red = 0
                        elif green >= 255:
                            green = 0
                        elif blue >= 255:
                            blue = 0

                    c_trans = "#{0:02x}{1:02x}{2:02x}".format(red, green, blue)

                    img.put(c_trans, to=(xa, ya))
                    red = c_r[0]
                    green = c_r[1]
                    blue = c_r[2]
                    # '''

                # Erfassung der Iterationen
                ir = ir + 1

    # Zeiterfassung
    end_time = time.time()

    it_time = end_time - start_time
    us_time = round(it_time / 60)
    sec = round((it_time % 60))
    print("{0}min{1}sec".format(us_time, sec))

    d_time = Label(window, text="Zeit letzter Durchlauf:  {0}min {1}sec" .format(us_time, sec))
    d_time.grid(row = 6, column = 1, sticky = E)


def flow():
    global f_test
    global HEIGHT
    global WIDTH
    global maxItr
    global ir_cache
    global z_cache
    global zoom

    #Übergabe Eingabewerte
    if f_test == False:
        HEIGHT = scale_HEIGHT.get()
        WIDTH = scale_WIDTH.get()
        ir_cache = ir_entry.get()
        z_cache = z_entry.get()

        #Iterationen Angabe
        if ir_cache == "":
            ir_cache = ""
        else:
            try:
                ir_cache = int(ir_cache)
            except:
                sys.exit(102)
            maxItr = ir_cache

        #Zoom-Faktor Angabe
        if z_cache == "":
            z_cache = ""
        else:
            try:
                z_cache = round(float(z_cache),2)
            except:
                sys.exit(102)
            zoom = 1/z_cache    #Kehrbruch da 2fache Vergröserung -> 0.5 Faktor

    #Erstellung der Anwendung
    gui()
    m_pic()
    f_test = False


#Hauptschleife
if __name__ == "__main__":
    flow()
    mainloop()



