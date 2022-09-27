#9a
print('mai jo kuchh bhi bolunga woh jhut hai ')
from tkinter import*
display=Tk()
display.title("Mumsad")

txt=Label(display,text="Sadik ek number ka padakku bacha hai or wo bhut mhenat karta hai",bg="green",fg="pink")
txt.grid(row=100,column=0)
#txt.pack()
#you can use pack and grid (any one )

txt2=Label(display,text="Faizan bhai bhut smart hai ",bg="yellow")
txt2.grid(row=0,column=0)
#txt2.pack()

txt3=Label(display,text="Mumsad ek dum noobda hai kuch nahi ata usko",bg="black",fg="white")
txt3.grid(row=50,column=0)

entry=Label(display,text="Kuch Bhi Dal Sakte hu Jo man kare ",bg="black",fg="white")
entry.grid(row=150,column=0)

ent=Entry(display)
ent.grid(row=150,column=1)


def button():
	btn(text="Clicked Me")
btn=Button(display,text="click me",command="Clicked")
btn.place(height=250,width=500,x=300,y=800)

txt4=Checkbutton(display,text="Sufiyan bhai sab se bade topper hai",bg="pink",fg="green")
txt4.grid(row=200,column=0)

txt5=Radiobutton(display,text="Sab bhut he Aram se pass hunge ",bg="orange",fg="blue")
txt5.grid(row=500,column=0)

scale=Scale(display,from_=0, to=200)
scale.grid(row=1000,column=0)

scalehorizontal=Scale(display,from_=0, to=200,orient=HORIZONTAL)
scalehorizontal.grid(row=2000,column=0)


display.mainloop()
