from binary_tree import BinarySearchTree 
from PIL import Image, ImageTk
import os
import tkinter as tk
from image import get_number_images


class BinaryTreeWindow: 

    def __init__(self, master: tk.Tk) -> None: 
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Visualise binary serach tree")
        self.canvas = tk.Canvas(master=self.master, bg="blue", width=800, height=450)
        self.canvas.pack()
        self.number_buttons_frame = tk.Frame(master=self.master, width=800, height=100)
        self.number_buttons_frame.pack()
        self.number_images = get_number_images(self.master)
        self.__display_number_buttons()
    
    def __display_number_buttons(self) -> None: 
        for row in range(2): 
            for col in range(5): 
                button = tk.Button(master=self.number_buttons_frame) 
                button.config(image=self.number_images[row*5+col])
                button.grid(row=row, column=col)

    def run(self) -> None: 
        self.master.mainloop()