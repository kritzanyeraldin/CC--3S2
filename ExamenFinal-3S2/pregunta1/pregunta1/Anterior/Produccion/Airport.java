public class Airport {

    public static void main(String[] args) {
        Flight economyFlight = new Flight("1", "Economico");   //se instancia economyFlight como flight
        Flight businessFlight = new Flight("2", "Negocios");    //se instancia businessFlight como flight

        Passenger cesar = new Passenger("Cesar", true);     //se instancia cesar como passenger
        Passenger jessica = new Passenger("Jessica", false);    //se instancia jessica como paseenger

        businessFlight.addPassenger(cesar);     //se agrega el pasajero cesar a vuelo bussenesflight
        businessFlight.removePassenger(cesar);  //se remueve el pasajero cesar del vuelo businessflight
        businessFlight.addPassenger(jessica);   //se agrega la pasajera jesisca al vuelo bussinesflight
        economyFlight.addPassenger(jessica);    //se agrega la pasajera jessica al vuelo economyfligth

        System.out.println("Lista de pasajeros de vuelos de negocios:");
        for (Passenger passenger : businessFlight.getPassengersList()) {    //recorre la lista de pasajeros del vuelo businessflight
            System.out.println(passenger.getName());
        }

        System.out.println("Lista de pasajeros de vuelos economicos:");
        for (Passenger passenger : economyFlight.getPassengersList()) { //recorer la lsita de pasjeros de vuelo economyflight
            System.out.println(passenger.getName());
        }
    }
}
