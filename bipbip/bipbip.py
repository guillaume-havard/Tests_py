#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Programme Bip Bip.
Fait des bips pour délimiter, en boucle, une période t1 suivi d'une période t2
le tout sur une durrée limité.
Par exemple une répétition de 30s, 10s, 30s, 10s ... le tout sur 10 minutes

"""

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


# pygame : 
#    sons
#    touches ?
#    Affichage ?

# tkinter :
#    touches ?
#    Affichage ?

# Pour les deux http://fsincere.free.fr/isn/python/cours_python_tkinter.php

# Je commence par le son (voir si automatiquement en thread ou s'il faut 
# l'ajouter) -> il faut l'ajouter
# Pseudo module de son fonctionant.
# Pour la récupération des arguments je vais utiliser docopt

 
from docopt import docopt

import sound
import time

manager = sound.SoundManager()

arguments = docopt(help)
print(arguments)
print(type(arguments["<time1>"]))

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
time1 = parse_time(arguments["<time1>"])
time2 = parse_time(arguments["<time2>"])
time_total = parse_time(arguments["<time_total>"])

print("temps pour le timer", time1, time2, time_total)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

