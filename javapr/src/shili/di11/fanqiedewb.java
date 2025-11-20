package shili.di11;
import java.awt.*;
import java.io.*;
import java.awt.event.*;
import javax.management.StringValueExp;
import javax.swing.*;
public class fanqiedewb extends  JFrame implements  ActionListener{
    JMenuBar m;
    JMenu file;
    JMenuItem nw,op,cl,sf,ex;
    JTextArea tx;
    public fanqiedewb(String t){
        super(t);
        setSize(400,400);
        setLocationRelativeTo(null);
        me();
        tx = new JTextArea();
        add(tx);
        setVisible(true);
    }
    private void me() {
        m = new JMenuBar();
        file = new JMenu("file");
        nw =  new JMenu("new");
        op =  new JMenu("open");
        cl =  new JMenu("close");
        sf =  new JMenu("sava");
        ex =  new JMenu("exit");
        file.add(nw);
        file.add(op);
        file.add(cl);
        file.add(sf);
        file.add(ex);
        m.add(file);
        setJMenuBar(m);
        nw.addActionListener(this);
        op.addActionListener(this);
        cl.addActionListener(this);
        sf.addActionListener(this);
        ex.addActionListener(this);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        Object ob = e.getSource();
        JFileChooser f = new JFileChooser();
        if ((ob == nw) || (ob == cl)){
            tx.setText("");
        }else if (ob == op){
            f.showOpenDialog(this);
            try {
                StringBuffer s = new StringBuffer();
                FileReader in = new FileReader(f.getSelectedFile());
                while (true){
                    int b = in.read();
                    if (b == -1){
                        break;
                    }
                    s.append((char) b);
                }
                tx.setText(s.toString());
                in.close();
            } catch (Exception e1) {
            }
        }else if (ob == sf){
            f.showOpenDialog(this);
            try {
                FileWriter out = new FileWriter(f.getSelectedFile());
                out.write(tx.getText());
                out.close();
            }catch (Exception e2){
            }
        }else if (ob == ex){
            System.exit(0);
        }
    }
    public static void main(String[] args){
        new fanqiedewb("fanqieµÄÎÄ±¾±à¼­Æ÷");
    }
}