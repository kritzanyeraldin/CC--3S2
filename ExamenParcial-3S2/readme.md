# Examen Parcial

## Pregunta 1 Solid Y refactorizacion

### Antes de refactorizar

Creamos primero la clase `Member` que será abstracta y la cual extenderemos
en nuestras siguientes subclases: `PremiumMember`, `VipMember` y `FreeMember`.

Esta clase `Member` posee un atributo `name` y dos métodos `joinTournament` y
`organizeTournament`.
    
![Member](imagenes/1.png)
    
Luego creamos nuestras tres clases `PremiumMember`, `VipMember` y `FreeMember`
las cuales extenderán de la clase base `Member` y definirá sus métodos utilizando
el decorador `@Override`.

Pero hay un problema, la clase `FreeMember` no puede organizar torneos, lo cual
significa que no puede definir el método `organizeTournament` (esto rompe LSP).

![Member](imagenes/2.png)

![Member](imagenes/3.png)

![Member](imagenes/4.png)

![Member](imagenes/5.png)

### Después de refactorizar

Por lo tanto, vamos a cambiar el enfoque. Definiremos la habilidad de organizar
torneos como una interfaz de manera que podamos implementarlo o no en nuestras clases
de forma modular, de la siguiente manera.

Vamos a crear una interfaz llamada `TournamentOrganizer` que declarará el método
`organizeTournament`.

![Member](imagenes/6.png)

Y ahora vamos a refactorizar nuestra clase `Member`, que solo el atributo `name` y
el método `joinTournament`.

![Member](imagenes/7.png)

Luego refactorizamos nuestras subclases implementando la interfaz creada donde sea necesaria.

![Member](imagenes/8.png)

![Member](imagenes/9.png)

![Member](imagenes/10.png)
