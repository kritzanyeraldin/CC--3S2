import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PremiumFlight{
    private String id;
    private List<Passenger> passengers = new ArrayList<Passenger>();
    public PremiumFlight(String id) {
        this.id=id;
    }

    public List<Passenger> getPassengersList() {
        return Collections.unmodifiableList(passengers);
    }
    public boolean addPassenger(Passenger passenger) {
        if(passenger.isVip()){
            return passengers.add(passenger);
        }
        return false;
    }

    public boolean removePassenger(Passenger passenger) {

            return passengers.remove(passenger);

    }



}

