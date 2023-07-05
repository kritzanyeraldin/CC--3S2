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

Ahora creamos un contenedor con l aimagen creada con volumen 

![Texto alternativo](imagenes/p2/5.png)
![Texto alternativo](imagenes/p2/6.png)

y si quisieramos saber lo que contiene la etiqueta config.label ejecutamos docker inspect

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

Modificamos el archivo ControladorBase de la siguietne forma

![Alt text](imagenes/p3/12.png)

Antes de correr el proyecto agregaremos una dependencia al pom.xml llamada thymeleaf. Luego cargamos de nuevo el proyecto e importamos en la clase ControladorBase la libreria que permite el uso de Model

![Alt text](imagenes/p3/13.png)

![Alt text](imagenes/p3/16.png)

Ahora si corremos el proyecto y no deberia salir errores

![Alt text](imagenes/p3/14.png)

Ingresamo a http://localhost:8080/ nuevamente y nos aparece el texto que se retorna en el metodo index

![Alt text](imagenes/p3/15.png)

Agregamos codigo a index.mustache

![Alt text](imagenes/p3/17.png)

### Parte3

Ejecutamos el proyecto nuevamente

![Alt text](imagenes/p3/18.png)

Ingresamos a http://localhost:8080/ nuevamente y nos aparece el texto que se retorna en el metodo index. En este caso modifique el codigo para que retornara model.toString()

![Alt text](imagenes/p3/19.png)

## Parte 4

Vamos a proceder a crear clases para cada controlador. 
Primero crearemos la clase Video

![Alt text](imagenes/p3/20.png)

## Parte 5

Luego creamos una clase VideoServices en la cual se creara una lista de Videos

![Alt text](imagenes/p3/19.png)

## Parte 6 y Parte 7

Actualizamos la clase de ControladorBase para comenzar a usar la nueva clase que creamos.
Se creo una variable de clase VideoServices y se usa @Autowired para inyectar una dependecia en este caso la variable VideoServices en el constructor de la clase ControladorBase

![Alt text](imagenes/p3/21.png)

Como notamos tambien se actualiza el metodo index. Cambiamos el tipo a ModelandView y retornamos el mapeo de los videos que hay en la lista videos aplicando la plantilla index

![Alt text](imagenes/p3/22.png)

Ahora procedemos a ejecutar el proyecto e Ingresamos a http://localhost:8080/ para ver el listado de los videos

![Alt text](imagenes/p3/23.png)

![Alt text](imagenes/p3/24.png)

### Parte 8
Agregamos lo siguiente a index.mustache

![Alt text](imagenes/p3/25.png)

### Parte 9
Escribimos un nuevo metodo el cual llama a newVideo de la clase VideoServices

![Alt text](imagenes/p3/27.png)

y llamamos a ese metodo en nuevo video. Procedemos a correrlo

![Alt text](imagenes/p3/26.png)

Al correr el proyecto nos sale un formulario en el cual podemos ingresar el nuevo video

![Alt text](imagenes/p3/28.png)

Pero al apretar el boton de submit vemos que aparece un error 

![Alt text](imagenes/p3/29.png)

El error que se genera en consola es UnsupportedOperationException.

![Alt text](imagenes/p3/30.png)

Este error se produce ya que la lista que se esta usando es List.of

### Parte 10
 Vamos a crear una clase crear de tipo Video, dentro de esta se crea una lista extend que es una copia de la lista de videos existente y agregaremos a ella un nuevo video luego se crea una lista inmutable basada en extend que es asignado a videos y lo retornamos

 ![Alt text](imagenes/p3/31.png)

 Luego modificamos la clase ControladorBase en PostMapping  nuevo video para que se agregue el video que ingresaremos en el form y nos redireccione a "/" en la cual se muestra la lista de videos actualizada

  ![Alt text](imagenes/p3/32.png)

Ejecutamos el proyecto e ingresamos a http://localhost:8080/

![Alt text](imagenes/p3/33.png)

Ingresamos nuevo video en el form y apretamos el boton el cual guarda el nuevo video y nos redirige a "/" donde se mostrara la lista actualizada

![Alt text](imagenes/p3/34.png)

![Alt text](imagenes/p3/35.png)

Creamos una clase ControladorApi en cual trabajaremos sin plantillas. Creamos una variable privada de tipo VideoService y la inicializamos en el constructor luego en el metodo all obtenemos todos los videos en videos.
Estos se deberian mostrar en  http://localhost:8080/api/videos al correr el proyecto

![Alt text](imagenes/p3/36.png)

![Alt text](imagenes/p3/37.png)


### Parte 11





## PREGUNTA 4

La automatización de infraestructura en la arquitectura de microservicios se refiere a la automatización del proceso de aprovisionamiento, configuración y gestión de la infraestructura necesaria para ejecutar y mantener los microservicios en producción. Se utilizan herramientas y técnicas para automatizar tareas por ejemplo: la creación de máquinas virtuales, la configuración de redes, la gestión de contenedores. Tambien permite gestionar de manera eficiente la infraestructura para admitir tanto implementacion como ejecucion de multiple microservicios idependientemente. Tambien permite una tolerancia a fallos, de esta forma contribuye a la estabilidad del sistema





















