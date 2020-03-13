package pc;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Index {
    final static int PORT = 1346;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("IP address: ");
        bw.flush();
        final String ADDRESS = br.readLine();

        Boat boat = null;
        try {
            boat = new Boat(ADDRESS, PORT);
            boat.connect();
            startKeyboardInput(boat);
        } catch (Exception e) {
            bw.write(e.getMessage());
            boat.close();
        }
        finally{}
    }

    public static void startKeyboardInput(Boat boat) {
        while(true) {
            
        }
    }
}

class Boat {
    final int PORT;
    final String ADDRESS;

    Socket socket = null;

    public Boat(String address, int port) {
        ADDRESS = address;
        PORT = port;
    }

    public void connect() throws IOException {
        socket = new Socket(ADDRESS, PORT);
    }

    public void close() throws IOException {
        socket.close();
    }

    public void control() {

    }
}