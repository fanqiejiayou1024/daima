package javajiaqizhuoye.d7;

import java.util.*;

public class bc1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        char[] arr = s.toCharArray();
        //字符数组排序
        Arrays.sort(arr);
        //去重
        Set<Character> set = new HashSet<>();
        for (char c : arr) {
            set.add(c);
        }
        char[] uniqueArray = new char[set.size()];
        int index = 0;
        for (char c : set) {
            uniqueArray[index++] = c;
        }
        //输出
        for (char c : uniqueArray) {
            System.out.print(c + " ");
        }
        scan.close();
    }
}
