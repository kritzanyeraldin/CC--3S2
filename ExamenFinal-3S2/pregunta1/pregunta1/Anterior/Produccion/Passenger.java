public class Passenger {

    private String name;
    private boolean vip;

    public Passenger(String name, boolean vip) {    //constructor con parametros name(variable tipo string) y vip(variable tipo boolena)
        this.name = name;
        this.vip = vip;
    }

    public String getName() {
        return name;
    }   //este metodo retorna name

    public boolean isVip() {
        return vip;
    }   //este metodo retorna vip

}
