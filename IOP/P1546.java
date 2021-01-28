package IOP;
import java.util.Scanner;
import java.util.Arrays;

public class P1546 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int num = stdIn.nextInt();
        double sum = 0;
        double ave = 0;
        double[] arr = new double[num];

        for (int i = 0; i < num; i++) {
            arr[i] = stdIn.nextDouble();
        }
        Arrays.sort(arr);

        double max = arr[num - 1];

        for (int i = 0; i < num; i++) {
            arr[i] = arr[i] / max * 100;
            sum += arr[i];
        }
        ave = sum / num;
        System.out.println(ave);
    }
}
