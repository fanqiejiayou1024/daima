package shushangshixun.shixun7;

import java.util.*;

public class s1 {
    public static void main(String[] args){
        Set<Integer> set = new TreeSet<>();
        set.add(10);
        set.add(15);
        set.add(20);
        set.add(10);
        set.add(18);
        set.add(Integer.valueOf(15));
        System.out.println("size = " + set.size());
        Iterator<Integer> it = set.iterator();
        while (it.hasNext()){
            System.out.print(it.next() + " ");
        }
    }
}
