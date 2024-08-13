import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

def open_file():
    filetypes = (('JPG', '*.jpg'),
                 ('PNG', '*.png'),
                 ('All files', '*.*'))
    f = fd.askopenfilename(filetypes=filetypes)
    return f

def open_image():
    path = open_file()
    picturePath.config(text=f"{path}")

    img = Image.open(path)

    global picture
    picture = ImageTk.PhotoImage(img)
    canvasPicture.create_image(200,200,image = picture)
    canvasPicture.itemconfig(pictureText, text = "")

def open_watermark():
    path = open_file()
    watermarkPath.config(text=f"{path}")

    img = Image.open(path)

    global watermark
    watermark = ImageTk.PhotoImage(img)
    canvasWatermark.create_image(200, 200, image=watermark)
    canvasWatermark.itemconfig(watermarkText, text="")

window = tk.Tk()
window.minsize(width = 500, height = 500)
window.title("Image Watermarking")
window.config(pady=30, padx=30)

uploadPicture = tk.Button(text = "Upload picture!", command = open_image)
uploadPicture.grid(row = 0, column = 1)

picturePath = tk.Label(text = "Please, upload an image!")
picturePath.grid(row = 1,column = 1)

uploadWatermark = tk.Button(text = "Upload watermark!", command = open_watermark)
uploadWatermark.grid(row = 2, column = 1)

watermarkPath = tk.Label(text = "Please, upload a watermark image!")
watermarkPath.grid(row = 3,column = 1)

canvasPicture = tk.Canvas()
canvasPicture.config(width = 400, height = 400, background = "white")
pictureText = canvasPicture.create_text(200,200, text = "Uploaded picture will\nbe shown here!", font = ("Arial", 20, "bold"))
canvasPicture.grid(row = 4, column = 0)

canvasWatermark = tk.Canvas()
canvasWatermark.config(width = 400, height = 400, background = "white")
watermarkText = canvasWatermark.create_text(200,200, text = "Uploaded watermark will\nbe shown here!", font = ("Arial", 20, "bold"))
canvasWatermark.grid(row = 4, column = 2)

placeWatermark = tk.Button(text = "Place watermark!")
placeWatermark.grid(row = 5, column = 1)

window.mainloop()