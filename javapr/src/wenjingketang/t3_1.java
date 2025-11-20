package wenjingketang;

import java.util.Scanner;

public class t3_1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double[] a = new double[3];
        //输入
        for (int i = 0; i < 3; i++) {
            a[i] = s.nextDouble();
        }
        //运算及输出
        if ((a[0] + a[1]) > a[3] & (a[0] + a[2]) > a[1] & (a[1] + a[2]) > a[0]) {
            double S = (a[0] + a[1] + a[2]) / 2;
            double Area = Math.sqrt(S * (S - a[0]) * (S - a[1]) * (S - a[2]));
            System.out.println("三角形的面积为" + Area);
        }
        else{
            System.out.println("边长为" + a[0] +"、" + a[1] + "、" + a[2] + "的三条边不能组成三角形");
        }
    }
}