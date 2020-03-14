package pc;

import java.io.IOException;
import java.net.Socket;

class Boat {
    final private int PORT;
    final private String ADDRESS;
    private int voltage;
    private Socket socket = null;

    public Boat(String address, int port) {
        ADDRESS = address;
        PORT = port;
    }

    /**
    *    connect to boat with IP address and Port
    */
    public void connect() throws IOException {
        socket = new Socket(ADDRESS, PORT);
    }

    /**
     * Close the socket connection
     * @throws IOException
     */
    public void close() throws IOException {
        socket.close();
    }

    public void control() {
        
    }

    public int getVoltage() {
        /* TODO 볼트 얻는 코드 추가 */
        return voltage;
    }
}