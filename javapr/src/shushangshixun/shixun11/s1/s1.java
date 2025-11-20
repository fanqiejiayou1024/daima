package shushangshixun.shixun11.s1;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class s1 extends JFrame{
    public static void main(String[] args){
        s1 f = new s1();
        f.setLocationRelativeTo(null);
        f.setVisible(true);
    }
    public s1(){
        setResizable(false);
        setTitle("j");
        setSize(220,300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container c = getContentPane();
        c.setLayout(new GridLayout(1,0,0,0));
        JPanel i = new JPanel();
        i.setBackground(Color.WHITE);
        c.add(i);
        i.setLayout(new BorderLayout(0, 0));
        JLabel l = new JLabel("");
        l.setBackground(Color.WHITE);
        l.setIcon(new ImageIcon(s1.class.getResource("im/green.png")));
        i.add(l, BorderLayout.CENTER);

        JPanel btnPanel = new JPanel();
        c.add(btnPanel);
        btnPanel.setLayout(null);
        JRadioButton rbtnRed = new JRadioButton("ºìµÆ");
        rbtnRed.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                l.setIcon(new ImageIcon(s1.class.getResource("im/red.png")));
            }
        });
        rbtnRed.setBounds(20, 51, 60, 20);
        btnPanel.add(rbtnRed);
        JRadioButton rbtnYellow = new JRadioButton("»ÆµÆ");
        rbtnYellow.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                l.setIcon(new ImageIcon(s1.class.getResource("im/yellow.png")));
            }
        });
        rbtnYellow.setBounds(20, 117, 60, 20);
        btnPanel.add(rbtnYellow);

        JRadioButton rbtnGreen = new JRadioButton("ÂÌµÆ");
        rbtnGreen.setSelected(true);
        rbtnGreen.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                l.setIcon(new ImageIcon(s1.class.getResource("im/green.png")));
            }
        });
        rbtnGreen.setBounds(20, 182, 60, 20);
        btnPanel.add(rbtnGreen);
        ButtonGroup group = new ButtonGroup();
        group.add(rbtnRed);
        group.add(rbtnYellow);
        group.add(rbtnGreen);
    }
}
