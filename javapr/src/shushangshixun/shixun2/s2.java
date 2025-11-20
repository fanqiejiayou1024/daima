package shushangshixun.shixun2;

public class s2 {
    final static int A = 1,B = 2;
    final static double C = 3;
    public static void main(String[] args){
        double x = (A + C) * B / C;
        System.out.println("x的值为: " + x);
        boolean y = A > B | B > C & C > A;
        System.out.println("y的值为: " + y);
        int a = A + B;
        int b = ++a;
        int c = a++;
        System.out.println("b的值为: " + b + '\t' + "c的值为: " + c);
    }
}
