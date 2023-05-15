package org.example;

public class VipMember extends Member implements TournamentOrganizer{
    public VipMember(String nombre) {
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
