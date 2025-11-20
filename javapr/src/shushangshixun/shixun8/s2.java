package shushangshixun.shixun8;

import java.util.*;

class OverflowException extends Exception{
    public OverflowException(double w){
        System.out.println("异常提示：商品的重量为" + w + "斤，超过3斤了，超重了！！！");
    }
}
public class s2 {
    public static void pay(double w) throws OverflowException {
        if (w > 30){
            throw new OverflowException(w);
        }
        double m = w * 3.98;
        System.out.println(m);
    }
    public static void main(String[] args){
        System.out.println("请输入商品的重量（斤）：");
        Scanner s = new Scanner(System.in);
        double w = s.nextDouble();
        try {
            pay(w);
        }catch(OverflowException e) {

        }finally{
            s.close();
        }
    }
}
