package wenjingketang;

public class t3_2 {
    public static void main(String[] args) {
        int k = 2,i = 0,count = 0;
        while (k <= 100) {
            i = 2;
            while (i <= k-1) {
                if (k % i == 0)
                    break;
                i ++;
            }
            if (i == k) {
                System.out.print(k + " ");
                count ++;
                if (count % 5 ==0)
                    System.out.print("\n");
            }
            k++;
        }
    }
}
