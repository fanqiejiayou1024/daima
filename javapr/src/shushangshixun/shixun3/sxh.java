package shushangshixun.shixun3;

//水仙花数
public class sxh {
    public static void main(String[] args){
        for (int i = 100;i < 1000;i++){
            int b = 0,s = 0,g = 0;
            b = i / 100;
            s = i / 10 % 10;
            g = i % 10;
            if (Math.pow(b,3) + Math.pow(s,3) + Math.pow(g,3) == i){
                System.out.println(i);
            }
        }
    }
}