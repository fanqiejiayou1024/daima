package shushangshixun.shixun6;
public abstract class s4 {
    public static void main(String[] args) {
        String str = "1a2b3c";
        char[] c = str.toCharArray();
        for (char item : c) {
            if (item >= '0' && item <= '9')
                System.out.print(item + " ");
        }
        System.out.println();
        for (char value : c) {
            if ((value >= 'A' && value <= 'Z') || (value >= 'a' && value <= 'z'))
                System.out.print(value);
        }
    }
}