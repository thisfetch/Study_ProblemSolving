package IOP;
import java.util.Scanner;

public class P11022 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        while (stdIn.hasNextLine()) {
            String exam = stdIn.nextLine();
            if (exam.length() > 100) {
                break;
            } else {
                System.out.println(exam); 
            }
        }
        stdIn.close();
    }
}
