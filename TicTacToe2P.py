from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter.ttk as ttk1
import random
tk=Tk()
tk.title("Tic Tac Toe Game")
tk.geometry("1500x1500+0+0")
tk.iconbitmap(default="ttt.ico")
def dpmain():
    s=ttk1.Style()
    s.configure("BW.TLabel", foreground="black", background="white",height=125,width=55,font=("Times 14 italic"))
    s.configure("BW1.TLabel", foreground="red", background="white",height=125,width=55,font=("Times 18 bold"))
    s.configure("BW2.TLabel", foreground="blue", background="white",height=3,width=25,font=("Times 18 italic"))
    s.configure("BW3.TLabel", foreground="blue", background="white",height=3,width=15,font=("Times 18 italic"))
    s.configure("BW4.TLabel", foreground="red", background="white",width=3,height=1,font=("Courier 45 bold"))
    s.configure("b1.TButton", font=('Times 130 italic'),height=10,width=4,foreground="black",background="white")
    s.configure("b2.TButton", font=('Times 20'),height=1,width=13,foreground="black",background="white")
    image1 = Image.open('jefbot_musashi.jpg')
    global img
    img = ImageTk.PhotoImage(image1)
    label0=Label(tk,image=img).place(x=0,y=0)
    def exitg():
            tkinter.messagebox.showinfo("Thank You For Playing","Play Again Soon :)")
            exit()
    global click
    click=True
    global countp1
    countp1=IntVar()
    countp1.set(0)
    global countp2
    countp2=IntVar()
    countp2.set(0)
    global counttie
    counttie=IntVar()
    counttie.set(0)
    global plr1
    plr1=StringVar()
    plr1.set("Player 1 (X)")
    global plr2
    plr2=StringVar()
    plr2.set("Player 2 (O)")
    global plr1l
    plr1l=StringVar()
    plr1l.set("X")
    global plr2l
    plr2l=StringVar()
    plr2l.set("O")
    frame=Frame(tk).grid(row=0,column=0)
    label101=ttk1.Label(frame,text="Enter Player Detail's",style="BW1.TLabel")
    label101.place(x=70,y=30)
    label103=ttk1.Label(frame,text="Enter Player 1 Name :",style="BW2.TLabel")
    label103.place(x=20,y=100)
    entry1=ttk1.Entry(frame,textvariable=plr1,foreground="purple", background="white",width=25,font=("Times 18 italic"))
    entry1.place(x=270,y=100)
    label1013=ttk1.Label(frame,text="Player Letter :",style="BW2.TLabel")
    label1013.place(x=600,y=100)
    entry11=ttk1.Entry(frame,textvariable=plr1l,foreground="purple", background="white",width=3,font=("Times 18 italic"))
    entry11.place(x=750,y=100)
    label102=ttk1.Label(frame,text="Enter Player 2 Name :",style="BW2.TLabel")
    label102.place(x=20,y=200)
    entry2=ttk1.Entry(frame,textvariable=plr2,foreground="purple", background="white",width=25,font=("Times 18 italic"))
    entry2.place(x=270,y=200)
    label1023=ttk1.Label(frame,text="Player Letter :",style="BW2.TLabel")
    label1023.place(x=600,y=200)
    entry21=ttk1.Entry(frame,textvariable=plr2l,foreground="purple", background="white",width=3,font=("Times 18 italic"))
    entry21.place(x=750,y=200)
    def p2game():
        global plr1
        val1=plr1.get()

        plr1.set(str.capitalize(val1))
        global plr2
        val2=plr2.get()
        plr2.set(str.capitalize(val2))
        global plr1l
        val3=plr1l.get()


        plr1l.set(val3[0].upper())
        global plr2l
        val4=plr2l.get()
        plr2l.set(val4[0].upper())
        if val3==val4:
            tkinter.messagebox.showinfo("Sorry"," Player Letter's Can't Be Same :(")
        elif val1==val2:
            tkinter.messagebox.showinfo("Sorry"," Player Name's Can't Be Same :(")
        else:
            game()
        
    button101=ttk1.Button(frame,text="Submit",style="b2.TButton",command=lambda:p2game())
    button101.place(x=200,y=300)
    button102=ttk1.Button(tk,text="EXIT",style="b2.TButton",command=lambda:exitg())
    button102.place(x=400,y=300)
    f1=open("highscore.txt","r")
    r=f1.read()
    text16=Text(frame,width=60,height=10,font=("Courier 15 bold"),fg="Black")
    text16.place(x=15, y=400)
    text16.insert(END,r)

    def game():
        global click
        l=[0,1]
        pgoes1=random.choice(l)
        if pgoes1==1:
            click=True
            tkinter.messagebox.showinfo(plr1.get()+" Goes First",plr1.get()+" "+plr1l.get()+" Goes First:)")
        elif pgoes1==0:
            click=False
            tkinter.messagebox.showinfo(plr2.get()+" Goes First",plr2.get()+" "+plr2l.get()+" Goes First:)")
        def exitmain():
            tkinter.messagebox.showinfo("Thank You For Playing","Play Again Soon :)")
            f1=open("highscore.txt","a")
            f1.write("\n"+plr1.get()+"\t\t"+str(countp1.get())+"\t\t"+str(countp2.get())+"\t\t"+str(counttie.get()))
            f1.write("\n"+plr2.get()+"\t\t"+str(countp2.get())+"\t\t"+str(countp1.get())+"\t\t"+str(counttie.get()))
            f1.close()
            dpmain()
            
        global img
        label1=Label(tk,image=img).place(x=0,y=0)
        global count
        count=0
                
        def chkcount():
            global counttie
            global click
            if count==9:
                counttie.set(counttie.get()+1)
                click=True
                var=tkinter.messagebox.askyesno("Game Is A TIE","Game Is A TIE\n Do You Want To Play Again :")
                if var==1:
                    game()
                elif var==0:
                    exitmain()
                    
        def check(button):
            global click
            global count
            chkcount()
            if button["textvariable"]==" " and click==True:
                button["textvariable"]=plr1l
                click=False
                count+=1
            elif button["textvariable"]==" " and click==False:
                button["textvariable"]=plr2l
                click=True
                count+=1
            checkwin()
            chkcount()
            
        def checkwin():
            global click
            global countp1
            global countp2
            global plr1l
            p1=plr1l.get()
            global plr2l
            p2=plr2l.get()
            if(button1["text"]==p1 and button2["text"]==p1 and button3["text"]==p1 or
               button4["text"]==p1 and button5["text"]==p1 and button6["text"]==p1 or
               button7["text"]==p1 and button8["text"]==p1 and button9["text"]==p1 or
               button3["text"]==p1 and button5["text"]==p1 and button7["text"]==p1 or
               button1["text"]==p1 and button5["text"]==p1 and button9["text"]==p1 or
               button1["text"]==p1 and button4["text"]==p1 and button7["text"]==p1 or
               button2["text"]==p1 and button5["text"]==p1 and button8["text"]==p1 or
               button3["text"]==p1 and button6["text"]==p1 and button9["text"]==p1 ):
                countp1.set(countp1.get()+1)
                click=True
                var=tkinter.messagebox.askyesno("Winner Is "+plr1.get(),plr1l.get()+" Has Just Won A Game\n Do You Want To Play Again :")
                if var==1:
                    game()
                elif var==0:
                    exitmain()
                    
            elif(button1["text"]==p2 and button2["text"]==p2 and button3["text"]==p2 or
                 button4["text"]==p2 and button5["text"]==p2 and button6["text"]==p2 or
                 button7["text"]==p2 and button8["text"]==p2 and button9["text"]==p2 or
                 button3["text"]==p2 and button5["text"]==p2 and button7["text"]==p2 or
                 button1["text"]==p2 and button5["text"]==p2 and button9["text"]==p2 or
                 button1["text"]==p2 and button4["text"]==p2 and button7["text"]==p2 or
                 button2["text"]==p2 and button5["text"]==p2 and button8["text"]==p2 or
                 button3["text"]==p2 and button6["text"]==p2 and button9["text"]==p2 ):
                countp2.set(countp2.get()+1)
                click=True
                var=tkinter.messagebox.askyesno("Winner Is "+plr2.get(),plr2l.get()+" Has Just Won A Game\n Do You Want To Play Again :")
                if var==1:
                    game()
                elif var==0:
                    exitmain()
        
        Button=StringVar()
        button1=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button1))
        button1.grid(row=1,column=0,sticky=S+N+E+W)
        button2=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button2))
        button2.grid(row=1,column=1,sticky=S+N+E+W)
        button3=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button3))
        button3.grid(row=1,column=2,sticky=S+N+E+W)
        button4=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button4))
        button4.grid(row=2,column=0,sticky=S+N+E+W)
        button5=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button5))
        button5.grid(row=2,column=1,sticky=S+N+E+W)
        button6=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button6))
        button6.grid(row=2,column=2,sticky=S+N+E+W)
        button7=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button7))
        button7.grid(row=3,column=0,sticky=S+N+E+W)
        button8=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button8))
        button8.grid(row=3,column=1,sticky=S+N+E+W)
        button9=ttk1.Button(tk,textvariable=" ",style="b1.TButton",command=lambda:check(button9))
        button9.grid(row=3,column=2,sticky=S+N+E+W)

        label11=ttk1.Label(tk,textvariable=countp1,style="BW4.TLabel")
        label11.grid(row=1,column=4,padx=2,pady=2)
        label12=ttk1.Label(tk,textvariable=countp2,style="BW4.TLabel")
        label12.grid(row=2,column=4,padx=2,pady=2)
        label13=ttk1.Label(tk,textvariable=counttie,style="BW4.TLabel")
        label13.grid(row=3,column=4,padx=2,pady=2)
        label2=ttk1.Label(tk,textvariable=plr1,style="BW3.TLabel")
        label2.grid(row=1,column=3,padx=2,pady=2)
        label1=ttk1.Label(tk,textvariable=plr2,style="BW3.TLabel")
        label1.grid(row=2,column=3,padx=2,pady=2)
        label3=ttk1.Label(tk,text="TIE Game",style="BW3.TLabel")
        label3.grid(row=3,column=3,padx=2,pady=2)

        button10=ttk1.Button(tk,text="Main Window",style="b2.TButton",command=lambda:exitmain())
        button10.grid(row=4,column=2,sticky=S+N+E+W)
        button101=ttk1.Button(tk,text="Restart",style="b2.TButton",command=lambda:game())
        button101.grid(row=4,column=1,sticky=S+N+E+W)

dpmain()
tk.mainloop()
