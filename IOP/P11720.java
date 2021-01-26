package IOP;
import java.util.Scanner;

public class P11720 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        String exam = stdIn.next();
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(String.valueOf(exam.charAt(i)));
        }

        System.out.println(sum);
    }
}