import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        while (true) {
            int result = 0;
            String input = br.readLine();
            if (input.equals("#")) {
                break;
            }

            for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                if (c == 'a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U') {
                    result += 1;
                }
            }
            System.out.println(result);
        }


    }
}
