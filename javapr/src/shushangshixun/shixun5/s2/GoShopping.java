package shushangshixun.shixun5.s2;
public class GoShopping {
	public static void main(String[] args) {
		Market market = new WuMeiMarket("物美", "牙膏");
		market.shop();
		market = new JDMarket("京东", "手机");
		market.shop();
	}
}
