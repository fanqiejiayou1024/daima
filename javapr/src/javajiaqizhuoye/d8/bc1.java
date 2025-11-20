package javajiaqizhuoye.d8;

import java.util.*;

public class bc1{
    public static void main(String[] args){
        HashMap<String, String> mapCourse = new HashMap<>();
        // 调用put()方法将员工信息键值对添加到mapEmployee中
        mapCourse.put("吕红", "数据库");
        mapCourse.put("周婷", "线性代数");
        mapCourse.put("肖扬", "Java");
        mapCourse.put("李娟", "数据库");
        mapCourse.put("丁锦", "英语");
        mapCourse.put("周玲玲", "Java");
        mapCourse.put("赵红", "Java");
        mapCourse.put("周玲玲", "Python");
        System.out.println("********课程安排信息********");
        Iterator<String> it = mapCourse.keySet().iterator();
        while (it.hasNext()) {
            String key = it.next();
            String val = mapCourse.get(key);
            System.out.println("教师：" + key + "，课程:" + val);
        }
        System.out.println("******所有讲授Java的教师******");
        it = mapCourse.keySet().iterator();
        while (it.hasNext()) {
            String key = it.next();
            String val = mapCourse.get(key);
            if (val.equals("Java"))
                System.out.print(key + " ");
        }
    }
}