import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String temp = br.readLine();
        String input = br.readLine();

        int reuslt = 0;

        for (int i = 0; i < input.length(); i++) {
            reuslt += Integer.parseInt(String.valueOf(input.charAt(i)));
        }

        System.out.println(reuslt);
    }
}
