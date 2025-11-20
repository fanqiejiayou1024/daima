package shili.d7;

import java.util.*;

public class l7_8 {
    public static void main(String[] args){
        //创建
        HashMap<String,Integer> m = new HashMap<String,Integer>();
        //调用put
        m.put("a",20000);
        m.put("b",99999999);
        m.put("c",20097700);
        m.put("awwwww",2003300);
        m.put("bjhsjhscjhcs",99999);
        //输入对象
        Scanner s = new Scanner(System.in);
        //打断条件
        String jx;
        while (true) {
            //输出
            System.out.println("=====请选择存取款=====");
            System.out.println("1.存款         2.取款");
            System.out.println("请选择：");
            //输入
            int see = s.nextInt();
            //存或取
            if (see == 1) {
                System.out.println("请输入账户名和存款金额(用半角逗号隔开)");
            } else if (see == 2) {
                System.out.println("请输入账户名和取款金额(用半角逗号隔开)");
            }
            //输入
            String acc = s.next();
            String[] sAcc = acc.split(",");
            if (m.containsKey(sAcc[0])){
                Integer mo = m.get(sAcc[0]);
                if (see == 1){
                    mo += Integer.parseInt(sAcc[1]);
                } else if (see == 2) {
                    mo -= Integer.parseInt(sAcc[1]);
                }
                System.out.println(sAcc[0] + "账户余额为" + mo + "元");
                System.out.println("还需要存款或取款吗？（用y或者n）");//T or F
                jx = s.next();
            } else {
                System.out.println("该账户不存在！");
                break;
            }
            if (jx == "n"){
                break;
            }
        }
        s.close();
    }
}