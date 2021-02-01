package SOLVED;
import java.util.Scanner;

public class P1924 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int[] monthArr = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int month = stdIn.nextInt();
        int day = stdIn.nextInt();
        int sum = 0;
        int tmp;
        
        if ((month > 0 && month < 13) && (day > 0 && day < 32)) {
            for (int i = 0; i < month; i++) {
                sum += monthArr[i];
            }
            sum += day;
            tmp = sum % 7;
            switch (tmp) {
                case 1: System.out.println("MON"); break;
                case 2: System.out.println("TUE"); break;
                case 3: System.out.println("WED"); break;
                case 4: System.out.println("THU"); break;
                case 5: System.out.println("FRI"); break;
                case 6: System.out.println("SAT"); break;
                case 0: System.out.println("SUN"); break;
            }
        } else {
            System.out.println("");
        }
        stdIn.close();
    }
}
