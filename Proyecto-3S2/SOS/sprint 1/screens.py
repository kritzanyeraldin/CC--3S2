import tkinter as tk
from tkinter.messagebox import *
from constantes import style
from Board import Board


class Container(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Dimension de la vista login
        self.pack()
        self.place(x=0, y=0, width=900, height=660)
        self.configure(bg=style.beige)
        # edita desde aquio
        self.controller = controller
        self.init_widgets()

        self.frames = {}
        self.create_frames_button = tk.Button(self, text="Start", command=self.create_frames)
        self.create_frames_button.place(x=760, y=20, width=70, height=20)

    def create_frames(self):
        f = Container2
        frame = f(self, self)
        self.frames[f] = frame
        frame.tkraise()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def control(self):
        self.show_frame(Container2)

    def init_widgets(self):
        # frame1
        self.frame1 = tk.Frame(self, bg=style.beige)
        self.frame1.place(x=0, y=0, width=760, height=60)

        self.simple_game_button = tk.Button(self.frame1, text="Simple Game", bg='#FCDDD6')
        self.simple_game_button.place(x=120, y=20, width=100, height=20)

        self.general_game_button = tk.Button(self.frame1, text="General Game", bg='#FCDDD6')
        self.general_game_button.place(x=270, y=20, width=100, height=20)

        label_board_size = tk.Label(self.frame1, text='Board size: ', font='Arial 10')
        label_board_size.place(x=500, y=20, width=100, height=20)

        self.entry_board_size = tk.Entry(self.frame1, font='Arial 10')
        self.entry_board_size.place(x=600, y=20, width=40, height=20)


class Container2(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(parent)
        self.board = None
        self.container = container
        self.pack()
        self.place(x=0, y=60, width=900, height=600)
        self.configure(bg=style.beige2)
        self.condition()

    def condition(self):
        if int(self.container.entry_board_size.get()) >= 3:
            label = tk.Label(self, text='aqui2')
            label.place(x=0, y=0, width=20, height=20)
            # self.create_board()
            self.init_widgets()


        else:
            showerror(message="Tamaño invalido.")

    def create_board(self):

        # Se actualiza el tamaño del contenedor del tablero
        self.frame_board.update()

        # Crea un tablero vacio
        '''''
        self.board_size toma el valor del tamaño del tablero que se ingresa en la interfaz despues de apretar start
        lo que se quiere es que el tamañp del tablero se adapte a su contenedor en este caso seria self.frame_board
        asi que se toma el minimo valor entre ancho y altura y luego se divide entre el tamaño del tablero ingresado 
        de esta forma se logra contener el tablero en el frame board sea cual sea el tamaño que se ingrese.
        '''

        self.board = Board(int(self.container.entry_board_size.get()))
        self.board_size = self.board.get_board_size()

        frame_width = self.frame_board.winfo_width()
        frame_height = self.frame_board.winfo_height()
        # print(f'frame {frame_width} \ncell')
        self.cell_size = min(frame_width, frame_height) / self.board_size
        # print(self.cell_size)

        self.canvas_width = self.board_size * self.cell_size
        self.canvas_height = self.board_size * self.cell_size

        self.canvas = tk.Canvas(self.frame_board, width=self.canvas_width, height=self.canvas_height)
        self.canvas.place(x=0, y=0)

        # dibuja los rectangulos del tablero
        for row in range(self.board_size):
            for col in range(self.board_size):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = (col + 1) * self.cell_size
                y1 = (row + 1) * self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', tags='cell')

                self.canvas.tag_bind('cell', '<Button-1>', self.on_cell_clicked)

    def on_cell_clicked(self, event):

        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        # Esta division nos indica el indice de la columna en la qu el usuario hace click
        col = int(x // self.cell_size)
        row = int(y // self.cell_size)

        print(f'inicio: {self.board.board}')

        piece = None
        piece = self.piece()

        if self.board.board[row][col] is None:
            if self.valueTurn.get() == 'red':
                if piece == 'S':
                    self.board.insert_piece(row, col, piece)
                    self.canvas.create_text(
                        (col + 0.5) * self.cell_size,
                        (row + 0.5) * self.cell_size,
                        text='S',
                        font=('Arial', 32),
                        fill='red'
                        )
                    self.S_red_player.deselect()
                elif piece == 'O':
                    self.board.insert_piece(row, col, piece)
                    self.canvas.create_text(
                        (col + 0.5) * self.cell_size,
                        (row + 0.5) * self.cell_size,
                        text='O',
                        font=('Arial', 32),
                        fill='red'
                        )
                    self.O_red_player.deselect()

            if self.valueTurn.get() == 'blue':
                if piece == 'S':
                    self.board.insert_piece(row, col, piece)
                    self.canvas.create_text(
                        (col + 0.5) * self.cell_size,
                        (row + 0.5) * self.cell_size,
                        text='S',
                        font=('Arial', 32),
                        fill='blue'
                        )
                    self.S_blue_player.deselect()
                elif piece == 'O':
                    self.board.insert_piece(row, col, piece)
                    self.canvas.create_text(
                        (col + 0.5) * self.cell_size,
                        (row + 0.5) * self.cell_size,
                        text='O',
                        font=('Arial', 32),
                        fill='blue'
                        )
                    self.O_blue_player.deselect()

        self.turn()

        print(f'final: {self.board.board}')

    def turn(self):
        if self.valueTurn.get() == 'red':

            self.S_blue_player.config(state='normal')
            self.O_blue_player.config(state='normal')
            self.S_red_player.config(state='disabled')
            self.O_red_player.config(state='disabled')
            self.valueTurn.set('blue')

        else:

            self.S_blue_player.config(state='disabled')
            self.O_blue_player.config(state='disabled')
            self.S_red_player.config(state='normal')
            self.O_red_player.config(state='normal')
            self.valueTurn.set('red')


    def piece(self):
        if (self.redValue.get() == 'S') or (self.blueValue.get() == 'S'):
            piece = 'S'
        elif (self.redValue.get() == 'O') or (self.blueValue.get() == 'O'):
            piece = 'O'
        else:
            piece = None

        self.redValue.set(None)
        self.blueValue.set(None)
        return piece



    def init_widgets(self):

        # frame blue_player
        self.frame_blue_player = tk.Frame(self, bg='red')
        self.frame_blue_player.place(x=0, y=0, width=210, height=500)

        # frame tablero
        self.frame_board = tk.Frame(self, bg='blue')
        self.frame_board.place(x=210, y=0, width=480, height=500)
        # print(f'frame {self.frame_board.winfo_width()}')

        # frame red_player
        self.frame_red_player = tk.Frame(self, bg='green')
        self.frame_red_player.place(x=690, y=0, width=210, height=500)

        # frame turno
        self.frame_turn = tk.Frame(self, bg='black')
        self.frame_turn.place(x=0, y=500, width=900, height=100)

        # #
        # frame blue_player(210x500)
        label_blue_player = tk.Label(self.frame_blue_player, text='Blue Player')
        label_blue_player.place(x=30, y=50, width=100, height=30)

        label_human = tk.Label(self.frame_blue_player, text='Human')
        label_human.place(x=30, y=100, width=100, height=30)

        self.blueValue = tk.StringVar()
        self.blueValue.set(None)
        self.S_blue_player = tk.Radiobutton(self.frame_blue_player, text='S', variable=self.blueValue, value='S', state='disabled')
        self.S_blue_player.place(x=50, y=150, width=100, height=30)
        self.O_blue_player = tk.Radiobutton(self.frame_blue_player, text='O', variable=self.blueValue, value='O',state='disabled')
        self.O_blue_player.place(x=50, y=200, width=100, height=30)

        ##
        # frame red_player
        label_red_player = tk.Label(self.frame_red_player, text='Red Player')
        label_red_player.place(x=30, y=50, width=100, height=30)

        label_human = tk.Label(self.frame_red_player, text='Human')
        label_human.place(x=30, y=100, width=100, height=30)

        self.redValue = tk.StringVar()
        self.redValue.set(None)
        self.S_red_player = tk.Radiobutton(self.frame_red_player, text='S', variable=self.redValue, value='S')
        self.S_red_player.place(x=50, y=150, width=100, height=30)
        self.O_red_player = tk.Radiobutton(self.frame_red_player, text='O', variable=self.redValue, value='O')
        self.O_red_player.place(x=50, y=200, width=100, height=30)

        self.replay_button = tk.Button(self.frame_red_player, text='Replay')
        self.replay_button.place(x=50, y=350, width=100, height=40)
        self.new_game_button = tk.Button(self.frame_red_player, text='New Game')
        self.new_game_button.place(x=50, y=400, width=100, height=40)

        # creamos el tablero
        self.after(1000, self.create_board())

        ##
        # frame turn (900x100)
        label_current_game = tk.Label(self.frame_turn,text='Current Turn: ')
        label_current_game.place(x=330, y=30, width=80, height=30)

        self.valueTurn = tk.StringVar()
        self.valueTurn.set('red')

        label_turn = tk.Label(self.frame_turn,textvariable=self.valueTurn)
        label_turn.place(x=410, y=30, width=50, height=30)




