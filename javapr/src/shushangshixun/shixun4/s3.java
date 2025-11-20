package shushangshixun.shixun4;
public class s3 {
    public static void main(String[] args) {
        int leftOilVolume = 10;
        GasStation gs = new GasStation();
        for (int i = 1; i <= 5; i++) {
            leftOilVolume = gs.addOil(leftOilVolume);
        }
        System.out.println("该车现有油量：" + leftOilVolume + "L");
    }
}
class GasStation {
    public int addOil(int oilVolume) {
        oilVolume += 2;
        return oilVolume;
    }
}
