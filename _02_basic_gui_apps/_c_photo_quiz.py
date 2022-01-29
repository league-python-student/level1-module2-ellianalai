"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class photo(tk.Tk):
    def __init__(self):
        super(). __init__()
        self.label = tk.Label(self)
        self.label.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)






    # TODO 2) Create a constructor

        # TODO 3) call Tk's constructor

        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.


def question(q, a, filename):
    score = 0
    answer = simpledialog.askstring(title='', prompt=q)
    img = create_image(filename, 500, 500)
    pic.label.configure(image=img)
    # TODO 12) If the answer is correct, increase the score by 1
    if answer == a:
        score = score + 1
        messagebox.showinfo(title='', message='Good Job!! Next Question ^_^')
    else:
        messagebox.showerror(title='', message='Sorry, try again')
    return score

# TODO 5) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 6) Create an object of the tkinter class
    pic = photo()
    # TODO 7) Set the app window width and height using geometry()
    pic.geometry('500x500')
    # TODO 8) Declare and initialize a score variable
    score = 0
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable

    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)

    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.
    score += question('What is a vegetable and has the colors orange and green?', 'carrot', 'carrots.jpg')
    score += question('______ is the remains of a plant or animal who once lived a long time ago', 'fossil','fossil.jpg')
    score += question('What is mans best friend?', 'dog', 'puppy.png')
    messagebox.showinfo(title='', message = 'Your score is ' + str(score))



    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question

    # TODO 14) Display the score to the user after asking the last question
