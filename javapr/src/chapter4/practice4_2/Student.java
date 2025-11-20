/* Student.java */
package chapter4.practice4_2;
//导入chapter4.practice4_2.math.ComputeMaxMin类
//import chapter4.practice4_2.math.ComputeMaxMin; //编程训练（3）取消注释

public class Student {
	String sNo;
	String sName;
	char sSex;
	int sAge;
	double sJava;
	// 定义有参构造方法，初始化成员变量
	Student(String sNo, String sName, char sSex, int sAge, double sJava) {
		this.sNo = sNo;
		this.sName = sName;
		this.sSex = sSex;
		this.sAge = sAge;
		this.sJava = sJava;
	}
	String getNo( ) {				// 获取学号
		return sNo;
	}
	String getName( ) {				// 获取姓名
		return sName;
	}
	char getSex( ) {				// 获取性别
		return sSex;
	}
	int getAge( ) {					// 获取年龄
		return sAge;
	}
	double getJava( ) {				// 获取Java课程成绩
		return sJava;
	}
	// 显示学生信息
	public void display() {
		System.out.println("学号：" + sNo + " " + "姓名：" + sName + " " + "性别：" + sSex + " " + "年龄：" + sAge + " " + "Java课程成绩：" + sJava);
	}
	public static void main(String[] args) {
		// 创建对象并初始化对象
		Student s1 = new Student("001", "张一", '男', 18, 80);
		Student s2 = new Student("002", "李二", '女', 19, 75.5);
		Student s3 = new Student("003", "刘三", '女', 20, 90);
		Student s4 = new Student("004", "赵四", '男', 18, 88);
		Student s5 = new Student("005", "钱五", '男', 20, 70);
		s1.display();				// 调用display方法
		s2.display();
		s3.display();
		s4.display();
		s5.display();
		// 创建ComputeMaxMin类对象并初始化对象，编程训练（3）取消下面注释
		/*ComputeMaxMin c= new ComputeMaxMin(s1.sJava, s2.sJava, s3.sJava, s4.sJava, s5.sJava);
		System.out.println("Java课程成绩最大值：" + c.max());// 调用max方法并输出Java课程成绩最大值
		System.out.println("Java课程成绩最小值：" + c.min());// 调用min方法并输出Java课程成绩最小值*/

	}
}
