package shushangshixun.shixun4;

public class s2 {
    public static void main(String args[]) {
        RectConstructor rect1 = new RectConstructor(10, 20);
        double ar;
        ar = rect1.area();
        System.out.println("长方形的面积是" + ar);
    }
}
class RectConstructor {
    private double length;
    private double width;
    double area() {
        return length * width;
    }
    RectConstructor(double width, double length) {
        this.length = length;
        this.width = width;
    }
}


