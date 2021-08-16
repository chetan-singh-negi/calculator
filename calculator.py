from tkinter import *
def click(event):
    global scrv
    text=event.widget.cget("text")
    if text=="C":
        root.destroy()
    elif text=="R":
        scrv.set("")
        scr.update()
    elif text=="=":
        value=eval(scrv.get())
        scrv.set(value)
    else:
        scrv.set(scrv.get()+text)
root=Tk()
root.title("calculator")
root.geometry("400x700")
scrv=StringVar()
scrv.set("")
scr=Entry(root,textvariable=scrv,font="lucida 35 bold")
scr.pack(fill=Y,padx=20,pady=2)
f1=Frame(root,bg="grey")
b1=Button(f1,text="C",fg="black",bg="red",font="lucida 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="R",fg="black",bg="red",font="lucida 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="%",fg="black",bg="red",font="lucida 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b4=Button(f1,text="/",fg="black",bg="red",font="lucida 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="9",fg="black",bg="red",font="lucida 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="8",fg="black",bg="red",font="lucida 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="7",fg="black",bg="red",font="lucida 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b4=Button(f1,text="*",fg="black",bg="red",font="lucida 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="6",fg="black",bg="red",font="lucida 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="5",fg="black",bg="red",font="lucida 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="4",fg="black",bg="red",font="lucida 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b4=Button(f1,text="-",fg="black",bg="red",font="lucida 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)

f1.pack()
f1=Frame(root,bg="grey")
b1=Button(f1,text="3",fg="black",bg="red",font="lucida 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="2",fg="black",bg="red",font="lucida 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="1",fg="black",bg="red",font="lucida 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)
b4=Button(f1,text="+",fg="black",bg="red",font="lucida 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="0",fg="black",bg="red",font="lucida 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="00",fg="black",bg="red",font="lucida 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text=".",fg="black",bg="red",font="lucida 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)
b4=Button(f1,text="=",fg="black",bg="red",font="lucida 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)
f1.pack()

root.mainloop()
