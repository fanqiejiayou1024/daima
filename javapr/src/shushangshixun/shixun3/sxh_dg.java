package shushangshixun.shixun3;

public class sxh_dg {
    public static void main(String[] args){
        int x = 100;
        s(x);
    }
    public static int s(int y){
        if(y != 1000){
            int b = 0,s = 0,g = 0;
            b = y / 100;
            s = y / 10 % 10;
            g = y % 10;
            if (Math.pow(b,3) + Math.pow(s,3) + Math.pow(g,3) == y){
                System.out.println(y);
            }
            return s(y + 1);
        }
        return 0;
    }
}
