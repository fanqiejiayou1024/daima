package shili.di11.l12_2;
import java.awt.*;
import java.io.*;
import java.net.Socket;
import javax.swing.*;

public class khd extends JFrame {
    JTextArea ta = new JTextArea();
    public khd(String title) {
        super(title);
        setSize(430, 250);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container c = getContentPane();
        c.add(ta);
        setVisible(true);
    }
    public void transmit() {
        ta.append("准备连接……\n");
        try {
            String recvInfo = null;
            String sendInfo = null;
            Socket socket;
            DataInputStream in = null;
            DataOutputStream out = null;
            socket = new Socket("localhost", 80);
            ta.append("完成连接……\n");
            in = new DataInputStream(socket.getInputStream());
            out=new DataOutputStream(socket.getOutputStream());
            for (int i = 0; i < 4; i++) {
                sendInfo = String.valueOf(Math.random());
                out.writeUTF(sendInfo);
                ta.append("客户端发送：" + sendInfo + "\n");
                Thread.sleep(1000);
                recvInfo = in.readUTF();
                ta.append("客户端收到：" + recvInfo + "\n");
            }
            out.close();
            in.close();
            socket.close();
        } catch (IOException e) {
            System.out.println("无法连接");
        } catch (InterruptedException e) {
        }
    }
    public static void main(String[] args) {
        khd myClient = new khd("客户端");
        myClient.transmit();
    }
}
