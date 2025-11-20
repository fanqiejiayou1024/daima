package shushangshixun.shixun6;

public class s1 {
    public static void main(String[] args) {
        int[] a = { 52, 12, 51, 13, 19, 83, 8, 2 };
        int k;
        int t = 0;
        for (k = 0; k < a.length; k++) {
            if(a[k] % 2 == 1) {
                break;
            }
            t += a[k];
        }
        System.out.println(t);
    }
}
