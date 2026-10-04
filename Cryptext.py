from tkinter import *
import os

def CreateFile_Window():
    app1.destroy()
    import CreateFile

def Encrypt_Window():
    app1.destroy()
    import Encrypt

def Decrypt_Window():
    app1.destroy()
    import Decrypt

def Image_Window():
    app1.destroy()
    import Image_Enc

app1 = Tk()
app1.geometry("700x500")
app1.title("Cryptex(t)")

canvas1 = Canvas(app1)
canvas1.pack(fill="both", expand=True)
bg_image = PhotoImage(file=os.getcwd()+"/assets/Image_Background2.png")
canvas1.bg_image = bg_image
canvas1.create_image(0, 0, image=bg_image, anchor="nw")

button1 = Button(app1, text="Create File", cursor="hand2", font=("times new roman", 16, "bold"), command=lambda:[CreateFile_Window()], width="30", height="2", fg="white", bg="black")
button1.place(x=150, y=70)

button2 = Button(app1, text="Encrypt", cursor="hand2", font=("times new roman", 16, "bold"), command=lambda:[Encrypt_Window()], width="30", height="2", fg="white", bg="darkred")
button2.place(x=150, y=150)

button3 = Button(app1, text="Decrypt", cursor="hand2", font=("times new roman", 16, "bold"), command=lambda:[Decrypt_Window()], width="30", height="2", fg="white", bg="darkgreen")
button3.place(x=150, y=230)

button4 = Button(app1, text="Image Encryption & Decryption", cursor="hand2", font=("times new roman", 16, "bold"), command=lambda:[Image_Window()], width="30", height="2", fg="white", bg="darkblue")
button4.place(x=150, y=310)

mainloop()