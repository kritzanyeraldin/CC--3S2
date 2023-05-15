package org.example;

public class FreeMember extends Member {
    public FreeMember(String name) {
        super(name);
    }
    @Override
    public void joinTournament() {
        System.out.println("...");
    }
    //Este método rompe LSP
/*
    @Override
    public void organizeTournament() {
        System.out.println("...");
    }
*/
}