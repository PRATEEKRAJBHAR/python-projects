from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text=text1,src=src1,dest=dest1)
    return trans1.text

def data():
     s=comb_source.get()
     d=comb_dest.get()
     msg=source_txt.get(1.0,END)
     textget=change(text=msg,src=s,dest=d)
     dest_txt.delete(1.0,END)
     dest_txt.insert(END,textget)

gt=Tk()
gt.title("translation")
gt.geometry("500x500")
gt.config(bg="red")

gt1=Label(gt,text="Translator", font=("New Roman Time",40,"bold"),relief=RAISED)
gt1.place(x=100,y=40,height=55,width=300)

frame=Frame(gt).pack(side=BOTTOM)

gt1=Label(gt,text="Source text", font=("Time New Roman",20,"bold"),relief=RAISED,fg="Black")
gt1.place(x=100,y=100,height=20,width=300)

source_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
source_txt.place(x=10,y=130,height=150,width=480)

list_txt=list(LANGUAGES.values())

comb_source=ttk.Combobox(frame,value=list_txt)
comb_source.place(x=10,y=300,height=40,width=100)
comb_source.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=100)

comb_dest=ttk.Combobox(frame,value=list_txt)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("hindi") 

gt1=Label(gt,text="Result", font=("Tme New Roman",20,"bold"),relief=RAISED,fg="Black")
gt1.place(x=100,y=360,height=30,width=300)
 
dest_txt=Text(frame,font=("Tme New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)



gt.mainloop()
 