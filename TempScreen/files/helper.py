"""
Helper for gui.py
"""

from TempScreen.files.const import WINDOW
from TempScreen.files.test import get_cpu_temp, get_gpu_temp


def gpu_temp():

    temp = get_gpu_temp()

    WINDOW[0].gpu_label.config(text=temp)
    WINDOW[0].after(100, gpu_temp)


def cpu_temp():

    temp = get_cpu_temp()

    WINDOW[0].cpu_label.config(text=temp)
    WINDOW[0].after(100, cpu_temp)
