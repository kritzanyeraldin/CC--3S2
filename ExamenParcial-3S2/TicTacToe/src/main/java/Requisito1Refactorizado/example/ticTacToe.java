package Requisito1Refactorizado.example;

public class ticTacToe {
    private char[][] board;

    public ticTacToe(){
        board = new char[3][3];
    }

    public void jugar(int row, int col){
        validarLimites(row,col);
        validarCasillaVacia(row,col);
        insertarPieza(row,col,'X');
    }

    public void validarLimites(int row, int col){
        if ((row<1 || row>3) || (col<1 || col>3)){
            throw new RuntimeException("Pieza fuera de los limites.");
        }
    }

    public void validarCasillaVacia(int row,int col){
        if(this.board[row-1][col-1]!= '\0') {
            throw new RuntimeException("La casilla esta ocupada");
        }
    }

    public void insertarPieza(int row, int col, char pieza){
        board[row-1][col-1]=pieza;
    }
}
