package SOLVED;
import java.util.Scanner;

public class P10952 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a, b;
        do {
            a = stdIn.nextInt();
            b = stdIn.nextInt();
            if (a == 0 && b == 0) {
                break;
            } else {
                System.out.println(a + b);
            }
        } while(a != 0 && b != 0);
        stdIn.close();
    }
}
