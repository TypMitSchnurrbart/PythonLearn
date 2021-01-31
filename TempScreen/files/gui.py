#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import tkinter
from tkinter import *
from TempScreen.files.const import VERSION, WINDOW
from TempScreen.files.helper import gpu_temp, cpu_temp

def make_gui():

    #Make Window
    WINDOW[0] = tkinter.Tk()

    #Set GUI title
    WINDOW[0].title("TempScreen {0}" .format(VERSION))

    #Create dynamic_label
    WINDOW[0].gpu_label = Label(WINDOW[0], fg="black", font="Helvetica 25")
    WINDOW[0].gpu_label.pack()

    WINDOW[0].cpu_label = Label(WINDOW[0], fg="black", font="Helvetica 25")
    WINDOW[0].cpu_label.pack()

    #Get label data and update
    gpu_temp()
    cpu_temp()

    return