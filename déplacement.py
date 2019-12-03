'''bard = Image.open("bardejov.jpg")
bardejov = ImageTk.PhotoImage(bard)'''

import tkinter as tk
import random  
import time


app = tk.Tk()
app.title("Déplacement objet")
app.minsize(600,800)
app.resizable(width=True, height=True)
app.geometry("800x645+0+0")
app.configure(bg = "light blue")
Frame = tk.Frame(app, bg='navy')

level=1
running = True

def leftKey(event):
    global dx,dy
    dx=-(1.5+0.5*level)
    dy=0
        
def rightKey(event):
    global dx,dy
    dx=1.5+0.5*level
    dy=0
    
def upKey(event):
    global dx,dy
    dy=-(1.5+0.5*level)
    dx=0

def downKey(event):
    global dx,dy
    dy=1.5+0.5*level
    dx=0
    
class GameButton(tk.Button):
    """classe de boutons dans la frame de jeu"""
    
    def __init__(self,id):
        tk.Button.__init__(self,Frame)
        
        self.id = id
        
        if self.id == 0:
            self.config(text='Play',width=5, height=2, bg="blue",fg='white',
            font="GROBOLD.ttf 15 bold",relief=tk.RAISED, cursor='hand2',command=self.play)
        elif self.id == 1:
            self.config(text='Pause',width=5, height=2, bg="blue",fg='white',
            font="GROBOLD.ttf 15 bold",relief=tk.RAISED, cursor='hand2',command=self.pause)
    
    def pause(self):
        global running
        running=False
        print('Pause')
    
    def play(self):
        global running
        running = True
        print('play')
        self.deplacement()
    
    def deplacement(self):
        global dx,dy,can,L_widgets,running
        app.bind('<q>', leftKey)
        app.bind('<d>', rightKey)
        app.bind('<z>', upKey)
        app.bind('<s>', downKey)
        
        if running==True:
            for i in L_widgets:
                can.move(i,dx,dy)
            can.after(20,self.deplacement)
            

def main():
    global can,L_widgets
    
    L_widgets=[]
    can = tk.Canvas(app, width=400, height=400, bg='blue')
    
    tete=can.create_rectangle(Rectangle[0], Rectangle[1], Rectangle[0]+30, Rectangle[1]+30,
    outline='green', fill='red')
    L_widgets.append(tete)

    B_play=GameButton(0)
    B_pause=GameButton(1)
    
    can.place(x=100,y=100)
    B_play.grid(row=1,column=1,padx=2,pady=2)
    B_pause.grid(row=2,column=1,padx=2,pady=2)
    Frame.place(x=600,y=250)

    app.mainloop()
    
    
x,y = 245,24
dx,dy=1.5+0.5*level,0
l=3
Rectangle=[x,y]


if __name__=='__main__':
    main()
