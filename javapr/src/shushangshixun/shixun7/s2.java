package shushangshixun.shixun7;

import java.util.*;

public class s2 {
    public static void main(String[] args) {
        List<String> shelf = new ArrayList<>();
        shelf.add("《三国演义》");
        shelf.add("《莎士比亚诗选》");
        shelf.add("《红楼梦》");
        System.out.println("书架上的书籍：" + shelf);
        List <String> desk = new ArrayList <String>();
        desk.add("《西游记》");
        desk.add("《水浒传》");
        System.out.println("书桌上的书籍：" + desk);
        shelf.addFirst(desk.get(1));
        shelf.set(2,desk.get(0));
        System.out.print("中国的四大名著分别是：");
        for(int i = 0; i < shelf.size(); i++) {
            System.out.print(shelf.get(i) + " ");
        }
    }
}
