package SOLVED;
import java.util.Scanner;

public class P2588 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        int m = stdIn.nextInt();

        System.out.println(n * (m % 10));
        System.out.println(n * (m % 100 / 10));
        System.out.println(n * (m / 100));
        System.out.println(n * m);

        stdIn.close();
    }
}
