package org.example;

public class PremiumMember extends Member implements TournamentOrganizer{
    public PremiumMember(String nombre) {
        super(nombre);
    }

    @Override
    public void joinTournament() {
        System.out.println("...");
    }

    @Override
    public void organizeTournament() {
        System.out.println("...");
    }

}