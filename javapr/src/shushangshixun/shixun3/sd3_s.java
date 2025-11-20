package shushangshixun.shixun3;
import java.util.Scanner;
public class sd3_s {
    public static void main(String[] args){
        int[] a = new int[10];
        Scanner s = new Scanner(System.in);
        //输入
        System.out.println("请输入十个正整数");
        for (int i = 0;i < 10;i++){
            a[i] = s.nextInt();
        }
        //计算并输出
        for (int i = 0;i < 10;i++){
            if(a[i] % 9 == 0){
                System.out.println(a[i]);
                break;
            }else if (i > 10){
                System.out.println("不存在");
            }
        }
        s.close();
    }
}
