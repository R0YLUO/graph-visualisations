from PIL import Image, ImageTk
import tkinter as tk 
import os

# variables 
window_size = "800x600" 
background_colour = "#263D42"

# initiate tkinter root 
window = tk.Tk() 
window.geometry(window_size)
window.configure(bg=background_colour)
background_colour
# adding main window frames 
title_frame = tk.Frame(master=window, height=300, width=800, bg=background_colour) 
instruction_frame = tk.Frame(master=window, height=150, width=800, bg=background_colour)
graph_selection_frame = tk.Frame(master=window, height=150, width=800, bg=background_colour)
title_frame.pack() 
instruction_frame.pack() 
graph_selection_frame.pack() 

# adding label for title 
title_image = ImageTk.PhotoImage(Image.open(os.path.join("img", "title.png")).resize((800,300)))
title_label = tk.Label(master=title_frame, height=300, width=800, bg=background_colour, image=title_image)
title_label.pack()

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