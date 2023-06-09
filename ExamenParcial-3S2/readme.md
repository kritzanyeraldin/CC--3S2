# Examen Parcial

## Pregunta 1 Solid Y refactorizacion

### Antes de refactorizar

Creamos primero la clase `Member` que será abstracta y la cual extenderemos
en nuestras siguientes subclases: `PremiumMember`, `VipMember` y `FreeMember`.

Esta clase `Member` posee un atributo `name` y dos métodos `joinTournament` y
`organizeTournament`.
    
![Member](imagenes/p1/1.png)
    
Luego creamos nuestras tres clases `PremiumMember`, `VipMember` y `FreeMember`
las cuales extenderán de la clase base `Member` y definirá sus métodos utilizando
el decorador `@Override`.

Pero hay un problema, la clase `FreeMember` no puede organizar torneos, lo cual
significa que no puede definir el método `organizeTournament` (esto rompe LSP).

![Member](imagenes/p1/2.png)

![Member](imagenes/p1/3.png)

![Member](imagenes/p1/4.png)

![Member](imagenes/p1/5.png)

### Después de refactorizar

Por lo tanto, vamos a cambiar el enfoque. Definiremos la habilidad de organizar
torneos como una interfaz de manera que podamos implementarlo o no en nuestras clases
de forma modular, de la siguiente manera.

Vamos a crear una interfaz llamada `TournamentOrganizer` que declarará el método
`organizeTournament`.

![Member](imagenes/p1/6.png)

Y ahora vamos a refactorizar nuestra clase `Member`, que solo el atributo `name` y
el método `joinTournament`.

![Member](imagenes/p1/7.png)

Luego refactorizamos nuestras subclases implementando la interfaz creada donde sea necesaria.

![Member](imagenes/p1/8.png)

![Member](imagenes/p1/9.png)

![Member](imagenes/p1/10.png)

## Pregunta 2
Empezamos implementando pruebas para limitar los valores en el eje X

![Member](imagenes/p2/Requisito1//2.png)

Finalmente estas serian todas la pruebas
![Member](imagenes/p2/Requisito1//1.png)

Realizamos la prueba para asegurarnos que el primero juagador siempre sea X
![Member](imagenes/p2/Requisito2//1.png)

Ahor su implementacion el cual sera un simple return 'X' y pasa la prueba
![Member](imagenes/p2/Requisito2//2.png)

Realizamos la prueba en el cual el siguiente jugador sea O 
![Member](imagenes/p2/Requisito2//3.png)

En la implementacion crearemos una variable ultimoJugador que se inicializara en el constructor como 'O' por defecto.El metodo proximo Jugador verificara si ultimojugador es igual a X pues se actualiza y pasa a ser O sino retorna X como ultimo jugador
![Member](imagenes/p2/Requisito2//4.png)

Vemos que pasa la prueba
![Member](imagenes/p2/Requisito2//5.png)

El hecho de crear la prueba que verifique que despues de O siga X es innecesario por que no se implementa nada nuevo en el metodo creado anteriormente simplemente redundamos la implementacion. Es por eso que es preferible eliminarla
![Member](imagenes/p2/Requisito2//6.png)

# Requisito 3

Realizamos la prueba en la cual no exista ganador 
![Member](imagenes/p2/Requisito2//8.png)

En su implementacion agregaremos una variable ganador en el constructor el cual se inicializara vacio '\0' el metodo ObtenerGanador simplemente lo retornara
![Member](imagenes/p2/Requisito2//10.png)
Vemos que pasa la prueba
![Member](imagenes/p2/Requisito2//9.png)

Empezaremos a realizar las diversas condiciones para determinar si hay un ganador

Realizamos una prueba que verifique si se obtiene un ganador cuando se completa una fila con la misma pieza
![Member](imagenes/p2/Requisito2//11.png)

Hacemos su implementacion la cual verificara lo dicho anteriormente
![Member](imagenes/p2/Requisito2//12.png)

Realizamos una prueba que verifique si se obtiene un ganador cuando se completa una columna con la misma pieza
![Member](imagenes/p2/Requisito2//13.png)

Hacemos la implementacion
![Member](imagenes/p2/Requisito2//14.png)

Realizamos una prueba para verficar la primera diagonal
![Member](imagenes/p2/Requisito2//15.png)
![Member](imagenes/p2/Requisito2//16.png)

Realizamos una prueba para verificar la segunda diagonal
![Member](imagenes/p2/Requisito2//17.png)
![Member](imagenes/p2/Requisito2//18.png)








# Pregunta 3 
## Tomare el Sprint 1 de mi proyecto y realizare RGB
Primero creamos una clase Board

 Ahora lo que queremos es crear un prueba donde el tablero tenga un tamaño valido 3<=n y se inserte
![Member](imagenes/p3/1.png)

El terminal muestra que no existen test por que aun no se implementado tamañoValido. Asi que procedemos a implementar el metodo

![Member](imagenes/p3/2.png)

Ahora haremos una prueba donde se cree un tablero 3x3 y tiene que estar vacio

![Member](imagenes/p3/3.png)

Procedemos a realizar la implementacion para que se cree un tablero vacio de nxn. Vemos que pasa la prueba

![Member](imagenes/p3/4.png)

Ahora realizaremos una prueba para insertar una pieza valida, es decir que solo se permita inserta S u O en una casilla valida.

Empezaremos por realizar la prueba para insertar una pieza valida en una casilla invalida.Trataremos de insertar en la posicion (3,2) una ficha valida 'O'.
Se espera que el resultado sea: Coordenadas fuera del rango del tablero.
![Member](imagenes/p3/5.png)

Procedemos a realizar la implementacion y vemos que pasa prueba
![Member](imagenes/p3/6.png)

Ahora realizamos una prueba para insertar una pieza invalida, es decir que no sea de tipo string. Trataremos de insertar en la posicion (0,0) una pieza 4 o sea no es de tipo string. El resultado esperado es: 'La pieza deber ser de tipo string.

![Member](imagenes/p3/7.png)

Procedemos a realizar la implementacion y vemos que pasa prueba
![Member](imagenes/p3/8.png)

Ahora realizamos una prueba para insertar una pieza invalida, es decir la pieza solo puede S u O. Intentaremos insertar un pieza 'W' en la poscion (0,0) el resultado espera es: Pieza no valida

![Member](imagenes/p3/9.png)

Procedemos a realizar la implementacion y vemos que pasa prueba
![Member](imagenes/p3/10.png)

Realizamos una prueba pra insertar una pieza valida en una casilla ocupada.
Intentaremos insertar una pieza valida en una casilla valida pero que ya ha sido ocupada. El resultado esperado es: 'Casilla Ocupada'

![Member](imagenes/p3/11.png)

Procedemos a realizar la implementacion y vemos que pasa prueba
![Member](imagenes/p3/12.png)

