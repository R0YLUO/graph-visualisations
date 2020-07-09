from PIL import Image, ImageTk
import tkinter as tk 
import os

# initiate tkinter root 
window = tk.Tk() 
window.geometry("1200x800")

# variables 
image_size = (50, 50) 

# getting images of numbers 1 to 10
one = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "one.png")).resize(image_size))
two = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "two.png")).resize(image_size))
three = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "three.png")).resize(image_size))
four = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "four.png")).resize(image_size))
five = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "five.png")).resize(image_size))
six = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "six.png")).resize(image_size))
seven = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "seven.png")).resize(image_size))
eight = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "eight.png")).resize(image_size))
nine = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "nine.png")).resize(image_size))
ten = ImageTk.PhotoImage(Image.open(os.path.join("numbers_1_to_10", "ten.png")).resize(image_size))

# run root 
window.mainloop()