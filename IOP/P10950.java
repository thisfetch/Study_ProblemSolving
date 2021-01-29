package IOP;
import java.util.Scanner;

public class P10950 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n, a, b;
        n = stdIn.nextInt();

        for (int i = 0; i < n; i++) {
            a = stdIn.nextInt();
            b = stdIn.nextInt();
            System.out.println(a + b);
        }
        stdIn.close();
    }
}