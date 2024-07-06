from tkinter import *
import os
def restart():
    os.system("Shutdown /r /t 0")
def restart_time():
    os.system("Shutdown /r /t 20")
def log_out():
    os.system("Shutdown /l /t 0")
def shutdown():
    os.system("Shutdown /s /t 0")
st=Tk()
st.configure(bg="blue")
st.title("shutdown")
st.geometry("500x500")

r_button=Button(st,text="Restart",font=("New Times Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st, text="Restart Time",font=("New Times Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st, text="Log-out",font=("New Times Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=150,y=270,height=50,width=200)

sd_button=Button(st, text="Shutdown",font=("New Times Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200)






st.mainloop()