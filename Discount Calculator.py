import tkinter as tk
from tkinter import ttk
room=tk.Tk()
Frame1=tk.LabelFrame(room,text="Enter A Value",background='red')
Frame1.place(x=20,y=10,relwidth=1,height=300)
Frame2=tk.LabelFrame(room,text="Enter A Value")
Frame2.place(x=20,y=500,relwidth=1)

value1=tk.StringVar()
value2=tk.StringVar()

name1=tk.Label(Frame1,text="Enter A Product Mrp Value")
name2=tk.Label(Frame1,text="Enter A Product Actual Value")
l1=tk.Entry(Frame1)
l2=tk.Entry(Frame1)

name11=tk.Label(Frame2,text="Discount in Percentage(%)")
name22=tk.Label(Frame2,text="Discount In Rupees")
V1=tk.Label(Frame2,textvariable=value1)
V2=tk.Label(Frame2,textvariable=value2)


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



def vv(event=None):
   try:
      s = int(l1.get()) - int(l2.get())
      value2.set("Differnce :\t"+str(s)+"")
      s1 = int(s) / int(l1.get()) * 100
      value1.set("Discount :\t" + str(int(s1))+" %")
   except:
      pass



l1.bind("<KeyRelease>",vv)
l2.bind("<KeyRelease>",vv)



l1.bind("<Return>",lambda event=None:l2.focus() )
l2.bind("<Return>",lambda event=None:l1.focus() )
l1.focus()

room.mainloop()
