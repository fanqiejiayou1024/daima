/* ComputeRootTest.java*/
package chapter4.practice4_4;
public class ComputeRootTest {
	public static void main(String[] args) {
		ComputeRoot y1, y2;				// 声明对象
		y1 = new ComputeRoot(1, 5, 10);		// 使用有参构造方法创建对象
		y1.showRoot();					// 调用showRoot方法
		y2 = new ComputeRoot(1, 10, 9);
		y2.showRoot();

	}

}
class ComputeRoot {
	double x1, x2;
	private double a, b, c;
	// 带参数构造方法初始化成员变量
	public ComputeRoot(double a, double b, double c) {		
		this.a = a;
		this.b = b;
		this.c = c;
	}
// 计算方程实根的方法
	void real_root(double delt) {
		x1 = (-b + Math.sqrt(delt)) / (2 * a);
		x2 = (-b - Math.sqrt(delt)) / (2 * a);
		System.out.println("delt>=0，方程的实根为\nx1=" + x1);	// 输出方程的实根
		System.out.println("x2=" + x2);
	}
	// 计算方程虚根的方法
	void imag_root(double delt) {
		double real, imag;
		real = (-b) / (2 * a);
		imag = Math.sqrt(-delt) / (2 * a);
		System.out.println("delt<0，方程的虚根为\nx1=" + real + "+" + imag + "i");
		System.out.println("x2=" + real + "-" + imag + "i");
	}
	// 根据判别式delt的值，选择调用的方法
	void showRoot() {
		double delt = b * b - 4 * a * c;
		if (delt >= 0)
			real_root(delt);
		else
			imag_root(delt);
	}
}
