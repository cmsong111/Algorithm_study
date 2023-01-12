import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int price = Integer.parseInt(br.readLine());

        int money = 1000 - price;

        int result = 0;

        // 500 엔
        while (money >= 500) {
            money -= 500;
            result += 1;
        }
        // 100 엔
        while (money >= 100) {
            money -= 100;
            result += 1;
        }
        // 50 엔
        while (money >= 50) {
            money -= 50;
            result += 1;
        }
        // 10 엔
        while (money >= 10) {
            money -= 10;
            result += 1;
        }
        // 5 엔
        while (money >= 5) {
            money -= 5;
            result += 1;
        }
        // 1 엔
        while (money >= 1) {
            money -= 1;
            result += 1;
        }

        System.out.println(result);
    }
}
