package org.example;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
public class CalculatorTest {
    private static Calculadora calculadora;
    @BeforeAll
    public static void init(){
        calculadora = new Calculadora();
    }
    @Test
    public void whenCalculatorInitializedThenReturnTrue(){
        assertTrue(calculadora.getStatus());
    }
    @Test
    public void whenAdditionTwoNumberThenReturnCorrectAnswer() {
        assertEquals( 5, calculadora.addition(2,3));
    }
    @Test
    public void whenRestTwoNumberThenReturnCorrectAnswer() {
        assertEquals( 1, calculadora.rest(3,2));
    }
    @Test
    public void whenDivisionThenReturnCorrectAnswer() {
        assertEquals(2, calculadora.division(8, 4));
    }
    @Test
    public void whenDivisionByZeroThenThrowException() {
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
            calculadora.division(5, 0);
        });
        assertEquals("No se puede divisor por  cero", exception.getMessage());
    }
}
