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

        self.label = tk.Label(self, text="",
                    fg='Green', font=('Times New Roman', 30, 'bold'))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
#How will the buttons add, subtract, multiply, and divide?
        self.button = tk.Button(self, text='Divide', fg='black',
                                font=('courier new', 13, 'bold'), command=self.divide)
        self.button.place(relx=0.7, rely=0.5, relwidth=0.15, relheight=0.07)
        self.button = tk.Button(self, text='Multiply', fg='black',
                                font=('courier new', 13, 'bold'), command=self.multiply)
        self.button.place(relx=0.48, rely=0.5, relwidth=0.15, relheight=0.07)
        self.button = tk.Button(self, text='Subtract', fg='black',
                                font=('courier new', 13, 'bold'), command=self.subtract)
        self.button.place(relx=0.27, rely=0.5, relwidth=0.15, relheight=0.07)
        self.button = tk.Button(self, text='Add', fg='black',
                                font=('courier new', 13, 'bold'), command=self.add)
        self.button.place(relx=0.06, rely=0.5, relwidth=0.15, relheight=0.07)
#Text Fields, how do I get both text fields to show up?
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.5, rely=0.65, relwidth=0.3, height=18)
        self.field = tk.Entry(self)
        self.field.place(relx=0.15, rely=0.65, relwidth=0.3, height=18)
    def add(self):
        t = self.field.get()
        text = self.text_field.get()
        sum = float(t) + float(text)
        self.label.configure(text=sum)

    def subtract(self):
        t = self.field.get()
        text = self.text_field.get()
        difference = float(t)-float(text)
        self.label.configure(text = difference)
    def multiply(self):
        t = self.field.get()
        text = self.text_field.get()
        product = float(t)*float(text)
        self.label.configure(text = product)
    def divide(self):
        t = self.field.get()
        text = self.text_field.get()
        quotient = float(t)/float(text)
        self.label.configure(text = quotient)

if __name__ == '__main__':
    calc = calculator()
    calc.geometry('500x500')
    calc.mainloop()