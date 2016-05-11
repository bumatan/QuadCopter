package com.company;

public class Main {

    public static void main(String[] args) {

        Client client = new Client("49.50.10.93" , 8080);

        new Thread(client).start();

    }
}
