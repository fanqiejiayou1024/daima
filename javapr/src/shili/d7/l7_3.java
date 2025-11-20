package shili.d7;

import java.util.*;

public class l7_3 {
    public static void main(String[] args) {
        System.out.println("姓名 签到时间");
        ArrayList<String> listEmployee = new ArrayList<String>();
        listEmployee.add("杨朝来 8：25");
        listEmployee.add("蒋平 8：29");
        listEmployee.add("马达 8：35");
        listEmployee.add("丁健 8：31");
        listEmployee.add("王丹 9：00");
        for (int i = 0;i < listEmployee.size();i++){
            System.out.println(listEmployee.get(i));
        }
    }
}
