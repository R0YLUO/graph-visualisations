from PIL import Image, ImageTk
import os
import tkinter as tk
from image_processor import get_number_images
from functools import partial


class BinaryTreeWindow: 
    WIN_WIDTH = 1200
    WIN_HEIGHT = 600

    def __init__(self, master: tk.Tk) -> None: 
        self.master = master
        self.master.geometry(str(self.WIN_WIDTH) + 'x' + str(self.WIN_HEIGHT))
        self.master.title("Visualise binary serach tree")
        self.canvas = tk.Canvas(master=self.master, height=450)
        self.canvas.pack(fill=tk.BOTH)
        self.number_buttons_frame = tk.Frame(master=self.master, width=self.WIN_WIDTH, height=150)
        self.number_buttons_frame.pack()
        self.number_images = get_number_images(self.master, (50,50))
        self.binary_tree = BinaryTreeOnCanvas(self.canvas, get_number_images(self.master, (20,20)))
        self.__display_number_buttons()
    
    def __display_number_buttons(self) -> None: 
        for row in range(2): 
            for col in range(5): 
                number_index = row * 5 + col 
                number = number_index + 1 
                button = tk.Button(master=self.number_buttons_frame) 
                button.config(image=self.number_images[number_index], command=partial(self.binary_tree.insert, number, button))
                button.grid(row=row, column=col)

    def run(self) -> None: 
        self.master.mainloop()


class BinaryTreeNode: 

    def __init__(self, number: int): 
        self.value = number 
        self.left_child = None 
        self.right_child = None 


class BinaryTreeOnCanvas: 

    def __init__(self, canvas: tk.Canvas, number_images: list):
        self.root = None
        self.canvas = canvas
        self.number_images = number_images

    def insert(self, number: int, button: tk.Button): 
        button.destroy()
        self.root = self.__insert_aux(number, self.root, 600, 20, 350) 

    def __insert_aux(self, number: int, current: BinaryTreeNode, x_coord: int, y_coord: int, line_length: int, previous_coords: tuple = None) -> BinaryTreeNode: 
        if line_length < 50: 
            line_length = 50
        if current is None: 
            current = BinaryTreeNode(number) 
            self.__update_canvas(x_coord, y_coord, self.number_images[number - 1], previous_coords)
        elif number > current.value: 
            current.right_child = self.__insert_aux(number, current.right_child, x_coord + line_length, y_coord + 40, line_length - 160, (x_coord, y_coord))
        elif number < current.value: 
            current.left_child = self.__insert_aux(number, current.left_child, x_coord - line_length, y_coord + 40, line_length - 160, (x_coord, y_coord)) 
        return current

    def __update_canvas(self, x_coord, y_coord, img, previous_coords: tuple): 
        self.canvas.create_image(x_coord, y_coord, image=img)
        if previous_coords is not None:
            self.canvas.tag_lower(self.canvas.create_line(previous_coords[0], previous_coords[1], x_coord, y_coord))
        