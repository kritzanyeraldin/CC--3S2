import tkinter as tk
from tkinter.messagebox import *
from constantes import style
from Board import Board
from Game import SimpleGame, GeneralGame


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
        self.create_frames_button = tk.Button(self, text="Start",
                                              **style.menu,
                                              command=self.create_frames)
        self.create_frames_button.place(x=760, y=20, width=70, height=25)

    def create_frames(self):
        #se crea una variable frame=None
        frame = 'None'

        # Se verifica que el tamaño y modo de juego hayan sido ingresados sino
        # se muestra un mensaje de error
        if self.entry_board_size.get() != "" and self.modeValue.get() != 'None':

        # Se verifica que el tamaño ingresado sea valido (mayor igual a 3)
        # para que se cree un tablero que sera pasado al juego con el modo
        # que se selecciono. Tambien se crea el frame, en este caso fram2, que
        # contiene el juego
            try:
                #print('a')
                self.create_frames_button.focus_set()
                board = Board(int(self.entry_board_size.get()))
                self.mode(board)
                frame = Container2(self, self)
                self.frames[Container2] = frame

            except ValueError:
                showerror(title='Error', message='Tamaño invalido')
                self.entry_board_size.delete(0, tk.END)
                self.modeValue.set('None')

        else:
            self.entry_board_size.delete(0, tk.END)
            self.modeValue.set('None')
            showerror(title='Error', message='Ingrese un tamaño de tablero y seleccione un modo de juego.')

        # Si frame es diferente de None quiere decir que se creo
        # correctamente el frame2 y se debe mostrar sino sale del metodo
        if frame =='None':
            pass
        else:
            frame.tkraise()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def control(self):
        self.show_frame(Container2)

    def mode(self, board):
        if self.modeValue.get() == 'Simple':
            self.game = SimpleGame(board)
            self.game.set_players('red','blue')
        elif self.modeValue.get() == 'General':
            self.game = GeneralGame(board)
            self.game.set_players('red','blue')
        else:
            self.game = None

    def init_widgets(self):
        # frame1
        self.frame1 = tk.Frame(self, bg=style.beige)
        self.frame1.place(x=0, y=0, width=760, height=60)

        self.modeValue = tk.StringVar()
        self.modeValue.set('None')
        self.simple_game_button = tk.Radiobutton(self.frame1, text="Simple Game", **style.letras, variable=self.modeValue, value='Simple')
        self.simple_game_button.place(x=120, y=20, width=100, height=30)

        self.general_game_button = tk.Radiobutton(self.frame1, text="General Game", **style.letras, variable=self.modeValue, value='General')
        self.general_game_button.place(x=270, y=20, width=100, height=30)

        label_board_size = tk.Label(self.frame1, text='Board size: ', **style.label)
        label_board_size.place(x=500, y=20, width=100, height=20)

        self.entry_board_size = tk.Entry(self.frame1, font=style.arial)
        self.entry_board_size.place(x=600, y=20, width=40, height=20)


