package Requisito1.example;

public class ticTacToe {
    private char[][] board;

    public ticTacToe() {
        board = new char[3][3];
    }

    public void jugar(int row, int col) {
        if (row < 1 || row > 3) {
            throw new RuntimeException("Pieza fuera de los limites en el eje X");
        }

        if (col<1 || col>3){
            throw new RuntimeException("Pieza fuera de los limites en el eje Y");
        }

        if(this.board[row-1][col-1]!= '\0'){
            throw new RuntimeException("La casilla esta ocupada");
        }

        this.board[row-1][col-1]='X';
    }

}
