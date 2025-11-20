package wenjingketang;

import java.util.Scanner;

public class t2_1 {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int bw = 0,sw = 0,gw = 0;
        bw = a / 100;
        sw = a / 10 % 10;
        gw = a % 10;
        System.out.print(gw);
        System.out.print(sw);
        System.out.print(bw);
        s.close();
    }
}
