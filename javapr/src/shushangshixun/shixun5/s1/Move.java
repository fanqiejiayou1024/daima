package shushangshixun.shixun5.s1;
public interface Move {
	public void work();
	public void talk();
}
class Student implements Move {
	public String name;
	public Student(String name) {
		this.name = name;
	}
	@Override
	public void work() {
		System.out.println(name + "：开始记笔记");
	}
	@Override
	public void talk() {
		System.out.println(name + "：老师好");
	}
}
class Teacher implements Move {
	public String name;
	public Teacher(String name) {
		this.name = name;
	}
	@Override
	public void work() {
		System.out.println(name + "：开始上课");
	}
	@Override
	public void talk() {
		System.out.println(name + "：同学们好");
	}
}
