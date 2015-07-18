#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Graphical interface for a timer


"""


import tkinter as tk

class Watch(tk.Label):

    def __init__(self, master, pos, bg='green', font=('times', 20, 'bold')):
        tk.Label.__init__(self, master)
    
        self.config(bg=bg, font=font)
    
        self.grid(row = 0, column=pos)       


if __name__ == "__main__":
    pass
