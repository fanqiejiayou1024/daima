package shushangshixun.shixun9.s2;
import java.io.*;
public class s2 {
    public static void main(String[] args)throws IOException{
        File f = new File("test.txt");
        FileOutputStream fs = new FileOutputStream(f, true);
        for (int i = 1; i <= 5; i++) {
            String str = "第" + i + "行\n";
            fs.write(str.getBytes());
        }
        fs.flush();
        fs.close();
    }
}
