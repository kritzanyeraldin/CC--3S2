## PREGUNTA 1
### fase 1 
En la fase1 al compilar con cobertura no se obtiene el 100% ya que al instanciar el busineesFlight se nombra a su atributo flitghtipo business. Cuando se ejecuta el código el método addPassenger va a la excepción de vuelo de tipo desconocido. Una refactorizacion sería cambiar el tipo de vuelo a Negocios o Económico ya que son los 2 tipos de vuelo que existen hasta ahora.

### fase 2
Se agrega una interfaz llamada fligth
En la fase 2 a comparación de la fase 1 la clase flight pasa a ser una clase abstracta y contiene atributos y metodos de un vuelo en general por ejemplo el id. También se crean las clases BusinessFlight y EconomyFlight que extienden de la clase flight ambas tiene el método agregar pasajeros y remover pasajero. Estos serán modificado con las condiciones que se establecieron dependiendo del tipo de vuelo . En AirportTest se puede nota que en la linea 18 primero se instancia economyflight como fligth y luego instancia como EconomyFlight. Realizado esto se especifica que
tipo de vuelo es y que métodos se deben usar.

Con esta refactorizacion se logra eliminar el campo flightType ya que ya no es significativo y crear por separado clases de vuelos que extiendan de uno general. Se logra modular un poco mas que en la fase 1.

Esta refactorizacion, de la fase 1 a la fase 2, mejoro la calidad del codigo testAirport ya que ahora se logra en la mayoria el 100% y en otras no baja de 70% 

### fase 3
Se agrega el tipo de vuelo premium sin extender de flight posee sus metodos con las politicas establecidas. Tambien se agregan sus pruebas unitarias en el archivo AirportTest el cual el porcentaje es muy bajo comparado a la fase 2 baja el min de 70% a 33% 

### fase4

Ahora haremos que premium flight extienda de flight y sobreescribiremos sus metodos por el momento con false pasamos a crear las pruebas unitarias y luego rellenamos dichos metodos para que pueda pasar las pruebas establecidas. al correr las pruebas con cobertura nos damos cuenta que ahora si corren al 100% esto es por la refactorizacion que se hizo 

### fase5
Cambiamos el tipo de la lista de pasajeros a HashSet para que se conserve la unicidad del pasajero. Lo que hace que tambien se cambie el metodo addpassenger ya que ahora trabajamos con otro tipo de lista. Tambien se modifica las pruebas. Mejora la cobertura en las pruebas la mayoria obtiene un 100%, pero no bajan de 90%.
