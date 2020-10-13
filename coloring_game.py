from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import colorchooser
import os

class draw():
    def __init__(self, master):
        self.board = master
        self.frame = Frame(self.board, width = 400) 
        self.frame.pack() 
        self.init_dropmenu()
        self.init_spinbox()
        self.init_canvas()
        self.init_mouse_event()
        self.init_button()

        self.picture = "def_image"
        self.choose_pok(self.picture)
        self.image_number = 1
        self.pen_color = "black"
        self.pen_width = 10
        self.lastx, self.lasty = 0, 0

    def init_canvas(self):
        self.canvas = Canvas(self.board, width=450, height=550, bd = 2, cursor = "circle")
        self.ex_canvas = Canvas(self.board, width = 150)

    def init_dropmenu(self):
        self.optionList = [ x[:-4] for x in os.listdir(r"images\coloring_pages") if x.endswith(".gif") and x != "def_image.gif"]
        self.dropVar=StringVar(self.board)
        self.dropVar.set("select pokémon")
        self.dropMenu1 = OptionMenu(self.board, self.dropVar, *self.optionList, command=self.choose_pok)
        self.dropMenu1.config(font=('Kristen ITC', 15))
        self.dropMenu1.pack()

    def init_button(self):
        self.save_icon = ImageTk.PhotoImage(Image.open(r"images\src\save.png").resize((100,80))) 
        self.save_button = Button(self.frame, text='save',fg = "white", font = "arial 15", command=self.save, image = self.save_icon) 
        self.save_button.pack(side = LEFT)
        self.color_icon = ImageTk.PhotoImage(Image.open(r"images\src\paint.png").resize((100,80))) 
        self.color_button = Button(self.frame, text='change color', fg = "white",font = "arial 15", command=self.change_color, image = self.color_icon) 
        self.color_button.pack(side = RIGHT)
        self.clear_icon = ImageTk.PhotoImage(Image.open(r"images\src\clear.png").resize((100,80))) 
        self.reset_button = Button(self.frame, text='clean',font = "arial 15", command=self.clear, image = self.clear_icon) 
        self.reset_button.pack(side = RIGHT)

    def init_mouse_event(self):
        self.canvas.bind("<Button-1>", self.coordinates)
        self.canvas.bind("<B1-Motion>", self.addLine)
        self.canvas.bind("<ButtonRelease-1>", self.show)

    def init_spinbox(self):
        self.slide = Spinbox(self.frame, from_ = 10, to = 25, command = self.change_width, font = "arial 20", justify = CENTER, width = 10)
        self.slide.config(font=('Kristen ITC', 20))
        self.slide.pack(side = BOTTOM)
        number_label = Label(self.frame, text = "change pen size:")
        number_label.config(font = ('Kristen ITC', 12))
        number_label.pack(side = BOTTOM)

    def show_images(self, value):
        self.image = f"images\coloring_pages\{value}.gif"
        self.ex_image = f"images\examples\{value}_example.png"
        self.picture = value
        self.img = ImageTk.PhotoImage(Image.open(self.image).resize((450,550)))
        self.canvas.create_image(0, 0, anchor = NW, image = self.img)
        self.canvas.pack()

    def choose_pok(self, value):
        self.canvas.delete(ALL)
        self.ex_image = f"images\examples\{value}_example.png"
        self.ex_img = ImageTk.PhotoImage(Image.open(self.ex_image).resize((150,180)))
        self.ex_canvas.create_image(0, 0, anchor = NW, image = self.ex_img) 
        self.ex_canvas.pack(side = LEFT)
        self.show_images(value)

    def save(self):
        filename = f'image_{self.image_number}'
        self.canvas.postscript(file = filename + '.eps')
        self.image_number += 1

    def change_width(self):
        self.pen_width = self.slide.get()

    def change_color(self):
        self.pen_color = colorchooser.askcolor(color = self.pen_color)[1]
    
    def coordinates(self, event):
        self.lastx, self.lasty = event.x, event.y

    def addLine(self, event):
        self.canvas.create_line((self.lastx, self.lasty, event.x, event.y), width = self.pen_width, fill = self.pen_color, capstyle = ROUND, smooth = True)
        self.lastx, self.lasty = event.x, event.y

    def show(self, event):
        self.show_images(self.picture)

    def clear(self):
        self.choose_pok(self.picture)


def run():
    board=Tk(className="Coloring is fun ;)")
    title = Label(board, text='- - - Welcome to our cool coloring game - - -') 
    title.config(font = ('Kristen ITC', 18))
    title.pack()
    draw(board)
    board.mainloop() 

run()

