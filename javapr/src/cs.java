public class cs {
    public static void main(String[] args) {
        //计算pi的10000位
        double pi = 0;
        for (int i = 0; i < 10000; i++) {
            pi += Math.pow(-1, i) / (2 * i + 1);
        }
        pi *= 4;
        System.out.println(pi);
        //计算pi的1000000000000000000位
        pi = 0;
        for (long i = 0; i < 1000000000; i++) {
            pi += Math.pow(-1, i) / (2 * i + 1);
        }
        pi *= 4;
        System.out.println(pi);
    }
}
