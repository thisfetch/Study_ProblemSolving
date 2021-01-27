package IOP;
import java.util.Scanner;

public class P2445 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
            for (int k = 2 * n; k > 2 * (i + 1); k--) {
                System.out.print(" ");
            }
            for (int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
        for (int i = 0; i < n - 1; i++) {
            for (int j = n - 1; j > i; j--) {
                System.out.print("*");
            }
            for (int k = 0 ; k < 2 * (i + 1); k++) {
                System.out.print(" ");
            }
            for (int j = n - 1; j > i; j--) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
