from tkinter import *
import os
from tkinter import messagebox
from Crypto.Cipher import AES
import hashlib
import sqlite3

def back_command():
    app4.destroy()
    import importlib, Cryptext
    importlib.reload(Cryptext)

def clear():
    Enter_file_entry.delete(0, END)
    Enter_text_entry.delete(0, END)

def popup():
    response = messagebox.showinfo("Successful", "Data Decrypted!")
    clear()

def Decrypt_AES():
    Enterfilename_info = Enterfilename.get()
    password1 = Entertext.get()
    password2 = password1.encode()
    save_path = os.getcwd()

    try:
        try:
            con = sqlite3.connect("cryptex.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS filename (Filename TEXT, Password TEXT)")
            cur.execute("SELECT * FROM filename WHERE Filename=? AND Password=?", (Enterfilename_info, password1))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Filename and Password", parent=app4)
                clear()
            else:
                key = hashlib.sha256(password2).digest()
                mode = AES.MODE_CBC
                IV = 'This is an IV456'.encode()

                cipher = AES.new(key, mode, IV)

                with open(Enterfilename_info, 'rb') as e:
                    encrypted_file = e.read()

                decrypted_file = cipher.decrypt(encrypted_file)

                os.remove(Enterfilename_info)
                with open(Enterfilename_info, 'wb') as df:
                    df.write(decrypted_file.rstrip(b'0'))

                cur.execute("DELETE FROM filename WHERE Filename=? AND Password=?", (Enterfilename_info, password1))
                popup()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app4)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app4)
        clear()

def Decrypt_XOR():
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
                messagebox.showerror("Error", "Invalid Filename and Password", parent=app4)
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
                popup()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=app4)
            clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app4)
        clear()

app4 = Tk()
app4.geometry("700x500")
app4.title("Cryptex(t) - DECRYPTION")

canvas1 = Canvas(app4)  # app name differs per file
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

button1 = Button(app4, text="XOR Decrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Decrypt_XOR()], width="10", height="1", fg="white", bg="darkgreen")
button1.place(x=230, y=310)

button2 = Button(app4, text="AES Decrypt", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[Decrypt_AES()], width="10", height="1", fg="white", bg="darkgreen")
button2.place(x=350, y=310)

button5 = Button(app4, text="←Back", cursor="hand2", font=("times new roman", 10, "bold"), command=lambda:[back_command()], width="8", height="1", fg="black", bg="white")
button5.place(x=5, y=5)

mainloop()