package IOP;
import java.util.Scanner;

public class P11021 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        int a, b;
    
        for (int i = 1; i <= n; i++) {
            a = stdIn.nextInt();
            b = stdIn.nextInt();
            System.out.println("Case #" + i +": " + (a + b));
        }
        stdIn.close();
    }
}
