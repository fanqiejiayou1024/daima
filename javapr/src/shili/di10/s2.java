package shili.di10;
class m implements Runnable {
    public void run(){
        for(int i = 0;i < 10;i++){
            System.out.println(i + " ");
        }
    }
}
public class s2 {
    public void main(String[] args){
        m mt = new m();
        Thread t1 = new Thread(mt);
        t1.start();
    }
}
