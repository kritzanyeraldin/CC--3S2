## Practica Calificada 5

### Pregunta 2
Copiamos el texto del dockerfile de la pregunta 2 y guardamos

![Texto alternativo](imagenes/p2/2.png)

Entramos al cmd y corremos el dockerfile para poder contruir la imagen de alpine. Para comprobar si se creo correctamente escribimos el comando
```(powersheell)
docker images
```

![Texto alternativo](imagenes/p2/1.png)

Corremos un contenedor con la imagen creada. Y comprobamos si esta corriendo con 
```(powersheell)
docker ps
```

![Texto alternativo](imagenes/p2/3.png)

Si ingresamos a http://localhost:8080/ nos muestra lo siguiente

![Texto alternativo](imagenes/p2/4.png)

a

![Texto alternativo](imagenes/p2/5.png)
![Texto alternativo](imagenes/p2/6.png)

a

![Texto alternativo](imagenes/p2/7.png)

Ahora descargaremos una imagen de docker hub. En este caso sera la de alpine la ultima version que se tenga. Comprobamos si se ha creado la imagen

![Texto alternativo](imagenes/p2/8.png)

Luego creamo un contenedor de nombre alpine-test e ingresamos a el con -it /bin/sh. Y ejecutamos ciertos comandos que instalaran NGINX

![Texto alternativo](imagenes/p2/9.png)

Ejecutamos la siguiente linea la cual detiene el contenedor alpine-test y crea una imagen de el con el nombre my-repo

![Texto alternativo](imagenes/p2/10.png)

Verificamos si se creo la imagen

![Texto alternativo](imagenes/p2/11.png)

Luego lo guardamos la imagen 

![Alt text](imagenes/p2/12.png)

Ahora crearemos un nuevo dockerfile para crear la imagen de alpine desde scratch

![Alt text](imagenes/p2/13.png)

Construimos la imagen a partir del dockerfile y comprobamos si se creo correctamente

![Alt text](imagenes/p2/14.png)

Podemos observar que pesa menos que la imagen creada anteriormente la cual se llama alpine

![Alt text](imagenes/p2/15.png)

Finalmente, creamos un contenedor con la imagen fromscratch e ingresamos a ella con -it 

![Alt text](imagenes/p2/16.png)


### Pregunta 3

Ingresamos a https://start.spring.io/ y selecionamos los datos agregamos la dependecia de Spring Web y generamos el proyecto el cual se descargara en un archivo ZIP lo descomprimimos y abrimos el archivo con intellij 

![Alt text](imagenes/p3/1.png)

![Alt text](imagenes/p3/2.png)

Checamos la depencia en el pom.xml

![Alt text](imagenes/p3/3.png)

### parte 1

Comenzamos creando la clase ControladorBase de la siguiente forma

![Alt text](imagenes/p3/4.png)


¿Qué crees que significan @Get Mapping @Controller, index?
@RestController: Nos indica que la clase es un controlador REST, o sea respondera a solicitudes HTTP y devolvera datos en formato xml o Json en lugar de html como se solia hacer  

@Get Mapping: Nos indica que el metodo index() hara manejo de las solicitudes HTTP GET a la ruta que se le especifica en este caso '/'
 
 index: Es el metodo que realiza la solicitud get a la ruta "/api". El cual devuelve el texto "index"
 

Corremos el codigo principal 

![Alt text](imagenes/p3/5.png)

Ahora ingresamos a http://localhost:8080/ y nos deberia aparecer el texto "index"

![Alt text](imagenes/p3/6.png)

Ahora generamos un nuevo proyecto agregando la dependencia Mustache

![Alt text](imagenes/p3/7.png)

Abrimos el archivo en intellij y nos fijamos las dependencias en el pom.xml

![Alt text](imagenes/p3/8.png)

## parte 2

Creamos el archivo index.mustache en el apartado de /templates del proyecto

![Alt text](imagenes/p3/9.png)

Luego procedemos a correr el proyecto 

![Alt text](imagenes/p3/10.png)

Ingresamos a http://localhost:8080/ nuevamente y se debe mostrar la plantilla creada

![Alt text](imagenes/p3/11.png)





