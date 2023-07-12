import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AirportTest {
    @DisplayName("Dado que hay un vuelo economico")
    @Nested
    class EconomyFlightTest {

        private Flight economyFlight;
        private Passenger jessica;
        private Passenger cesar;

        @BeforeEach
        void setUp() {
            economyFlight = new EconomyFlight("1");
            jessica = new Passenger("Jessica", false);
            cesar = new Passenger("Cesar", true);
        }

        @Test
        public void testEconomyFlightRegularPassenger() {


            assertEquals("1", economyFlight.getId());
            assertEquals(true, economyFlight.addPassenger(jessica));
            assertEquals(1, economyFlight.getPassengersList().size());
            assertEquals("Jessica", economyFlight.getPassengersList().get(0).getName());

            assertEquals(true, economyFlight.removePassenger(jessica));
            assertEquals(0, economyFlight.getPassengersList().size());
        }

        @Test
        public void testEconomyFlightVipPassenger() {


            assertEquals("1", economyFlight.getId());
            assertEquals(true, economyFlight.addPassenger(cesar));
            assertEquals(1, economyFlight.getPassengersList().size());
            assertEquals("Cesar", economyFlight.getPassengersList().get(0).getName());

            assertEquals(false, economyFlight.removePassenger(cesar));
            assertEquals(1, economyFlight.getPassengersList().size());
        }

    }

    @DisplayName("Dado que hay un vuelo negocios")
    @Nested
    class BusinessFlightTest {
        private Flight businessFlight;
        private Passenger jessica;
        private Passenger cesar;

        @BeforeEach
        void setUp() {
            businessFlight = new BusinessFlight("2");
            jessica = new Passenger("Jessica", false);
            cesar = new Passenger("Cesar", true);
        }

        @Test
        public void testBusinessFlightRegularPassenger() {


            assertEquals(false, businessFlight.addPassenger(jessica));
            assertEquals(0, businessFlight.getPassengersList().size());
            assertEquals(false, businessFlight.removePassenger(jessica));
            assertEquals(0, businessFlight.getPassengersList().size());

        }

        @Test
        public void testBusinessFlightVipPassenger() {

            assertEquals(true, businessFlight.addPassenger(cesar));
            assertEquals(1, businessFlight.getPassengersList().size());
            assertEquals(false, businessFlight.removePassenger(cesar));
            assertEquals(1, businessFlight.getPassengersList().size());

        }

    }

    @DisplayName("Dado que hay un vuelo premium")
    @Nested
    class PremiumFlightTest {
        private PremiumFlight premiumFlight;
        private Passenger jessica;
        private Passenger cesar;

        @BeforeEach
        void setUp() {
            premiumFlight = new PremiumFlight("3");
            jessica = new Passenger("Jessica", false);
            cesar = new Passenger("Cesar", true);
        }

        @Nested
        @DisplayName("Cuando tenemos un pasajero regular")
        class RegularPassenger {

            @Test
            @DisplayName("No puedes agregarlo o  eliminarlo de un vuelo premium")
            public void testPremiumFlightRegularPassenger() {
                assertAll(
                        () -> assertEquals(false, premiumFlight.addPassenger(jessica)),
                        () -> assertEquals(0, premiumFlight.getPassengersList().size()),
                        () -> assertEquals( false , premiumFlight.removePassenger(jessica)),
                        () -> assertEquals(0, premiumFlight.getPassengersList().size())
                );
            }
        }

        @Nested
        @DisplayName("Cuando tenemos un pasajero VIP")
        class VipPassenger {

            @Test
            @DisplayName("Se puede agregar y eliminar de un vuelo premium")
            public void testPremiumFlightVipPassenger() {
                assertAll(
                        () -> assertEquals(true, premiumFlight.addPassenger(cesar)),
                        () -> assertEquals(1, premiumFlight.getPassengersList().size()),
                        () -> assertEquals(true, premiumFlight.removePassenger(cesar)),
                        () -> assertEquals(0, premiumFlight.getPassengersList().size())
                );
            }
        }


    }

}