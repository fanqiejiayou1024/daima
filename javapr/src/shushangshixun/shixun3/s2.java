package shushangshixun.shixun3;

import java.util.Scanner;

public class s2 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("请输入您的消费金额：");
        int money = scan.nextInt();
        switch (money / 200){
            case 0:
                System.out.println("您已消费：" + money + "元，尚未超过200元须按照小票价格支付全款，即" + money +"元");
                break;
            case 1:
            case 2:
                System.out.println("您已消费：" + money + "元，不少于200元但尚未超过600元，全部的消费金额可享8.5折优惠，即" + (money * 0.85) +"元");
                break;
            case 3:
            case 4:
                System.out.println("您已消费：" + money + "元，不少于600元但尚未超过1000元，全部的消费金额可享7折优惠，即" + (money * 0.7) +"元");
                break;
            default:
                System.out.println("您已消费：" + money + "元，不少于1000元，全部的消费金额可享6折优惠，即" + (money * 0.6) +"元");
                break;
        }
        scan.close();
    }
}
