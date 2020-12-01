import random
import time
import tkinter as tk
min = 1
max = 6



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.die_roll = tk.Button(self)
        self.die_roll['text'] = 'Roll the Dice'
        self.die_roll['command'] = self.die_roll
        self.die_roll.pack(side='top')
    


    def die_roll(self):
        print('Rolling')
        time.sleep(2)
        print('You got - ')
        print(ranom.randit(min, max))
        time.sleep(1.5)
        print('If you want to play agian press the button.')


root = tk.Tk()
app = Application(master=root)
app.mainloop()

