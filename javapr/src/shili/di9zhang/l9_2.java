package shili.di9zhang;

import java.io.*;

public class l9_2 {
    public static void main(String[] args) {
        try {
            FileOutputStream fos;
            fos = new FileOutputStream("FileStreamTest.txt");
            String data = "人们常觉得准备的阶段是在浪费时间，\n" + "只有当真正机会来临，而自己没有能力把握的时候，\n" + "才能觉悟自己平时没有准备才是浪费了时间。\n" + "——罗曼.罗兰";
            byte[] outData = data.getBytes();
            fos.write(outData);
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            FileInputStream fis;
            fis = new FileInputStream("FileStreamTest.txt");
            byte[] inData = new byte[1024];
            int len = fis.read(inData);
            String outString = new String(inData, 0, len);
            System.out.println(outString);
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}