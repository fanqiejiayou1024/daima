/*ComputeMaxMin.java*/
package chapter4.practice4_2.math;
public class ComputeMaxMin {
	double num1, num2, num3, num4, num5;
	// 定义有参构造方法，并初始化成员变量
	public ComputeMaxMin(double num1, double num2, double num3, double num4, double num5) {
		this.num1 = num1;
		this.num2 = num2;
		this.num3 = num3;
		this.num4 = num4;
		this.num5 = num5;
	}
	public double max() {			// 定义方法计算最大值
		double max;
		max = Math.max(num1, num2);// 调用Math类中max方法计算两个数的较大值
		max = Math.max(max, num3);
		max = Math.max(max, num4);
		max = Math.max(max, num5);	
		return max;					// 返回最大值
	}
	public double min() {				// 定义方法计算最小值
		double min;
		min = Math.min(num1, num2);// 调用Math类中的min方法计算两个数的较小值
		min = Math.min(min, num3);
		min = Math.min(min, num4);
		min = Math.min(min, num5);	
		return min;					// 返回最小值
	}
}
