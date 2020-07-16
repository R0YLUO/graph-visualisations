from PIL import Image, ImageTk
import tkinter as tk 
import os


class GraphVisualisingApplication: 

    def __init__(self, window_size: str, background_colour: str) -> None: 
        self.window = tk.Tk()
        self.window.geometry(window_size)
        self.window.configure(bg=background_colour) 
        self.background_colour = background_colour
        self.WIDTH = int(window_size.split('x')[0])
        self.HEIGHT = int(window_size.split('x')[1])
        self.number_images = get_number_images()
        self.__set_frames()

    def __set_frames(self) -> None: 
        # setting up frame configurations 
        title_width = self.WIDTH
        title_height = self.HEIGHT // 2
        instruction_height = self.HEIGHT // 4 
        buttons_height = self.HEIGHT // 4

        # packing frames 
        self.title_frame = tk.Frame(master=self.window, width=title_width, height=title_height, bg=self.background_colour)
        self.title_frame.pack() 
        self.instruction_frame = tk.Frame(master=self.window, width=title_width, height=instruction_height, bg=self.background_colour)
        self.instruction_frame.pack() 
        self.buttons_frame = tk.Frame(master=self.window, width=title_width, height=buttons_height, bg=self.background_colour)
        self.buttons_frame.pack() 

    def run(self) -> None:
        # set up title 
        title_height = self.HEIGHT//2
        title_width = self.WIDTH
        title_image = ImageTk.PhotoImage(Image.open(os.path.join("img", "title.png")).resize((title_width, title_height)))
        title_label = tk.Label(master=self.title_frame, width=title_width, height=title_height, bg=self.background_colour, image=title_image)
        title_label.pack()
        # set up instruction 
        instruction_height = self.HEIGHT // 4 
        instruction_width = self.WIDTH 
        instruction_label = tk.Label(master=self.instruction_frame, width=instruction_width, height=instruction_height, bg=self.background_colour, text="Select the type of graph to visualise", fg="white", font=("Helvetica", 18), anchor='n')
        instruction_label.pack() 
        # run window 
        self.window.mainloop() 


def get_number_images() -> list: 
    image_size = (50, 50)
    number_images = []
    for number in range(1, 11): 
        path = os.path.join("numbers_1_to_10", str(number) + ".png")
        number_images.append(ImageTk.PhotoImage(Image.open(path).resize(image_size)))
    return number_images


if __name__ == "__main__": 
    app = GraphVisualisingApplication("800x600", "#263D42")
    app.run()

