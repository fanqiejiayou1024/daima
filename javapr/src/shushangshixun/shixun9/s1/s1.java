package shushangshixun.shixun9.s1;
import java.io.*;
import java.util.*;
public class s1 {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.println("请输入要写入的文件名： ");
        String f  =s.nextLine();
        String[] c = { "对酒当歌", "人生几何", "譬如朝露", "去日苦多", "慨以当康", "忧思难忘", "何以解忧", "唯有杜康" };
        FileWriter fw = null;
        try {
            fw = new FileWriter(f,true);
            for (int i = 0;i < c.length;i++){
                fw.write(c[i] + "\n");
            }
            fw.close();
        }catch (IOException e){
            e.printStackTrace();
        }
        s.close();
    }
}
