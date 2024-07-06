from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def shutdown():
    os.system("shutdown /s /t 1")
def st():
    os.system("shutdown /r /t 10")
def logout():
    os.system("logout /-1")




st=Tk()
st.title("shutdown")
st.geometry("500x500")
st.config(bg="blue")

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

r_shut=Button(st,text="shutdown",font=("New times Roman",20,"bold"),cursor="plus",relief=RAISED,commond=shutdown)

r_shut.place(x=150,y=170,height=50,width=200)

r_tr=Button(st,text="reset tme",font=("New times Roman",20,"bold"),cursor="plus",relief=RAISED,command=st)
r_tr.place(x=150,y=270,height=60,width=200)

r_button=Button(st,text="logout",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
r_button.place(x=150,y=360,height=50,width=200)



st.mainloop()