from tkinter import *
import speedtest

def speedcheck():
    pb=speedtest.Speedtest()
    pb.get_servers()
    down=str(round(pb.download()/(10**6),3))+ "mbps"
    up=str(round(pb.upload()/(10**6),3))+ "mbps"
    rajbhar_ji2.config(text=down)
    rajbhar_ji.config(text=up)



prateek=Tk()
prateek.title("bholenath")
prateek.config(bg="cyan")
prateek.geometry("500x500")

rajbhar=Label(prateek,text="Internet Speed Test",font=("Times New Roman",30,"bold"),bg="black",fg="white")
rajbhar.place(x=60,y=40,height=50,width=380)

rajbhar=Label(prateek,text="Download Speed",font=("Times New Roman",30,"bold"),bg="orange",fg="white")
rajbhar.place(x=60,y=140,height=50,width=380)

rajbhar_ji=Label(prateek,text="00",font=("Times New Roman",30,"bold"),bg="orange",fg="white")
rajbhar_ji.place(x=60,y=240,height=50,width=380)

rajbhar=Label(prateek,text="upload Speed",font=("Times New Roman",30,"bold"),bg="orange",fg="white")
rajbhar.place(x=60,y=340,height=50,width=380)

rajbhar_ji2=Label(prateek,text="00",font=("Times New Roman",30,"bold"),bg="orange",fg="white")
rajbhar_ji2.place(x=60,y=440,height=50,width=380)

button=Button(prateek,text="Download Speed",font=("Times New Roman",30,"bold"),bg="red",fg="blue",relief=RAISED,cursor="plus",command=speedcheck)
button.place(x=60,y=540,height=50,width=380)

prateek.mainloop()