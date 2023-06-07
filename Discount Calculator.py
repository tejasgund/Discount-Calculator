import tkinter as tk
from tkinter import ttk
room=tk.Tk()
room.geometry("900x900")

Frame1=tk.LabelFrame(room,text="Enter A Value")
Frame2=tk.LabelFrame(room,text="Enter A Value")


value1=tk.StringVar()
value2=tk.StringVar()
right_wrong=0

name1=tk.Label(Frame1,text="Enter A Product Mrp Value")
name2=tk.Label(Frame1,text="Enter A Product Actual Value")
l1=tk.Entry(Frame1)
l2=tk.Entry(Frame1)

name11=tk.Label(Frame2,text="Discount in Percentage(%)")
name22=tk.Label(Frame2,text="Discount In Rupees")
V1=tk.Label(Frame2,textvariable=value1)
V2=tk.Label(Frame2,textvariable=value2)

Frame1.place(x=20,y=10,relwidth=1,height=300)
Frame2.place(x=20,y=500,relwidth=1)
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
name1.grid(row=0,column=0)
name2.grid(row=1,column=0)
name11.grid(row=0,column=0)
name22.grid(row=1,column=0)
V1.grid(row=0,column=1)
V2.grid(row=1,column=1)

l1,l2,name1,name2.grid(pady=20,padx=20,ipadx=20,ipady=20)
V1,V2,name11,name22.grid(pady=20,padx=20,ipadx=20,ipady=20)

#Design
def normal():
    room.configure(background="black")
    f1_bg="red"
    f2_bg="lightblue"
    f1_font=("Arial", 25)
    f2_font=("Arial", 25)
    labels_font=("Arial", 15)
    entry_fonts=("Arial", 15)
    name1.configure(background=f1_bg,font=labels_font)
    name2.configure(background=f1_bg,font=labels_font)
    name11.configure(background=f1_bg,font=labels_font)
    name22.configure(background=f1_bg,font=labels_font)
    l1.configure(font=entry_fonts)
    l2.configure(font=entry_fonts)
    V1.configure(font=entry_fonts)
    V2.configure(font=entry_fonts)
    Frame1.configure(background=f1_bg,font=f1_font)
    Frame2.configure(background=f1_bg,font=f2_font)
normal()

def vv(event=None):
   try:
      s = int(l1.get()) - int(l2.get())
      value2.set(" :\t"+str(s)+"")
      s1 = int(s) / int(l1.get()) * 100
      value1.set(" :\t" + str(int(s1))+" %")
   except:
        right_wrong=1
        room.configure(background="black")

    




l1.bind("<KeyRelease>",vv)
l2.bind("<KeyRelease>",vv)



l1.bind("<Return>",lambda event=None:l2.focus() )
l2.bind("<Return>",lambda event=None:l1.focus() )
l1.focus()

room.mainloop()
