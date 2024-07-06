#its project are not working 
from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()

    down= str(round(sp.download()/(10**6),3)) + "mbps+" #10**6 (its given mbps)
    up= str(round(sp.upload()/(10**6),3)) + "mbps+"
#set parameters where goves zero 
    lab_down.config(text=down)
    lab_up.config(text=up)



internet=Tk()
internet.title("bholenath")
internet.config(bg="cyan")
internet.geometry("500x500")

lab=Label(internet,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(internet,text="Download speed",font=("Times New Roman", 20,"bold"),cursor="plus",relief="raised")
lab.place(x=150,y=130,height=50,width=380) 

lab_down =Label(internet,text="00",font=("Times New Roman",20,"bold"),relief="raised",cursor="plus")
lab_down.place(x=150,y=260,height=80,width=170)

lab =Label(internet,text="Upload Speed",font=("Times New Roman",20,"bold"),relief="raised",cursor="plus")
lab.place(x=150,y=360,height=80,width=170)

lab_up =Label(internet,text="00",font=("Times New Roman",20,"bold"),relief="raised",cursor="plus")
lab_up.place(x=150,y=460,height=80,width=170)

o_button =Button(internet,text="check Speed",font=("Times New Roman",20,"bold"),relief="raised",bg="red",fg="white",cursor="plus",command=speedcheck)
o_button.place(x=150,y=560,height=80,width=170)




internet.mainloop()