from PIL import Image, ImageTk
import os
import tkinter as tk
from image_processor import get_number_images
from functools import partial


class MaxHeapWindow: 
    WIN_WIDTH = 1200
    WIN_HEIGHT = 600

    def __init__(self, master: tk.Tk) -> None: 
        self.master = master
        self.master.geometry(str(self.WIN_WIDTH) + 'x' + str(self.WIN_HEIGHT))
        self.master.title("Visualise the max heap")
        self.canvas = tk.Canvas(master=self.master, height=450)
        self.canvas.pack(fill=tk.BOTH)
        self.instruction = tk.Label(master=self.master, text="Click on a number to add it to the heap")
        self.instruction.pack()
        self.number_buttons_frame = tk.Frame(master=self.master, width=self.WIN_WIDTH, height=150)
        self.number_buttons_frame.pack()
        self.number_images = get_number_images(self.master, (50,50))
        self.heap = MaxHeapOnCanvas(self.canvas, get_number_images(self.master, (20,20)))
        self.__display_number_buttons()
    
    def __display_number_buttons(self) -> None: 
        for row in range(2): 
            for col in range(5): 
                number_index = row * 5 + col 
                number = number_index + 1 
                button = tk.Button(master=self.number_buttons_frame) 
                button.config(image=self.number_images[number_index], command=partial(self.heap.insert, number))
                button.grid(row=row, column=col)

    def run(self) -> None: 
        self.master.mainloop()


class NumberOnCanvas: 

    def __init__(self, number, image, x_coord, y_coord):
        self.number = number
        self.image = image 
        self.x_coord = x_coord
        self.y_coord = y_coord 
        self.line_to_parent = None
        self.coords_of_parent = None
    
    def add_to_canvas(self, canvas: tk.Canvas, coords_of_parent=None): 
        canvas.create_image(self.x_coord, self.y_coord, image=self.image)
        if coords_of_parent is not None: 
            self.line_to_parent = canvas.create_line(coords_of_parent[0], coords_of_parent[1], self.x_coord, self.y_coord)

    def get_coords(self): 
        return self.x_coord, self.y_coord

    def shift(self, new_x, new_y): 
        pass 


class MaxHeapOnCanvas: 

    def __init__(self, canvas: tk.Canvas, number_images: list):
        self.canvas = canvas
        self.number_images = number_images
        self.array = []  # our max heap will be implemented by an array 
        self.array.append(None)  # first element in array will be None for ease of indexing 
        self.size = 0
        self.level = 1
        self.level_capacity = 2**(self.level - 1)
        self.level_size = 0
        self.coords_to_add_new = [600, 20]
        self.line_side_shift = 800
        self.line_verticle_shift = 40
    
    def insert(self, number: int): 
        self.size += 1  
        self.__execute_insert(number)
        self.level_size += 1
        self.__update_level()
        self.__update_coords_to_add_new()
        # self.__raise(self.size)

    def __execute_insert(self, number: int): 
        parent_coords = None
        if self.size > 1: 
            parent_coords = self.array[self.size//2].get_coords() 
        number_on_canvas = NumberOnCanvas(number, self.number_images[number - 1], self.coords_to_add_new[0], self.coords_to_add_new[1])
        number_on_canvas.add_to_canvas(self.canvas, parent_coords)
        self.array.append(number_on_canvas)

    def __update_level(self): 
        if self.level_size == self.level_capacity: 
            self.level_size = 0 
            self.level += 1 
            self.level_capacity = 2**(self.level - 1)
            self.coords_to_add_new[1] += self.line_verticle_shift
            self.line_side_shift //= 2 
            if self.line_side_shift < 50: 
                self.line_side_shift = 50
    
    def __update_coords_to_add_new(self): 
        next_parent_coords = self.array[(self.size + 1) // 2].get_coords()
        if self.size // 2 * 2 != self.size:  # self.size is odd
            self.coords_to_add_new[0] = next_parent_coords[0] - self.line_side_shift
        else: 
            self.coords_to_add_new[0] = next_parent_coords[0] + self.line_side_shift 

    def __raise(self, index): 
        if index > 1 and self.array[index // 2].number < self.array[index].number: 
            self.__swap(index//2, index)
            self.__raise(index//2)

    def __swap(self, index1, index2): 
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]
