package shushangshixun.shixun8;

import java.util.*;

public class s1 {
    public static void main(String[] args){
        double l = 1023.79;
        Scanner s = new Scanner(System.in);
        System.out.println("请输入取款金额");
        try {
            int d = s.nextInt();
            double r = l - d;
            if(r >= 0){
                System.out.println("您账户的余额：" + r + "元");
            }else{
                System.out.println("您账户的余额不足！");
            }
        }
        catch(Exception e){
            System.out.println("您输入的取款金额不是整数！");
        }finally{
            s.close();
        }
    }
}
