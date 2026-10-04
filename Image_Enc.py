from tkinter import *
from tkinter import messagebox
import os
import sqlite3

def back_command():
    app5.destroy()
    import importlib, Cryptext
    importlib.reload(Cryptext)

def clear():
    Enter_file_entry.delete(0, END)
    Enter_text_entry.delete(0, END)

def popup1():
    response = messagebox.showinfo("Successful", "Data Encrypted!")
    clear()

def popup2():
    response = messagebox.showinfo("Successful", "Data Decrypted!")
    clear()

def Encrypt():
    Enterfilename_info = Enterfilename.get()
    password = Entertext.get()
    save_path = os.getcwd()

    try:
        file = open(Enterfilename_info, "rb")
        try:
            con = sqlite3.connect("cryptex.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS filename (Filename TEXT, Password TEXT)")
            cur.execute("SELECT * FROM filename WHERE Filename=?", (Enter_file_entry.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "File already exists", parent=app5)
                clear()
            else:
                key = int(password)
                cur.execute("INSERT INTO filename (Filename, Password) VALUES (?, ?)",
                            (Enter_file_entry.get(), Enter_text_entry.get()))
                data = file.read()
                file.close()

                data = bytearray(data)
                for index, value in enumerate(data):
                    data[index] = value ^ key

                os.remove(Enterfilename_info)
                file = open(Enterfilename_info, "wb")
                file.write(data)
                file.close()
                popup1()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app5)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app5)
        clear()

def Decrypt():
    Enterfilename_info = Enterfilename.get()
    password = Entertext.get()
    save_path = os.getcwd()

    try:
        try:
            con = sqlite3.connect("cryptex.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS filename (Filename TEXT, Password TEXT)")
            cur.execute("SELECT * FROM filename WHERE Filename=? AND Password=?", (Enterfilename_info, password))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Filename and Password", parent=app5)
                clear()
            else:
                key = int(password)
                file = open(Enterfilename_info, "rb")
                data = file.read()
                file.close()

                data = bytearray(data)
                for index, value in enumerate(data):
                    data[index] = value ^ int(key)

                os.remove(Enterfilename_info)
                file = open(Enterfilename_info, "wb")
                file.write(data)
                file.close()
                cur.execute("DELETE FROM filename WHERE Filename=? AND Password=?", (Enterfilename_info, password))
                popup2()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app5)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app5)
        clear()

app5 = Tk()
app5.geometry("700x500")
app5.title("Image Encryption and Decryption")

canvas1 = Canvas(app5)  # app name differs per file
canvas1.pack(fill="both", expand=True)
bg_image = PhotoImage(file=os.getcwd()+"/assets/Encryptionbackground1.png")
canvas1.bg_image = bg_image
canvas1.create_image(0, 0, image=bg_image, anchor="nw")

Enterfilename_text = Label(text="Enter image filename with extension :", font=("times new roman", 12, "bold"))
Entertext_text = Label(text="Enter Password :", font=("times new roman", 12, "bold"))

Enterfilename_text.place(x=230, y=130)
Entertext_text.place(x=230, y=210)

Enterfilename = StringVar()
Entertext = StringVar()

Enter_file_entry = Entry(textvariable=Enterfilename, width=30, font=("times new roman", 12))
Enter_text_entry = Entry(textvariable=Entertext, width=30, font=("times new roman", 12))

Enter_file_entry.place(x=230, y=160, height=30)
Enter_text_entry.place(x=230, y=240, height=30)

button1 = Button(app5, text="Encrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Encrypt()], width="10", height="1", fg="white", bg="darkred")
button2 = Button(app5, text="Decrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Decrypt()], width="10", height="1", fg="white", bg="darkgreen")
button1.place(x=230, y=310)
button2.place(x=350, y=310)

button5 = Button(app5, text="←Back", cursor="hand2", font=("times new roman", 10, "bold"), command=lambda:[back_command()], width="8", height="1", fg="black", bg="white")
button5.place(x=5, y=5)

mainloop()