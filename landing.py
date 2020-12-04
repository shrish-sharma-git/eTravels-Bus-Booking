from tkinter import *
from PIL import ImageTk,Image

#root layout
root = Tk()
root.geometry('500x500')

# Fullscreen Attrs
root.attributes("-fullscreen", True)  
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# image as a bg
img = ImageTk.PhotoImage(Image.open("./Assets/landing.png"))
label = Label(image=img).pack()

root.mainloop()
