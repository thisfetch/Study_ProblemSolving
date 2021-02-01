package SOLVED;
import java.util.Scanner;

public class P8958 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        stdIn.nextLine();
        for (int i = 0; i < n; i++) {
            String str = stdIn.nextLine();
            int count = 0; 
            int sum = 0;
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == 'O') {
                    count++;
                    sum += count;
                } else {
                    count = 0;
                }
            }
            System.out.println(sum);
            stdIn.close();
        }
        
    }
}