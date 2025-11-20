package shushangshixun.shixun3;

import java.util.Scanner;

public class s1 {
    public static void main(String[] arge){
        float x,y;
        Scanner scan = new Scanner(System.in);
        System.out.println("«Î ‰»ÎX£∫");
        x = scan.nextFloat();
        if (x <= 0.0){
            y = 0.0f;
        } else if (x < 10.0) {
            y = 1.0f / x;
        }else {
            y = 1.0f;
        }
        System.out.println("y = " + y);
        scan.close();
    }
}
