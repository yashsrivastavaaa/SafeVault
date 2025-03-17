import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# USERNAME : test1234 password : 1234  forgot password ans : answer

app = customtkinter.CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight()               
app.geometry("%dx%d+0+0" % (width, height))
app.title("Password Manager")

alist = [line.rstrip() for line in open('data/data/pass.txt')]

def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
key = "mysecretkey"

def check(username_entry,password_entry):
    username = username_entry.get()
    password = password_entry.get()
    user = xor_encrypt_decrypt(alist[0],key)
    pass_new =xor_encrypt_decrypt(alist[1],key) 
    if(username == user and password == pass_new):
        messagebox.showinfo("Login Successful","Welcome! to Password Manager")
        app.destroy()
        from data.data import password_manager
    else:
        messagebox.showerror("Login Failed","Please Enter Correct Information")

def validityCheck(inputValue):
    ansGet = inputValue.get()
    ans = xor_encrypt_decrypt(alist[2],key)
    if(ansGet==ans):
        messagebox.showinfo("s","Success")
        app.destroy()
        import forgotPassword # type: ignore
    else:
        messagebox.showerror("ERROR","WRONG ANSWER")


def forgotPassword():
    res = messagebox.askyesno("Forgot Password","Do you want to reset Password?")
    if(res):
        forgot =Toplevel()
        forgot.geometry('670x280+650+400')
        forgot.title("Forgot Password")
        forgot.resizable(0,0)
        forgot.config(background="grey14")
        forgot.grab_set()

        forgot_text = Label(forgot,text="Answer for Forgot Question",font=('Century Gothic',25),bg="grey14",fg="white")
        forgot_text.grid(row=0,column=0,padx = 120,pady = 30)

        forgot_text_ent = customtkinter.CTkEntry(forgot,font=('Century Gothic',25),width=300)
        forgot_text_ent.grid(row=1,column = 0,padx = 20,pady = 10)

        forgot_text_btn = customtkinter.CTkButton(master=forgot,text="Submit",height=35 ,width=320,command=lambda:validityCheck(forgot_text_ent))
        forgot_text_btn.grid(row=2,column = 0,padx = 20,pady = 10)


image1=ImageTk.PhotoImage(Image.open("./data/data/Pattern.png"))
label1=customtkinter.CTkLabel(master=app,image=image1)
label1.pack()

frame=customtkinter.CTkFrame(master=label1, width=420, height=330, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label2=customtkinter.CTkLabel(master=frame, text="Log In",font=('Century Gothic',35))
label2.place(relx=0.40,y=25,x=-3)

entry_of_username=customtkinter.CTkEntry(master=frame, height=35 ,width=320, placeholder_text='Username',font=('Century Gothic',25))
entry_of_username.place(x=50, y=100)

entry_of_password=customtkinter.CTkEntry(master=frame,height=35 ,width=320, placeholder_text='Password', show="*",font=('Century Gothic',25))
entry_of_password.place(x=50, y=160)

login_button = customtkinter.CTkButton(master=frame,text="Login",height=35 ,width=320, command = lambda : check(entry_of_username,entry_of_password) )
login_button.place(x=50, y=215)
forgot_btn = customtkinter.CTkButton(master=frame,text="Forgot Password?",height=35 ,width=320, command = lambda : forgotPassword())
forgot_btn.place(x=50, y=270)

app.mainloop()