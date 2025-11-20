package shushangshixun.shixun6;
public abstract class s3 {
	public static void main(String[] args) {
		String[] product= new String[] { "华为手机", "三星手机",
				"格力空调", "小米电视", "华为电脑", "美的吸尘器",
				"华为路由器", "海尔电热水器", "华为智能体脂秤" };
		int sum = 0;
		for (int i = 0; i < product.length; i++) {
			String name = product[i];
			if (name.startsWith("华为")) {
				sum++;
			}
		}
		System.out.println("华为品牌的电器共有" + sum + "种");
	}
}