class Container2(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(parent)
        self.board = None
        self.container = container
        self.pack()
        self.place(x=0, y=60, width=900, height=600)
        self.configure(bg=style.beige2)
        self.game = self.container.game
        self.init_widgets()
        self.canvas.variable = tk.StringVar()

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
        # self.board guardara el tablero que se inicializo en el juego
        self.board = self.game.get_board()
        self.board_size = self.board.get_board_size()

        frame_width = self.frame_board.winfo_width()
        frame_height = self.frame_board.winfo_height()
        # print(f'frame {frame_width} \ncell')

        #tamano del casillero
        self.cell_size = min(frame_width, frame_height) / self.board_size
        # print(self.cell_size)
        self.canvas_width = self.board_size * self.cell_size
        self.canvas_height = self.board_size * self.cell_size

        #dibuja el tablero
        self.canvas = tk.Canvas(self.frame_board, width=self.canvas_width,
                                height=self.canvas_height)
        self.canvas.place(x=0, y=0)
        self.canvas.variable = None

        # dibuja los rectangulos del tablero y las piezas
        for row in range(self.board_size):
            for col in range(self.board_size):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = (col + 1) * self.cell_size
                y1 = (row + 1) * self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', tags='cell')

                # dibuja las piezas
                self.canvas.tag_bind('cell', '<Button-1>', self.on_cell_clicked)

    def on_cell_clicked(self, event):
        piece = self.select_piece()

        # Si se ha seleccionado una pieza entonces se dibujara en el tablero sino retorna un mensaje de error
        if piece != 'None':
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)

            # Esta division nos indica el indice de la columna en la que el usuario hace click
            col = int(x // self.cell_size)
            row = int(y // self.cell_size)

            print(f'inicio: {self.board.board}')

            # Mientras la celda seleccionada esté ocupada, solicitar al
            # jugador que seleccione otra celda vacía
            while self.board.get_piece(row, col) !='None':
                showinfo(title='Care',message='Casilla Ocupada')
                event = self.canvas.wait_variable(self.canvas.variable)
                x = self.canvas.canvasx(event.x)
                y = self.canvas.canvasy(event.y)
                col = int(x // self.cell_size)
                row = int(y // self.cell_size)

            # Insertamos la pieza en la posicion indicada
            self.board.insert_piece(row, col, piece,self.valueTurn.get())
            # Dibujamos la pieza en la posicion indicada
            self.draw_piece(self.valueTurn.get(), row, col, piece)

            self.win_or_tie(self.valueTurn.get(),row,col)

            print(f'final: {self.board.board}\n{self.valueTurn.get()}')
        else:
            showerror(title='Error',message='Seleccione una pieza')


    def win_or_tie(self,turn,row,col):
        complete, player = self.game.take_turn(turn,row,col)
        print(self.game.type_game())
        if complete == 'Empty Board':
            showinfo(title='Care',message='Continue')
        else:
            if complete == 'Continue':
                print(f'state: {complete}\nplayer:{player}')
                if player != self.game.get_player1():
                    self.valueTurn.set('blue')
                    # Activa las casillas del jugador azul
                    self.s_blue_play.config(state='normal')
                    self.o_blue_play.config(state='normal')
                    self.s_red_play.config(state='disabled')
                    self.o_red_play.config(state='disabled')
                else:
                    self.valueTurn.set('red')
                    # Activa las casillas del jugador rojo
                    self.s_blue_play.config(state='disabled')
                    self.o_blue_play.config(state='disabled')
                    self.s_red_play.config(state='normal')
                    self.o_red_play.config(state='normal')
            elif complete == 'Win':
                showinfo(title='Care',message=f'{player} player win.\nCongratulations!')
            elif complete == 'Tie':
                showinfo(title='Care',message='Tie.\nTry again')

    def select_piece(self):
        if self.select_player_type():
            # Se establece el valor de la pieza que se ha seleccionado
            if (self.redValue.get() == 'S') or (self.blueValue.get() == 'S'):
                piece = 'S'
            elif (self.redValue.get() == 'O') or (self.blueValue.get() == 'O'):
                piece = 'O'
            else:
                piece = 'None'

            self.redValue.set('None')
            self.blueValue.set('None')
            return piece
        else:
            self.redtype.set('None')
            self.bluetype.set('None')
            showerror(title='Error', message='Seleccione el tipo de jugador')

    def select_player_type(self):
        if self.bluetype.get() == 'Human' and self.redtype.get() == 'Human':
            self.computer_blue.config(state='disabled')
            self.computer_red.config(state='disabled')
        elif self.redtype.get() == 'Computer' and self.bluetype.get() == 'Human':
            self.human_red.config(state='disabled')
            self.computer_blue.config(state='disabled')
        elif self.redtype.get() == 'Human' and self.bluetype.get() == 'Computer':
            self.computer_red.config(state='disabled')
            self.human_blue.config(state='disabled')
        elif self.redtype.get() == 'Computer' and self.bluetype.get() == 'Computer':
            self.human_red.config(state='disabled')
            self.human_blue.config(state='disabled')
        else:
            return False
        return True




    def draw_piece(self, valueTurn, row, col, piece):
        if piece == 'S':
            self.board.insert_piece(row, col, piece,valueTurn)
            self.canvas.create_text(
                (col + 0.5) * self.cell_size,
                (row + 0.5) * self.cell_size,
                text='S',
                font=('Arial', 32),
                fill=valueTurn
            )
            if valueTurn == 'red':
                self.s_red_play.deselect()
            elif valueTurn == 'blue':
                self.s_blue_play.deselect()
        elif piece == 'O':
            self.board.insert_piece(row, col, piece,valueTurn)
            self.canvas.create_text(
                (col + 0.5) * self.cell_size,
                (row + 0.5) * self.cell_size,
                text='O',
                font=('Arial', 32),
                fill=valueTurn
            )
            if valueTurn == 'red':
                self.o_red_play.deselect()
            elif valueTurn == 'blue':
                self.o_blue_play.deselect()

    def init_widgets(self):

        # frame blue_player
        self.frame_blue_player = tk.Frame(self, bg=style.beige2)
        self.frame_blue_player.place(x=0, y=0, width=210, height=500)

        # frame tablero
        self.frame_board = tk.Frame(self, bg=style.beige2)
        self.frame_board.place(x=210, y=0, width=480, height=500)
        # print(f'frame {self.frame_board.winfo_width()}')

        # frame red_player
        self.frame_red_player = tk.Frame(self, bg=style.beige2)
        self.frame_red_player.place(x=690, y=0, width=210, height=500)

        # frame turno
        self.frame_turn = tk.Frame(self, bg=style.beige)
        self.frame_turn.place(x=0, y=500, width=900, height=100)

        # #
        # frame blue_player(210x500)
        label_blue_player = tk.Label(self.frame_blue_player, text='Blue Player', **style.blue)
        label_blue_player.place(x=30, y=50, width=100, height=30)

        # tipo de jugador
        self.bluetype = tk.StringVar()
        self.bluetype.set('None')
        self.human_blue=tk.Radiobutton(self.frame_blue_player, text='Human', **style.letras, variable=self.bluetype,
                                       value='Human')
        self.human_blue.place(x=30,y=100,width=100,height=30)
        self.computer_blue = tk.Radiobutton(self.frame_blue_player, text='Computer', **style.letras, variable=self.bluetype,
                                            value='Computer')
        self.computer_blue.place(x=30, y=250, width=100, height=30)
        

        self.blueValue = tk.StringVar()
        self.blueValue.set('None')
        self.s_blue_play = tk.Radiobutton(self.frame_blue_player, text='S', **style.letras, variable=self.blueValue, value='S',
                                          state='disabled')
        self.s_blue_play.place(x=50, y=150, width=100, height=30)
        self.o_blue_play = tk.Radiobutton(self.frame_blue_player, text='O', **style.letras, variable=self.blueValue, value='O', state='disabled')
        self.o_blue_play.place(x=50, y=200, width=100, height=30)

        ##
        # tipo de jugador
        self.redtype = tk.StringVar()
        self.redtype.set('None')
        self.human_red = tk.Radiobutton(self.frame_red_player, text='Human', **style.letras, variable=self.redtype,
                                        value='Human')
        self.human_red.place(x=30, y=100, width=100, height=30)
        self.computer_red = tk.Radiobutton(self.frame_red_player, text='Computer', **style.letras, variable=self.redtype,
                                           value='Computer')
        self.computer_red.place(x=30, y=250, width=100, height=30)

        self.redValue = tk.StringVar()
        self.redValue.set('None')
        self.s_red_play = tk.Radiobutton(self.frame_red_player, text='S', **style.letras, variable=self.redValue, value='S')
        self.s_red_play.place(x=50, y=150, width=100, height=30)
        self.o_red_play = tk.Radiobutton(self.frame_red_player, text='O', **style.letras, variable=self.redValue, value='O')
        self.o_red_play.place(x=50, y=200, width=100, height=30)

        self.replay_button = tk.Button(self.frame_red_player, text='Replay', **style.menu, state='disabled')
        self.replay_button.place(x=50, y=350, width=100, height=40)
        self.new_game_button = tk.Button(self.frame_red_player, text='New Game', **style.menu, state='disabled')
        self.new_game_button.place(x=50, y=400, width=100, height=40)

        # creamos el tablero
        self.after(1000, self.create_board())

        ##
        # frame turn (900x100)
        label_current_game = tk.Label(self.frame_turn, text='Current Turn: ', **style.label)
        label_current_game.place(x=330, y=30, width=80, height=30)

        self.valueTurn = tk.StringVar()
        self.valueTurn.set('red')

        label_turn = tk.Label(self.frame_turn, textvariable=self.valueTurn, **style.label)
        label_turn.place(x=410, y=30, width=50, height=30)




