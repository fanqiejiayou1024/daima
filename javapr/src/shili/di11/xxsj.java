package shili.di11;
import java.awt.*;
import java.awt.event.*;
public class xxsj extends Frame implements ActionListener{
    TextField age = new TextField(4);
    TextField name = new TextField(100);

    Choice nat = new Choice();

    CheckboxGroup sex = new CheckboxGroup();

    Checkbox man = new Checkbox("男",true,sex);
    Checkbox woman = new Checkbox("女",false,sex);
    Checkbox like0001 = new Checkbox("看小说");
    Checkbox like0002 = new Checkbox("上网");
    Checkbox like0003 = new Checkbox("学习");

    List web = new List(6);

    Button btnOK = new Button("确认");
    Button btnCancel = new Button("取消");
    Button btnQuit = new Button("退出");

    Label label = new Label("个人信息调查表");
    Label Name = new Label("姓名");
    Label Sex = new Label("性别");
    Label Age = new Label("年龄");
    Label Nat = new Label("籍贯");
    Label Like = new Label("爱好");
    Label Web = new Label("喜欢的网站");

    public xxsj(String ti){

        super(ti);
        setSize(400,400);
        setLayout(null);

        label.setBounds(150,50,100,20);
        Name.setBounds(50,100,40,20);
        name.setBounds(90,100,100,20);
        Sex.setBounds(230,100,40,20);
        man.setBounds(270,100,60,20);
        woman.setBounds(330,100,60,20);
        Age.setBounds(50,150,40,20);
        age.setBounds(90,150,50,20);
        Nat.setBounds(230,150,40,20);
        nat.setBounds(270,150,60,20);
        Like.setBounds(50,200,40,20);
        like0001.setBounds(90,200,60,20);
        like0002.setBounds(150,200,60,20);
        like0003.setBounds(210,200,100,20);
        Web.setBounds(50,250,80,20);
        web.setBounds(130,250,100,60);
        btnOK.setBounds(110,330,50,20);
        btnCancel.setBounds(180,330,50,20);
        btnQuit.setBounds(250,330,50,20);

        nat.add("北京");
        nat.add("上海");
        nat.add("深圳");
        nat.add("广州");
        nat.add("杭州");
        nat.add("昆明");
        nat.add("武汉");
        nat.add("南京");
        nat.add("成都");
        nat.add("重庆");
        nat.add("天津");
        nat.add("苏州");
        nat.add("长沙");
        nat.add("青岛");
        nat.add("西安");
        nat.add("郑州");
        nat.add("宁波");
        nat.add("无锡");
        nat.add("大连");
        web.add("github");
        web.add("csdn");
        web.add("哔哩哔哩");
        web.add("知乎");
        web.add("嘉立创");
        web.add("立创商城");
        web.add("立创开发版");
        web.add("bing");
        web.add("捷配");
        web.add("msdn");
        web.add("小黑课堂");
        web.add("淘宝");
        web.add("京东");
        web.add("天猫");

        add(label);
        add(Name);
        add(name);
        add(Sex);
        add(man);
        add(woman);
        add(Age);
        add(age);
        add(Nat);
        add(nat);
        add(Like);
        add(like0001);
        add(like0002);
        add(like0003);
        add(Web);
        add(web);
        add(btnOK);
        add(btnCancel);
        add(btnQuit);

        setLocationRelativeTo(null);
        setVisible(true);

        btnOK.addActionListener(this);
        btnCancel.addActionListener(this);
        btnQuit.addActionListener(this);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object ob = e.getSource();
        if (ob == btnQuit){
            System.exit(0);
        }else if (ob == btnOK){

            String s1 = like0001.getState() ? like0001.getLabel() + " " : " ";
            String s2 = like0002.getState() ? like0002.getLabel() + " " : " ";
            String s3 = like0003.getState() ? like0003.getLabel() + " " : " ";

            System.out.println("姓名：" + name.getText());
            System.out.println("性别：" + sex.getSelectedCheckbox().getLabel());
            System.out.println("年龄：" + age.getText());
            System.out.println("籍贯：" + nat.getSelectedItem());
            System.out.println("爱好：" + s1 + s2 + s3);
            System.out.println("喜欢的网站：" + web.getSelectedItem());
        } else if (ob == btnCancel) {
            name.setText("");
            sex.setSelectedCheckbox(man);
            age.setText("18");
            like0001.setState(false);
            like0002.setState(false);
            like0003.setState(false);
            web.deselect(web.getSelectedIndex());
        }
    }

    public static void main(String[] args) {
        new xxsj("个人信息");
    }
}