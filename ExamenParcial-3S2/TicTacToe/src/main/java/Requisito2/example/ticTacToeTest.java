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



}

