import tkinter as tk 
from visualise_binary_tree import BinaryTreeWindow
from visualise_max_heap import MaxHeapWindow


class GraphVisualisingApplication: 

    def __init__(self, master: tk.Tk) -> None:
        bg_colour = "#263D42"
        self.master = master
        self.master.title("Graph visualisation tool")
        self.master.configure(bg=bg_colour)
        self.master.geometry("800x600")
        self.title = tk.Label(master=self.master, bg=bg_colour, 
                              text="Welcome to the graph visualisation tool", fg="orange", font=("Helvetica", 40))
        self.title.pack()
        self.binary_tree_button = tk.Button(master=self.master, text="Binary Search Tree", command=self.__run_binary_tree)
        self.binary_tree_button.pack() 
        self.heap_button = tk.Button(master=self.master, text="Max Heap", command=self.__run_heap)
        self.heap_button.pack()
        self.master.mainloop()

    def __run_binary_tree(self) -> None: 
        app_root = tk.Tk()
        app = BinaryTreeWindow(app_root) 
        app.run()

    def __run_heap(self) -> None: 
        app_root = tk.Tk() 
        app = MaxHeapWindow(app_root) 
        app.run()

    def run(self) -> None: 
        self.master.mainloop()
    

if __name__ == "__main__": 
    root = tk.Tk() 
    app = GraphVisualisingApplication(root)
    app.run()
