def plus():
    global total
    total += int(e.get())
    display()

def minus():
    global total
    total -= int(e.get())
    display()

def reset():
    global total
    total = 100
    display()

def display():
    global secondLabel
    secondLabel.destroy() 
    secondLabel = Label(window,text=total)
    secondLabel.grid(row=0,column=1) 


from tkinter import *

total = 100

window = Tk()

firstLabel  = Label(window, text="현재 합계: ")
secondLabel = Label(window, text=total)

firstLabel.grid(row=0,column=0) 
secondLabel.grid(row=0, column=1)

e = Entry(window) 
e.grid(row=1,column=0, columnspan=3) 

plusBtn  = Button(window, text="더하기(+)", command=plus) 
minusBtn = Button(window, text="빼기(-)", command=minus) 
resetBtn = Button(window, text="초기화", command=reset)

plusBtn.grid(row=2, column=0)
minusBtn.grid(row=2, column=1)
resetBtn.grid(row=2, column=2)

window.mainloop()