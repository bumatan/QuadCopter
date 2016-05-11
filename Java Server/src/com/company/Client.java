package com.company;

import java.io.*;
import java.net.Socket;

/**
 * Created by Daniel on 11/05/2016.
 */
public class Client implements Runnable {

    private int port ;
    private String ip ;

    private Socket socket ;
    private ObjectInputStream input ;
    private ObjectOutputStream output ;

    private boolean isRunnig = true ;

    public Client(String ip, int port){
        this.port = port ;
        this.ip = ip ;

    }

    //Start connection .


    @Override
    public void run() {

        while (isRunnig) {

            setSocket();
            setStreams();
            whileConnected();

        }
    }

    //Set The Socket Connection .
    private void setSocket(){
        try {
            socket = new Socket(ip,port);
            System.out.println("Connected");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //Set The Streams .
    private void setStreams(){

        try {
            output = new ObjectOutputStream(socket.getOutputStream());
            output.flush();

            input = new ObjectInputStream(socket.getInputStream());

            System.out.println("All Streams Are Set !");

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    //While we connected
    private void whileConnected(){
        String message = "hello matan !" ;
        sendData(message);

        System.out.println("Data Sent");
    }

    //Send Data
    public void sendData(String data){

        try {

            output.writeUTF(data);
            output.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    //Stop the connection .
    public void stop(){
        isRunnig = false ;
    }


}
