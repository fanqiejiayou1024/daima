/* EncryptTest.java */
package chapter4.practice4_1;
import java.util.Scanner;
class Encrypt {
	int code;
	Encrypt(int code) {
		this.code = code;
	}
	int encryptCode() {
		int qw = code / 1000;						// 取千位数
		int bw = (code - qw *1000) / 100;				// 取百位数
		int sw = (code - qw *1000 - bw * 100) / 10;		// 取十位数
		int gw = code % 10;						// 取个位数
		qw = (qw + 5) % 10;						// 千位数加5除以10
		bw = (bw + 5) % 10;						// 百位数加5除以10
		sw = (sw + 5) % 10;						// 十位数加5除以10
		gw = (gw + 5) % 10;						// 个位数加5除以10
		int temp;									// 定义中间量
		// 第一位和第四位交换
		temp = qw;
		qw = gw;
		gw = temp;
		// 第二位和第三位交换
		temp = bw;
		bw = sw;
		sw = temp;
		// 返回加密后的四位整数
		return qw * 1000 + bw * 100 + sw * 10 + gw;
	}
}
public class EncryptTest {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("请输入一个四位整数：");
		int code = scan.nextInt();		// 扫描为int型数据并赋值给code
		Encrypt c = new Encrypt(code);	// 创建Encrypt类的对象
		System.out.println("加密后的四位整数为：" + c.encryptCode());
		scan.close();					// 关闭扫描器
	}
}
