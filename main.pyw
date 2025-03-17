import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def openLoginScreen():
    result=messagebox.askyesno('Confirm',"Do You Want to open Password Manager?")
    if result==True:
        app.destroy()
        from data import loginScreen
        
def openStrengthChecker():
    result=messagebox.askyesno('Confirm',"Do You Want to open Password Strength Checker?")
    if result==True:
        app.destroy()
        from data import strengthChecker

def exit_btn_fn():
    result=messagebox.askyesno('Confirm',"Do You Want to Exit?")
    if result==True:
        app.destroy()

app = customtkinter.CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight()               
app.geometry("%dx%d+0+0" % (width, height))
app.resizable()
app.title("SafeVault")

image1=ImageTk.PhotoImage(Image.open("./data/data/Pattern.png"))
label1=customtkinter.CTkLabel(master=app,image=image1)
label1.pack()

frame=customtkinter.CTkFrame(master=label1, width=420, height=330, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label2=customtkinter.CTkLabel(master=frame, text="SafeVault",font=('Century Gothic',35))
label2.place(relx=0.33,y=25,x=-3)

loginScreen_btn=customtkinter.CTkButton(master=frame,text="Access Password Manager",height=35 ,width=320, command = lambda : openLoginScreen())
loginScreen_btn.place(x=50, y=110)

strength_Check_btn=customtkinter.CTkButton(master=frame,text="Password Strength Checker",height=35 ,width=320, command = lambda : openStrengthChecker() )
strength_Check_btn.place(x=50, y=180)

exit_btn = customtkinter.CTkButton(master=frame,text="Exit",height=35 ,width=320, command = lambda : exit_btn_fn())
exit_btn.place(x=50, y=250)

app.mainloop()