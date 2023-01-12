import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        StringBuffer sb = new StringBuffer(input[0]);
        int n = Integer.parseInt(sb.reverse().toString());


        sb = new StringBuffer(input[1]);
        int m = Integer.parseInt(sb.reverse().toString());

        if (n > m) {
            System.out.println(n);
        } else {
            System.out.println(m);
        }



    }
}
