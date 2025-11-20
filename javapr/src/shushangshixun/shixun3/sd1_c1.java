package shushangshixun.shixun3;

import java.util.Scanner;

public class sd1_c1 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("请输入一个整数 (1~20)：");
        int num = scan.nextInt();
        System.out.println(num + "的阶乘为：" + factorial(num));
    }
    public static long factorial(int n) {
       if (n == 1) {
            return 1;
       }
       return n * factorial(n - 1);
    }
}
