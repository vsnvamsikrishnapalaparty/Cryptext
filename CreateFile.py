from tkinter import *
from tkinter import messagebox
import os

def back_command():
    app2.destroy()
    import importlib, Cryptext
    importlib.reload(Cryptext)

def clear():
    Enter_file_entry.delete(0, END)
    Enter_text_entry.delete(0, END)

def button_command():
    response = messagebox.showinfo("Success", "File Saved Successfully", parent=app2)
    Enter_file_entry.delete(0, END)
    Enter_text_entry.delete(0, END)

def save_info():
    try:
        Enterfilename_info = Enterfilename.get()
        Entertext_info = Entertext.get()
        save_path = os.getcwd()
        filepath = os.path.join(save_path, Enterfilename_info)
        file = open(filepath, "w")
        file.write(Entertext_info)
        file.close()
        button_command()
    except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=app2)
        clear()

app2 = Tk()
app2.geometry("700x500")
app2.title("Create and Save File")

canvas1 = Canvas(app2)  # app name differs per file
canvas1.pack(fill="both", expand=True)
bg_image = PhotoImage(file=os.getcwd()+"/assets/Encryptionbackground1.png")
canvas1.bg_image = bg_image
canvas1.create_image(0, 0, image=bg_image, anchor="nw")

Enterfilename_text = Label(text="Enter file name with .txt extension :", font=("times new roman", 12, "bold"))
Entertext_text = Label(text="Enter text :", font=("times new roman", 12, "bold"))

Enterfilename_text.place(x=230, y=130)
Entertext_text.place(x=230, y=210)

Enterfilename = StringVar()
Entertext = StringVar()

Enter_file_entry = Entry(textvariable=Enterfilename, width=40, bg="lightgray", font=("times new roman", 12))
Enter_text_entry = Entry(textvariable=Entertext, width=40, bg="lightgray", font=("times new roman", 12))

Enter_file_entry.place(x=230, y=160, height=30)
Enter_text_entry.place(x=230, y=240, height=30)

button = Button(app2, text="Save file", cursor="hand2", font=("times new roman", 12, "bold"), command=lambda:[save_info()], width="20", height="1", fg="white", bg="black")
button.place(x=230, y=310)

button5 = Button(app2, text="←Back", cursor="hand2", font=("times new roman", 10, "bold"), command=lambda:[back_command()], width="8", height="1", fg="black", bg="white")
button5.place(x=5, y=5)

mainloop()