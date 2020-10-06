import math,random
from tkinter import*
from functools import partial
mines=[]
def no_of_mines(i):
    global mines
    count=0
    # for i in range(100):
    if (i-1) in mines:
        count+=1
    elif (i+1) in mines:
        count+=1
    elif (i+10) in mines:
        count+=1
    elif (i-10) in mines:
        count+=1
    elif (i+9) in mines:
        count+=1
    elif (i-9) in mines:
        count+=1
    elif (i-11) in mines:
        count+=1
    elif (i+11) in mines:
        count+=1
    return f"{count}"
def clickchk(num):
    global mines
    for i in range(100):
        if i==num:
            if i in mines:
                print("You Loose")
                for j in range(100):
                    if j in mines:
                        b[j]['text']='X'
            else:
                b[i]['text']=no_of_mines(i)
def bugs():
    digits="0123456789"
    mine=""
    mines=[]
    for j in range(10):
        for i in range(2):
            mine+=digits[math.floor(random.random()*10)]
            mines.append(int(mine))
        mine=""
    print(mines)
    return mines
    
            
fr=Tk()
fr.title("Minesweeper")
fr.geometry("350x350")
b=[]
X,Y=0,0
row=0
for i in range(100):
    b.append(Button(fr,text="",command=partial(clickchk,i)))
    b[i].place(x=X,y=Y,width=35,height=35)
    X+=35
    if i==9 or i-(10*row)==9:
        Y+=35
        X=0
        row+=1
mines=bugs()
fr.mainloop()