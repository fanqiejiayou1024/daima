package shushangshixun.shixun6;

public class s2 {
    public static void main(String[] args) {
        int[][] x = { { 12, 7, 3 }, { 4, 5, 6 } };
        int[][] y = { { 5, 8, 1 }, { 6, 7,3 } };
        int[][] r = new int [2][3];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                r[i][j] = x[i][j] + y[i][j];
                System.out.print(r[i][j] + " ");
            }
            System.out.println();
        }
    }
}
