package IOP;
import java.util.Scanner;

public class P10953 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        
        for (int i = 0; i < n; i++) {
            String[] arr = stdIn.next().split(",");
            System.out.println(Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]));
        }
        stdIn.close();
    }
}
