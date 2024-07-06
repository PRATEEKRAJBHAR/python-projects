from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

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
    msg=source_text.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root=Tk()
root.title("translator")
root.geometry("500x500")
root.config(bg="cyan")

label_txt=Label(root,text="Google Translator",font=("New Roman style",40,"bold"))
label_txt.place(x=100,y=40,height=55,width=300)

frame=Frame(root).pack(side=BOTTOM)

label_txt=Label(root,text="search box",font=("New Roman style",40,"bold"))
label_txt.place(x=100,y=100,height=20,width=300)



source_text=Text(frame,font=("New Roman style",20,"bold"),wrap=WORD)
source_text.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_source=ttk.Combobox(frame,value=list_text)
comb_source.place(x=10,y=300,height=40,width=100)
comb_source.set("english")


button_text=Button(frame,text="tab to translate",font=("New Roman style",40,"bold"),relief=RAISED,command=data)
button_text.place(x=170,y=300,height=40,width=100)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("hindi")


label_txt=Label(root,text="Result", font=("Tme New Roman",20,"bold"),relief=RAISED,fg="Black")
label_txt.place(x=100,y=360,height=30,width=300)

dest_txt=Text(frame,font=("New Roman style",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()