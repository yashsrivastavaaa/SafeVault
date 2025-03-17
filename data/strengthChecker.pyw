import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def exit_btn_fn():
    result=messagebox.askyesno('Confirm',"Do You Want to Exit?")
    if result==True:
        app.destroy()

list = []

def showPassword(password_entry_in):
    password_ent = password_entry_in.get()
    if(len(list) %2 == 0):
        password_entry=customtkinter.CTkEntry(master = frame,placeholder_text='Enter Password',font=('Century Gothic',25),width=320)
        password_entry.insert(0,password_ent)
        password_entry.place(x=50, y=100)
        list.append(1)
    else:
        password_entry=customtkinter.CTkEntry(master = frame,placeholder_text='Enter Password', show="*",font=('Century Gothic',25),width=320)
        password_entry.place(x=50, y=100)
        password_entry.insert(0,password_ent)
        list.append(1)

def passwordStrength(pas):
    input_string = pas.get()    
    n = len(input_string) 

    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    
    for i in range(n):
        if input_string[i].islower():
            hasLower = True
        if input_string[i].isupper():
            hasUpper = True
        if input_string[i].isdigit():
            hasDigit = True
        if input_string[i] not in normalChars:
            specialChar = True

    if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
        messagebox.showinfo("Password Strength","Your Password Strength is : STRONG")
        
    elif (((hasLower or hasUpper) and hasDigit and n >= 6) or ((hasLower or hasUpper) and specialChar and n >= 6)):
        messagebox.showinfo("Password Strength","Your Password Strength is : MODERATE")
    else:
        messagebox.showerror("Password Strength","Your Password Strength is : WEAK")

app = customtkinter.CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight()               
app.geometry("%dx%d+0+0" % (width, height))
app.resizable()
app.title("Password Strength Checker")

image1=ImageTk.PhotoImage(Image.open("./data/data/Pattern.png"))
label1=customtkinter.CTkLabel(master=app,image=image1)
label1.pack()

frame=customtkinter.CTkFrame(master=label1, width=420, height=330, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label2=customtkinter.CTkLabel(master=frame, text="Strength Checker",font=('Century Gothic',35))
label2.place(relx=0.13,y=25,x=-3)

password_entry=customtkinter.CTkEntry(master = frame,placeholder_text='Enter Password', show="*",font=('Century Gothic',25),width=320)
password_entry.place(x=50, y=100)

show_pass_btn=customtkinter.CTkButton(master=frame,text="Show Password",height=35 ,width=320, command = lambda : showPassword(password_entry) )
show_pass_btn.place(x=50, y=160)

strength_Check_btn=customtkinter.CTkButton(master=frame,text="Password Strength Checker",height=35 ,width=320, command = lambda : passwordStrength(password_entry) )
strength_Check_btn.place(x=50, y=215)

exit_btn = customtkinter.CTkButton(master=frame,text="Exit",height=35 ,width=320, command = lambda : exit_btn_fn())
exit_btn.place(x=50, y=270)

app.mainloop()