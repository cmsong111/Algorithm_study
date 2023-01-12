import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int result = 0;

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) <= 'C'){
                result += 3;
            }
            else if(input.charAt(i) <= 'F'){
                result += 4;
            }
            else if(input.charAt(i) <= 'I'){
                result += 5;
            }
            else if(input.charAt(i) <= 'L'){
                result += 6;
            }
            else if(input.charAt(i) <= 'O'){
                result += 7;
            }
            else if(input.charAt(i) <= 'S'){
                result += 8;
            }
            else if(input.charAt(i) <= 'V'){
                result += 9;
            }
            else if(input.charAt(i) <= 'Z'){
                result += 10;
            }
        }

        System.out.println(result);

    }
}
