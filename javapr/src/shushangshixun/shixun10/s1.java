package shushangshixun.shixun10;

import java.beans.IntrospectionException;

public class s1 extends Thread{
    public void run(){
        for (int i = 1; i <= 10; i++) {
            System.out.println("Êý×Ö" + i);
            try {
                sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args){
        s1 t = new s1();
        t.start();
    }
}
