package Requisito2.example;

public class ticTacToe {
    private char[][] board;
    private char ultimoJugador;
    private char ganador;

    public ticTacToe(){
        board = new char[3][3];
        ultimoJugador='O';
        ganador = '\0';

    }

    public void jugar(int row, int col){
        validarLimites(row,col);
        validarCasillaVacia(row,col);
        insertarPieza(row, col, proximoJugador());
        ultimoJugador = proximoJugador();
        verificarGanador(row, col);

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

    public char proximoJugador(){
        if (ultimoJugador == 'X') {
            return 'O';
        } else if (ultimoJugador == 'O') {
            return 'X';
        } else {
            return 'X'; // Retorna 'X' si el último jugador es diferente a 'X'
        }
    }

    public char getUltimoJugador() {
        return ultimoJugador;
    }

    private void verificarGanador(int row, int col) {
        // Verificar líneas horizontales
        if (board[row-1][0] == board[row-1][1] && board[row-1][0] == board[row-1][2]) {
            ganador = board[row-1][0];
            return;
        }

        // Verificar líneas verticales
        if (board[0][col-1] == board[1][col-1] && board[0][col-1] == board[2][col-1]) {
            ganador = board[0][col-1];
            return;
        }

        // Verificar diagonal principal
        if (row == col && board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
            ganador = board[0][0];
            return;
        }

        // Verificar diagonal secundaria
        if (row + col == 4 && board[0][2] == board[1][1] && board[0][2] == board[2][0]) {
            ganador = board[0][2];
            return;
        }

    }


    public char obtenerGanador() {
        return ganador;

    }

}
