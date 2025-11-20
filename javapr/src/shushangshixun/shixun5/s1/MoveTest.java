package shushangshixun.shixun5.s1;
public class MoveTest {
	public static void main(String[] args) {
		Move s = new Student("同学");
		Move t = new Teacher("老师");
		s.talk();
		t.talk();
		t.work();
		s.work();
	}
}
