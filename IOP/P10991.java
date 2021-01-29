package IOP;
import java.util.Scanner;

public class P10991 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();

        for (int i = 0; i < n; i++) {
            for (int k = n; k > i + 1; k--) {
                System.out.print(" ");
            }
            for(int j = 1; j <= 2 * i + 1; j++) {
                if ( j % 2 == 0) {
                    System.out.print(" ");
                } else {
                    System.out.print("*");
                }
            }
            System.out.println("");
        }
        stdIn.close();
    }
}
