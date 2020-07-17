from PIL import Image, ImageTk
import tkinter as tk 
import os


class GraphVisualisingApplication: 

    def __init__(self, master: tk.Tk) -> None:
        bg_colour = "#263D42"
        self.master = master
        self.master.configure(bg=bg_colour)
        self.master.geometry("800x600")
        self.title = tk.Label(master=self.master, bg=bg_colour, 
                              text="Welcome to the graph visualisation tool", fg="orange", font=("Helvetica", 40))
        self.title.pack()
        self.binary_tree_button = tk.Button(master=self.master, text="Binary Search Tree", command=self.run_binary_tree)
        self.binary_tree_button.pack() 
        self.heap_button = tk.Button(master=self.master, text="Max Heap", command=self.run_heap)
        self.heap_button.pack()

    def run_binary_tree(self): 
        print("runninb  tree")

    def run_heap(self): 
        print("running heap")
    
    def run(self) -> None: 
        self.master.mainloop()


if __name__ == "__main__": 
    root = tk.Tk()
    app = GraphVisualisingApplication(root)
    app.run() 
