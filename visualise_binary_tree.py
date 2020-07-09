from binary_tree import BinarySearchTree 
from PIL import Image, ImageTk
import tkinter as tk 

# initiate tkinter root 
window = tk.Tk() 
window.geometry("1200x800")

# variables 
image_size = (50, 50) 
path_to_images = "numbers_1_to_10/"

# getting images of numbers 1 to 10
one = Image.open(path_to_images + "one.png").resize(image_size)
two = Image.open(path_to_images + "two.png").resize(image_size)
three = Image.open(path_to_images + "three.png").resize(image_size)
four = Image.open(path_to_images + "four.png").resize(image_size)
five = Image.open(path_to_images + "five.png").resize(image_size)
six = Image.open(path_to_images + "six.png").resize(image_size)
seven = Image.open(path_to_images + "seven.png").resize(image_size)
eight = Image.open(path_to_images + "eight.png").resize(image_size)
nine = Image.open(path_to_images + "nine.png").resize(image_size)
ten = Image.open(path_to_images + "ten.png").resize(image_size)

# run root 
window.mainloop()
