package IOP;
import java.util.Scanner;

public class P11721 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        String arr = stdIn.next();
        if (arr.length() > 10) {
            for (int i = 0; i < arr.length(); i++) {
                if (i != 0 && i % 10 == 0) {
                    System.out.println("");
                    System.out.print(arr.charAt(i));
                } else {
                    System.out.print(arr.charAt(i));
                }
            }
        } else {
            System.out.println(arr);
        }
        stdIn.close();
    }
}