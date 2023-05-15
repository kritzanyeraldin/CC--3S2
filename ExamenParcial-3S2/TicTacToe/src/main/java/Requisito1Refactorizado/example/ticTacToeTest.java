package Requisito1Refactorizado.example;

import Requisito1.example.ticTacToe;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertThrows;

class ticTacToeTest {
    private static Requisito1.example.ticTacToe ticTacToe;
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

}

