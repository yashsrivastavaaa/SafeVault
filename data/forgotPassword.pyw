import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
key = "mysecretkey"

def passwordStrength(pas):
    input_string = pas.get()    
    n = len(input_string) 

    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

    if(input_string=='1234'):
        return True
    
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
        return True
        
    elif (((hasLower or hasUpper) and hasDigit and n >= 6) or ((hasLower or hasUpper) and specialChar and n >= 6)):
        messagebox.showinfo("Password Strength","Your Password Strength is : MODERATE")
        return True
    else:

        return False

def submit(entry_user,entry_pass,entry_ans):
    if(passwordStrength(entry_pass)):
        textFile = open('data/data/pass.text','w')
        newlist = []
        newlist.append(xor_encrypt_decrypt(entry_user.get(),key))
        newlist.append('\n')
        newlist.append(xor_encrypt_decrypt(entry_pass.get(),key))
        newlist.append('\n')
        newlist.append(xor_encrypt_decrypt(entry_ans.get(),key))
        textFile.writelines(newlist)
        messagebox.showinfo("Success","Login Credentials Updated Successfully")
        app.destroy()
        print()
        print()
        print()
        print()
        print()

        from data import afterForgot # type: ignore
    else :
        messagebox.showerror("ERROR","Your Password Strength is : WEAK")


app = customtkinter.CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight()               
app.geometry("%dx%d+0+0" % (width, height))
app.title("Forgot Password")

image1=ImageTk.PhotoImage(Image.open("./data/data/Pattern.png"))
label1=customtkinter.CTkLabel(master=app,image=image1)
label1.pack()

frame=customtkinter.CTkFrame(master=label1, width=420, height=330, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label2=customtkinter.CTkLabel(master=frame, text="Forgot Password",font=('Century Gothic',35))
label2.place(relx=0.18,y=25,x=-3)

entry_of_username=customtkinter.CTkEntry(master=frame, height=35 ,width=320, placeholder_text='Username',font=('Century Gothic',25))
entry_of_username.place(x=50, y=100)

entry_of_password=customtkinter.CTkEntry(master=frame,height=35 ,width=320, placeholder_text='Password', show="*",font=('Century Gothic',25))
entry_of_password.place(x=50, y=155)

entry_of_ans=customtkinter.CTkEntry(master=frame,height=35 ,width=320, placeholder_text='Answer',font=('Century Gothic',25))
entry_of_ans.place(x=50, y=210)
forgot_btn = customtkinter.CTkButton(master=frame,text="Submit",height=35 ,width=320, command = lambda : submit(entry_of_username,entry_of_password,entry_of_ans))
forgot_btn.place(x=50, y=270)

app.mainloop()