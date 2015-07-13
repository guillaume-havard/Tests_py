#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Programme Bip Bip.
Fait des bips pour délimiter, en boucle, une période t1 suivi d'une période t2
le tout sur une durrée limité.
Par exemple une répétition de 30s, 10s, 30s, 10s ... le tout sur 10 minutes

>>> python3 bipbip.py t1 t2 ttotal
or
>>> python3 bipbip.py
Then you will be asked to give your 3 periods

In both cases the timer will be ready.
You can launch/pause the timer with 'sapce' or reload it with 'r'.

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
# l'ajouter)

import sound
import time

manager = sound.SoundManager()
manager.play_end_pause()

print("Pause")
time.sleep(5)
print("fin")




