import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

watermark = ""

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
    canvasPicture.create_image(picture.width()/2,picture.height()/2,image = picture)
    canvasPicture.config(scrollregion=(0,0,picture.width(),picture.height()))
    canvasPicture.itemconfig(pictureText, text = "")

def open_watermark():
    path = open_file()
    watermarkPath.config(text=f"{path}")

    img = Image.open(path)

    global watermark
    watermark = ImageTk.PhotoImage(img)
    canvasWatermark.create_image(watermark.width()/2,watermark.height()/2, image=watermark)
    canvasWatermark.config(scrollregion=(0,0,watermark.width(),watermark.height()))
    canvasWatermark.itemconfig(watermarkText, text="")

def placeWatermark(event):
    x = event.x
    y = event.y
    canvasPicture.delete("watermark")
    canvasPicture.create_image(x,y,image=watermark,tag = "watermark")

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


#################### CANVASFORTHEPICTURE ####################
canvas_framePicture = tk.Frame(window)
canvas_framePicture.grid(row=4, column=0)

canvasPicture = tk.Canvas(canvas_framePicture, width = 400, height = 400, background = "white", scrollregion = (0,0,2000,2000))
pictureText = canvasPicture.create_text(200,200, text = "Uploaded picture will\nbe shown here!", font = ("Arial", 20, "bold"))
canvasPicture.grid(row = 0, column = 0)

xscrolPicture = tk.Scrollbar(canvas_framePicture, orient = "horizontal", command=canvasPicture.xview)
xscrolPicture.grid(row=1,column = 0, sticky ='ew')
canvasPicture.config(xscrollcommand=xscrolPicture.set)

yscrollPicture = tk.Scrollbar(canvas_framePicture, orient="vertical", command=canvasPicture.yview)
yscrollPicture.grid(row=0, column=1, sticky='ns')
canvasPicture.config(yscrollcommand=yscrollPicture.set)

pictureLabel = tk.Label(text = "Original Image")
pictureLabel.grid(row = 5, column = 0)

canvasPicture.bind("<Button-1>", placeWatermark)

#################### CANVASFORTHEWATERMARK ####################
canvas_frameWatermark = tk.Frame(window)
canvas_frameWatermark.grid(row=4, column=2)

canvasWatermark = tk.Canvas(canvas_frameWatermark, width = 400, height = 400, background = "white", scrollregion = (0,0,2000,2000))
watermarkText = canvasWatermark.create_text(200,200, text = "Uploaded watermark will\nbe shown here!", font = ("Arial", 20, "bold"))
canvasWatermark.grid(row = 0, column = 0)

xscrolWatermark = tk.Scrollbar(canvas_frameWatermark, orient = "horizontal", command=canvasWatermark.xview)
xscrolWatermark.grid(row=1,column = 0, sticky ='ew')
canvasWatermark.config(xscrollcommand=xscrolWatermark.set)

yscrollWatermark = tk.Scrollbar(canvas_frameWatermark, orient="vertical", command=canvasWatermark.yview)
yscrollWatermark.grid(row=0, column=1, sticky='ns')
canvasWatermark.config(yscrollcommand=yscrollWatermark.set)

watermarkLabel = tk.Label(text = "Watermark Image")
watermarkLabel.grid(row = 5, column = 2)


# placeWatermark = tk.Button(text = "Place watermark!")
# placeWatermark.grid(row = 6, column = 1)

window.mainloop()