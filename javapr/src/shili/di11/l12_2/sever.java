package shili.di11.l12_2;
import java.io.*;
import java.net.*;
public class sever {
    public static void main(String[] args) {
        ServerSocket se = null;
        Socket so;
        String re = null;
        String sen = null;
        DataOutputStream out = null;
        DataInputStream in = null;
        try {
            se = new ServerSocket(80);
        } catch (IOException e) {
            e.printStackTrace();
        }try {
            so = se.accept();
            in = new DataInputStream(so.getInputStream());
            out= new DataOutputStream(so.getOutputStream());
            for (int i = 0; i < 4; i++) {
                re = in.readUTF();
                System.out.println("服务器收到您的信息：" + re);
                sen = "您好，您发送的信息是："+ re;
                System.out.println("服务器发送信息：" + sen);
            }
            in.close();
            out.close();
            so.close();
            se.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
