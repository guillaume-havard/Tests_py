#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Programme Bip Bip.
Fait des bips pour délimiter, en boucle, une période t1 suivi d'une période t2
le tout sur une durrée limité.
Par exemple une répétition de 30s, 10s, 30s, 10s ... le tout sur 10 minutes

"""
 
from docopt import docopt

import tkinter as tk
from graphic import *

help = """Le nom de mon programme trop coolbipbip

Timer that will chain twwo period 'time1' and 'time2' until the 'time_totel'
id finish.
Time in s by default, if in minute add 'm' : 10m
 
Usage:
  bipbip.py <time1> <time2> <time_total>
  bipbip.py 
 
Options:
  -h --help          
  
 
Once launched you canlaunch/pause the timer with 'space' 
or reload it with 'r'.
"""

def parse_time(time) :
    """
    take a string time and convert it in seconds (int).
    
    Can detect if the time is in minute '10m' and convert it in seconds.
    
    >>> parse_time("-5")
    0
    >>> parse_time("10")
    10
    >>> parse_time("10m")
    600
    >>> parse_time(10)
    10
    >>> parse_time(-10)
    0
    >>> parse_time(None)
    0
    
    TODO : voir pour retourner une erreur si la valeur en entrée n'est pas 
    bonne (et enlever les cas < 0)
    
    """
    ret = 0
    
    if not time:
        return 0
    
    if isinstance( time, int ):
        if time >= 0:
            return time
        else :
            return 0
        
    if time.isdigit():
        ret = int(time)
        if ret < 0 : ret = 0
    else :
        if time[:-1].isdigit() and time[-1] == "m":
            ret = int(time[:-1]) * 60
    
    return ret

# Lecture des arguments
arguments = docopt(help)   
 
time1 = parse_time(arguments["<time1>"])
time2 = parse_time(arguments["<time2>"])
time_total = parse_time(arguments["<time_total>"])

# Windows
root = tk.Tk()
app = Application(master=root)

app.timer_init_1.value_s.set(time1)
app.timer_init_2.value_s.set(time2)
app.timer_init_tot.value_s.set(time_total)

app.mainloop()



import doctest
doctest.testmod()


    
    

