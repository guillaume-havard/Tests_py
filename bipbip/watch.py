#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Graphical interface for a timer


"""


import tkinter as tk

class Watch(tk.LabelFrame):

    def __init__(self, master, name, pos):
        tk.LabelFrame.__init__(self, master)
        
        self.name = name
        self.value = tk.StringVar()
        self.value.set("0")
        self.value_s = tk.IntVar()
        self.value_s.set(0)
        
        
        self.grid(row =0, column=pos)
        
        self.name_label = tk.Label(self, text=name)
        self.name_label.grid(row=1, column=0)
        
        self.value_label = tk.Label(self, text="value")
        self.value_label.grid(row=0, column=1)
        self.value_entry = tk.Entry(self, state=tk.DISABLED,
                                    textvariable=self.value)
        self.value_entry.grid(row=1, column=1)
        
        self.value_s_label = tk.Label(self, text="value (s)")
        self.value_s_label.grid(row=0, column=2)
        self.value_s_entry = tk.Entry(self,
                                      textvariable=self.value_s,
                                      validate='key')
        self.value_s_entry.grid(row=1, column=2)

        okay_value = self.register(self.value_cmd)
        self.value_s_entry["validatecommand"] = (okay_value, '%P')

    def value_cmd(self, value):
        """Called when the value is changed
        
        Check if the value is correct"""
        print("coucou :", self.name, value, "-", self.value_s.get())
        
        if str(value).isdigit(): 
        
            texte = str(self.value_s.get() // 60) + ":" + \
                    str(self.value_s.get() % 60)
            self.value.set(texte)  
            return True
        else:
            return False



print("pouet")

if __name__ == "__main__":
    pass
