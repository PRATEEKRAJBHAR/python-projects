from tkinter import *
import os

def restart():
    os.system ("Shutdown /r /t 1")

def restart_time():
    os.system ("Shutdown /r /t 20")

def log_out():
      os.system ("Shutdown -1")

def shutdown():
    os.system ("Shutdown /s /t 1")

st = Tk()
st.title("shutdown")
st.geometry("500x500")#its use for graphics height and width

st.config(bg="blue")#config are use to coloring pages

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

r_button=Button(st,text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
r_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text=":Log-Out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="Shut-Down",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()#iska use graphics(chart paper)ke liye kiya jata hai..