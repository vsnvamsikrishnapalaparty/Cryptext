from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sqlite3
from Crypto.Cipher import AES
import hashlib

def back_command():
    app3.destroy()
    import importlib, Cryptext
    importlib.reload(Cryptext)

def clear():
    Enter_file_entry.delete(0, END)
    Enter_text_entry.delete(0, END)

def popup():
    response = messagebox.showinfo("Successful", "Data Encrypted!")
    clear()

def Encrypt_XOR():
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
                messagebox.showerror("Error", "File already exists", parent=app3)
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
                popup()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app3)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app3)
        clear()

def Encrypt_AES():
    Enterfilename_info = Enterfilename.get()
    password1 = Entertext.get()
    password2 = password1.encode()
    save_path = os.getcwd()

    try:
        try:
            con = sqlite3.connect("cryptex.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS filename (Filename TEXT, Password TEXT)")
            cur.execute("SELECT * FROM filename WHERE Filename=?", (Enter_file_entry.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "File already exists", parent=app3)
                clear()
            else:
                cur.execute("INSERT INTO filename (Filename, Password) VALUES (?, ?)",
                            (Enter_file_entry.get(), Enter_text_entry.get()))
                key = hashlib.sha256(password2).digest()
                mode = AES.MODE_CBC
                IV = 'This is an IV456'.encode()

                def pad_message(file):
                    while len(file) % 16 != 0:
                        file = file + b'0'
                    return file

                cipher = AES.new(key, mode, IV)
                with open(Enterfilename_info, 'rb') as f:
                    orig_file = f.read()

                padded_file = pad_message(orig_file)
                encrypted_message = cipher.encrypt(padded_file)

                os.remove(Enterfilename_info)
                with open(Enterfilename_info, 'wb') as e:
                    e.write(encrypted_message)

                con.commit()
                con.close()
                popup()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app3)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app3)
        clear()

app3 = Tk()
app3.geometry("700x500")
app3.title("Cryptex(t) - ENCRYPTION")

canvas1 = Canvas(app3)  # app name differs per file
canvas1.pack(fill="both", expand=True)
bg_image = PhotoImage(file=os.getcwd()+"/assets/Encryptionbackground1.png")
canvas1.bg_image = bg_image
canvas1.create_image(0, 0, image=bg_image, anchor="nw")

Enterfilename_text = Label(text="Enter file name with .txt extension :", font=("times new roman", 12, "bold"))
Entertext_text = Label(text="Enter Password :", font=("times new roman", 12, "bold"))

Enterfilename_text.place(x=230, y=130)
Entertext_text.place(x=230, y=210)

Enterfilename = StringVar()
Entertext = StringVar()

Enter_file_entry = Entry(textvariable=Enterfilename, width=30, font=("times new roman", 12))
Enter_text_entry = Entry(textvariable=Entertext, width=30, font=("times new roman", 12))

Enter_file_entry.place(x=230, y=160, height=30)
Enter_text_entry.place(x=230, y=240, height=30)

button1 = Button(app3, text="XOR Encrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Encrypt_XOR()], width="10", height="1", fg="white", bg="darkred")
button1.place(x=230, y=310)

button2 = Button(app3, text="AES Encrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Encrypt_AES()], width="10", height="1", fg="white", bg="darkred")
button2.place(x=350, y=310)

button5 = Button(app3, text="←Back", cursor="hand2", font=("times new roman", 10, "bold"), command=lambda:[back_command()], width="8", height="1", fg="black", bg="white")
button5.place(x=5, y=5)

mainloop()