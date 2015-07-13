#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Manage the sound for the application
"""
import pygame
import pygame.mixer as mix
import time

PATH_SOUND = "Sounds/"

class SoundManager:
    """
    Manage the sound for the application
    
    Will call the good sound for the different moment of the timer.
    The different call will be executed in different threads.
    
    TODO : comportement s'il manque un son
    TODO : faire les sons dans des threads
    """
    
    def __init__(self):
        pygame.init()
        mix.init()
    
        # Voir le comportement à adopter si un ou tous les sons ne sont pas là.
        self.sound_pause_1 = mix.Sound(PATH_SOUND + "beep-pause-1.wav")
        self.sound_pause_2 = mix.Sound(PATH_SOUND + "beep-pause-2.wav")
        self.sound_fin = mix.Sound(PATH_SOUND + "beep-fin.wav")
        self.sound_finfin = mix.Sound(PATH_SOUND + "beep-finfin.wav")
    
    def play_end_pause(self):
        self.sound_pause_1.play()
        time.sleep(1)
        self.sound_pause_1.play()
        time.sleep(1)
        self.sound_pause_2.play()
        time.sleep(1)
    
    def play_end(self):
        self.sound_fin.play()
        time.sleep(1)
        
    def play_end_timer(self):        
        self.sound_finfin.play()
        time.sleep(1)
        
if __name__ == "__main__":
    test = SoundManager()
   
    test.play_end_pause()
    test.play_end()
    test.play_end_timer()
    
    
    
    
