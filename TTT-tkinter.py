from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("400x500")
root.title("Tic Tac Toe")
root.config(bg="skyblue")
board=["-","-","-","-","-","-","-","-","-"]
count = 0

l1 = Label(root,text="Player 1 is X and player 2 is O",font="Arial 20 bold")
l1.place(x=0,y=310)
l2 = Label(root,text="Turn: Player1(X)",font = "Arial 20 bold")
l2.place(x=0,y=350)


#defining  functions
def quit():
    root.destroy()

def winner():
    if (board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or
        board[6] == board[7] == board[8] == "X" or board[0] == board[3] == board[6] == "X" or
        board[1] == board[4] == board[7] == "X" or board[2] == board[5] == board[8] == "X" or
        board[0] == board[4] == board[8] == "X" or board[2] == board[4] == board[6] == "X"):
        messagebox.showinfo("Winner","PLayer1(X) is winner")
    elif (board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or
          board[6] == board[7] == board[8] == "O" or board[0] == board[3] == board[6] == "O" or
          board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O" or
          board[0] == board[4] == board[8] == "O" or board[2] == board[4] == board[6] == "O"):
        messagebox.showinfo("Winner","PLayer2(O) is winner")
    elif count == 9:
        messagebox.showinfo("Tie","Nobody wins.It's a tie")



def change(button,boardval):
    global count
    if button["text"] == "-":
        if count % 2 == 0:
            button["text"] = "X"
            l2 = Label(root, text="Turn: Player2(O)", font="Arial 20 bold")
            l2.place(x=0, y=350)
            board[boardval] = "X"
        else:
            button["text"] ="O"
            l2 = Label(root, text="Turn: Player1(X)", font="Arial 20 bold")
            l2.place(x=0, y=350)
            board[boardval]= "O"
        count += 1
        if count >= 5:
            winner()
    else:
        messagebox.showinfo("Error","The box is occupied")




#making buttons
b1=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b1,0),padx=2,activebackground="white")
b1.place(x=0,y=0)
b2=Button(root,text="-",bg="black",fg="white",width=19,height=6,command=lambda:change(b2,1),activebackground="white")
b2.place(x=130,y=0)
b3=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b3,2),activebackground="white")
b3.place(x=270,y=0)
b4=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b4,3),activebackground="white")
b4.place(x=0,y=100)
b5=Button(root,text="-",bg="black",fg="white",width=19,height=6,command=lambda:change(b5,4),activebackground="white")
b5.place(x=130,y=100)
b6=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b6,5),activebackground="white")
b6.place(x=270,y=100)
b7=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b7,6),activebackground="white")
b7.place(x=0,y=200)
b8=Button(root,text="-",bg="black",fg="white",width=19,height=6,command=lambda:change(b8,7),activebackground="white")
b8.place(x=130,y=200)
b9=Button(root,text="-",bg="black",fg="white",width=17,height=6,command=lambda:change(b9,8),activebackground="white")
b9.place(x=270,y=200)
Button(root,text="Quit",font="Algerian 10",width=5,bg="black",fg="white",command=quit).place(x=180,y=450)

root.mainloop()
