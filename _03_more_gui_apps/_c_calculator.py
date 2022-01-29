"""
Create a simple calculator app
"""
import tkinter as tk
class calculator(tk.Tk):

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
    def __init__(self):
        super().__init__()
#What to put in text??? Create a function?
        self.label = tk.Label(self, text="???",
                    fg='blue', font=('Times New Roman', 40, 'bold'))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
#Have to create a function for command = self.______& change x,y,width,height
        self.button = tk.Button(self, text='Add', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.button = tk.Button(self, text='Subtract', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.button = tk.Button(self, text='Multiply', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.button = tk.Button(self, text='Divide', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
#Text Fields, how do I connect this with the button press and label?
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)
if __name__ == '__main__':
    calc = calculator()
    calc.geometry('500x500')
    calc.mainloop()