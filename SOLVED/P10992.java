package SOLVED;
import java.util.Scanner;

public class P10992 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int num = stdIn.nextInt();

        for (int i = 0; i < num; i++) {
            for (int k = num; k > i + 1; k--) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                if (i == 0 || i == num - 1) {
                    System.out.print("*");
                } else {
                    if (j == 0 || j == 2 * i) {
                        System.out.print("*");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println("");
        }
        stdIn.close();
    }
}