import tkinter as tk
from tkinter.messagebox import * 
from constantes import style

class Container(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        #dimension de la vista login
        self.pack()
        self.place(x=0,y=0,width=900,height=660)
        self.configure(bg=style.beige)
        #edita desde aquio
        self.controller = controller
        self.init_widgets()

        self.frames={}
        self.create_frames_button = tk.Button(self, text="Start", command=self.create_frames)
        self.create_frames_button.place(x=760, y=20, width=70, height=20)

    def create_frames(self):
        f = Container2
        frame = f(self, self)
        self.frames[f] = frame
        frame.tkraise()

    def show_frame(self,container):
        frame=self.frames[container]   
        frame.tkraise()

    def control(self):
        self.show_frame(Container2)

    def init_widgets(self):
        #frame1
        self.frame1=tk.Frame(self,bg=style.beige)
        self.frame1.place(x=0,y=0,width=760, height=60)

        self.simple_game_button=tk.Button(self.frame1,text="Simple Game",bg='#FCDDD6')
        self.simple_game_button.place(x=120,y=20,width=100,height=20)

        self.general_game_button=tk.Button(self.frame1,text="General Game",bg='#FCDDD6')
        self.general_game_button.place(x=270,y=20,width=100,height=20)

        label_board_size=tk.Label(self.frame1,text='Board size: ',font='Arial 10')
        label_board_size.place(x=500,y=20,width=100,height=20)

        self.entry_board_size=tk.Entry(self.frame1,font='Arial 10')
        self.entry_board_size.place(x=600,y=20,width=40,height=20)

        


class Container2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(parent)
        self.container=container
        self.pack()
        self.place(x=0,y=60,width=1100,height=600)
        self.configure(bg=style.beige2)
        self.condition()
        self.init_widgets()

    def init_widgets(self):
        pass

    def condition(self):
        if int(self.container.entry_board_size.get()) >= 3:
            label=tk.Label(self,text='aqui2')
            label.place(x=0,y=0,width=20,height=20)

        else:
            showerror(message="Tamaño invalido.")

    def create_board(self):
        pass






