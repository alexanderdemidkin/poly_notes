# Import module
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime as dt



# Create object
root = Tk()

# Adjust size
root.geometry("1300x900")
root.title("Poly`s Notes")

# Add image file
bg = PhotoImage( file = "img/flora.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0, width=1300, height=900)

def change_image(filename):
    global bg
    bg = PhotoImage( file = filename)
    label1.configure(image = bg,width=1300, height=900)

def flora():
    change_image("img/flora.png")
    text.configure(bg="#d5ebd6", fg="#112e1a",font=("Helvetica", 16))
  

def enot():
    change_image("img/enot.png")
    text.configure(bg="#c5b3dd", fg="#211432", font=("Nimbus Sans", 16))

def plast():
    change_image("img/plast.png")
    text.configure(bg="#DBD5BE", fg="#2c291c", font=("Liberation Serif", 16))


def poly():
    change_image("img/poly.png")
    text.configure(bg="#9998c9", fg="#1b1a2e",font=("Fira Sans", 16))

def okto():
    change_image("img/okto.png")
    text.configure(bg="#c6e5e2", fg="131124",  font=("Iosevka Nerd Font Medium", 16))

def catdog():
    change_image("img/cat-dog.png")
    text.configure(bg="#e5b8d1", fg="#36232e",font=("Fantasque Sans Mono", 16))




def text_parce():
    tt = text.get("1.0", "end-1c")
    tts = gTTS(tt, lang='ru', slow=False)
    tts.save("text.mp3")
    playsound("text.mp3")
    os.remove("text.mp3")


def text_clear():
    text.delete("1.0", "end")


def text_save():
    tt = text.get("1.0", "end-1c")
    with open(f"text/text_note{dt.now()}.txt", "w") as file:
        file.write(tt)

def voice_save():
    tt = text.get("1.0", "end-1c")
    tts = gTTS(tt, lang='ru', slow=False)
    tts.save(f"music/poly_notes/voice{dt.now()}.mp3")




# Create Frame
frame1 = Frame( root)
frame1.grid(row = 0, column = 1, sticky = "n")

frame2 = Frame( root, bg="#FAFAEB")
frame2.grid(row = 2, column = 1, sticky = "n")

frame3 = Frame( root, bg = "gray75")
frame3.grid(row = 1, padx=150, pady=20, column = 1)
# Add buttons
button1 = Button( frame1, text = "Флора", command = flora)
button1.grid(row = 0, column = 0, padx=5, sticky = "nw")

button2 = Button( frame1, text = "Енотки", command = enot)
button2.grid(row = 0, column = 1, padx=5, sticky = "nw")

button3 = Button( frame1, text = "Пластилинки", command = plast)
button3.grid(row = 0, column = 2, padx=5,sticky = "nw")

button4 = Button( frame1, text = "Робокар Поли",  command = poly)
button4.grid(row = 0, column = 3, padx=5,sticky = "nw")

button5 = Button( frame1, text = "Октонавты", command = okto)
button5.grid(row = 0, column = 4, padx=5,sticky = "nw")

button6 = Button( frame1, text = "Кошечки-собачки", command = catdog)
button6.grid(row = 0, column = 5, padx=5,sticky = "nw")


button14 = Button( frame2, text = "Озвучить", command= text_parce)
button14.grid(row = 0, column = 0, padx=10,sticky = "ne")

button15 = Button( frame2, text = "Сохранить текст", command=text_save)
button15.grid(row = 0, column = 1, padx=10,sticky = "ne")

button15 = Button( frame2, text = "Сохранить голос", command=voice_save)
button15.grid(row = 0, column = 2, padx=10,sticky = "ne")


button18 = Button( frame2, text = "Очистить", command=text_clear)
button18.grid(row = 0, column = 3, padx=10,sticky = "ne")



text = Text(frame3,width=80, height=30, bg="#FAFAEB", fg='#212121', font=("Helvetica", 16), wrap=WORD)
text.grid(row=0, column=0, columnspan=2, sticky="nsew")
root.attributes('-alpha', 0.5)
#text.configure(bg='gray75')
# Add scrollbar
# Execute tkinter
root.mainloop()
