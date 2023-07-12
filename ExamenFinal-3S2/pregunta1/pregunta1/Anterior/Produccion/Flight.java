import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Flight {
    String id;
    private List<Passenger> passengers = new ArrayList<Passenger>();
    private String flightType;

    public Flight(String id, String flightType) {   //constructor con parametros id y tipodevuelo ambas variables de tipo string
        this.id = id;     //inicializa el atributo id
        this.flightType = flightType;   //inicializa el atributo flightype
    }

    public String getId() {
        return id;
    }   //metodo que retorna el atributo flight

    public List<Passenger> getPassengersList() {
        return Collections.unmodifiableList(passengers);     //metodo que retorna una vista no modificable de la lista passengers
    }

    public String getFlightType() {
        return flightType;
    }   //metodo que retorna el atributo flgihtype

    public boolean addPassenger(Passenger passenger) {
        switch (flightType) {
            case "Economico":                       //caso si el vuelo es economico
                return passengers.add(passenger);   //se agrega el pasajero que se paso como referencia
            case "Negocios":                        //caso vuelo negocios
                if (passenger.isVip()) {            //si el pasajero es vip entonces se puede agregar a un vuelo de negocios caso
                    return passengers.add(passenger);   //contrario se retorna false
                }
                return false;
            default:
                throw new RuntimeException("Tipo desconocido: " + flightType); //cualquier otro caso se imprime que tipo desconocido de vuelo
        }

    }

    public boolean removePassenger(Passenger passenger) {
        switch (flightType) {
            case "Economico":                               //caso: vuelo es economico
                if (!passenger.isVip()) {                   //si el pasajero no es vip se remueve de la lista
                    return passengers.remove(passenger);
                }
                return false;
            case "Negocios":                                //caso: vuelo es de negocios
                return false;                               //no se remueve a nadie
            default:
                throw new RuntimeException("Tipo desconocido: " + flightType);
        }
    }

}
