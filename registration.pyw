from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import os
from datetime import datetime, date
from time import strftime

window = Tk()
window.geometry('250x145+540+0')
window.title("Form")
window.resizable(0, 0)
window.iconbitmap('user.ico')

def time():
   string = strftime('%H:%M:%S %p') 
   lbl.config(text = string) 
   lbl.grid(row=4, column=1)
   lbl.after(200, time) 

lbl = Label(window, font = ('arial'), fg = 'black')

def Insert_Data():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    name_info = name_entry.get()
    age_info = age_entry.get()
    mobile_info = mob_entry.get()
    time_info = current_time
    dateday_info = today
    gen_val = v.get()

    gender = ''
    if gen_val == 1:
       gender = 'Male'
    else:
       gender = 'Female'



    flag = 0
    try:
        fr = open("registration.txt", 'r')
        for line in fr:
           if (mob_entry.get() in line):
              flag = 2
        fr.close()
    except Exception as e:
        print(e)

    if flag == 2:
       messagebox.showerror("Error", "Mobile Number Already Exists")
    else:
       file = open("registration.txt", "a")
       out_line = name_info + "\t" + age_info + "\t" + gender + "\t" + mobile_info + "\t" + str(dateday_info) + "\t" + time_info + "\n"
       file.write(out_line)
       file.close()
       messagebox.showinfo("Info", 'Record Inserted Successfully')

       name_entry.delete(0, END)
       age_entry.delete(0, END)
       mob_entry.delete(0, END)
       v.set(0)
      
def Check():
   flag = 0
   try:
      file = open("registration.txt", 'r')
      for word in file:
         if (name_entry.get() in word):
            flag = 1
      file.close()
   except Exception as e:
      print(e)

   if flag == 1:
      messagebox.showerror('Error', 'User Already Exists')
   else:
      Insert_Data()
      
def data():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   today = date.today()
   name_info = name_entry.get()
   age_info = age_entry.get()
   mobile_info = mob_entry.get()
   time_info = current_time
   dateday_info = today
   gen_val = v.get()

   gender = ''
   if gen_val == 1:
      gender = 'Male'
   else:
      gender = 'Female'
        
   if name_entry.get() == "" or age_entry.get() == "" or mob_entry.get() == "" or v.get() == "":
      messagebox.showwarning("Error", "Please Enter Something First")
   elif (not (age_info.isnumeric()) ):
      messagebox.showerror('Sorry', 'Valid Input is Needed')
   elif (not (mobile_info.isnumeric()) ):
      messagebox.showerror('Sorry', 'Valid Input is Needed')
   elif (name_info.isnumeric()):
         messagebox.showerror('Sorry', 'Valid Input is Needed')
   else:
      Check()   

name_lbl = Label(text = "Name", font = ("Calibri",15))
name_lbl.grid(row=1, column=0)
age_lbl = Label(text = "Age", font =("Calibri",15))
age_lbl.grid(row=3, column=0)
mob_lbl = Label(text = "Mobile", font =("Calibri",15))
mob_lbl.grid(row=4, column=0)

name_entry = ttk.Entry(width="28")
name_entry.grid(row=1, column=1)
age_entry = ttk.Entry(width="28")
age_entry.grid(row=3, column=1)
mob_entry = ttk.Entry(width="28")
mob_entry.grid(row=4, column=1)

v = IntVar()
gender1 = ttk.Radiobutton(text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(text='Female', value=2, variable=v)

gender1.grid(row=5, column=0, sticky=W+E, padx=(15, 10), pady=(0,5))
gender2.grid(row=5, column=1, sticky=W+E, padx=(15, 10), pady=(0,5))

btn = ttk.Button(window, text = "Submit", width=10, command = data)
btn.grid(row=6, column=1, sticky=W)

name_entry.bind('<Return>', data)
age_entry.bind('<Return>', data)
mob_entry.bind('<Return>', data)

time()
window.mainloop()
