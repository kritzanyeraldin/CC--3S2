package Requisito2.example;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


class ticTacToeTest {
    private static ticTacToe ticTacToe;
    @BeforeAll
    public static void init(){
        ticTacToe = new ticTacToe();
    }

    @Test
    public void whenPieceOutsideX() {
        assertThrows(RuntimeException.class, () -> ticTacToe.jugar(5, 2));
    }

    @Test
    public void whenPieceOutsideY(){
        assertThrows(RuntimeException.class,()->ticTacToe.jugar(2,5));
    }

    @Test
    public void whenPlaceIsBussy(){
        ticTacToe.jugar(1,3);

        assertThrows(RuntimeException.class, () -> ticTacToe.jugar(1,3));
    }
    @Test
    public void primerJugador(){
        char primerJugador= ticTacToe.proximoJugador();
        assertEquals('X',primerJugador);
    }

    @Test
    public void OsiguienteJugador(){
        // X realiza una jugada
        ticTacToe.jugar(1,1);

        char segundoJugador = ticTacToe.proximoJugador();
        // Verficar que el siguiente jugador sea O
        assertEquals('O', segundoJugador);
    }

    @Test
    public void XsiguienteJugador(){
        ticTacToe.jugar(1, 1);
        ticTacToe.jugar(1,2);

        // Verificar que el siguiente jugador sea 'X'
        assertEquals('X', ticTacToe.proximoJugador());
    }

    @Test
    public void noHayGanador() {

        assertEquals(ticTacToe.obtenerGanador(), '\0');
    }

    @Test
    public void verificarHorizontal(){
        ticTacToe.jugar(1,1);
        ticTacToe.jugar(2,1);
        ticTacToe.jugar(1,2);
        ticTacToe.jugar(2,2);
        ticTacToe.jugar(1,3);

        assertEquals(ticTacToe.obtenerGanador(),'X');
    }

    @Test
    public void verificarVertical(){
        ticTacToe.jugar(1,1);
        ticTacToe.jugar(1,2);
        ticTacToe.jugar(2,1);
        ticTacToe.jugar(3,2);
        ticTacToe.jugar(3,1);

        assertEquals(ticTacToe.obtenerGanador(),'X');
    }

    @Test
    public void verificarPrimeraDiagonal(){
        ticTacToe.jugar(1,1);
        ticTacToe.jugar(1,2);
        ticTacToe.jugar(2,2);
        ticTacToe.jugar(3,2);
        ticTacToe.jugar(3,3);

        assertEquals(ticTacToe.obtenerGanador(),'X');
    }

    @Test
    public void verificarSegundaaDiagonal(){
        ticTacToe.jugar(1,3);
        ticTacToe.jugar(1,2);
        ticTacToe.jugar(2,2);
        ticTacToe.jugar(3,2);
        ticTacToe.jugar(3,1);

        assertEquals(ticTacToe.obtenerGanador(),'X');
    }

}

