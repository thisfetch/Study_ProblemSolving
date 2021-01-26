package IOP;
import java.util.Scanner;

public class P10951 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a, b;
        while(stdIn.hasNextInt()) {
            a = stdIn.nextInt();
            b = stdIn.nextInt();
            System.out.println(a + b);
        }
    }
}
