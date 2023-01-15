import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringBuffer sb;

        StringBuffer temp = new StringBuffer("");
        StringBuffer result = new StringBuffer("");
        boolean stacked = false;

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '<') {
                sb = new StringBuffer(temp);
                sb.reverse();
                result.append(sb);
                temp = new StringBuffer("<");
                stacked = true;

            } else if (input.charAt(i) == '>') {
                temp.append(">");
                result.append(temp);
                temp = new StringBuffer("");
                stacked = false;

            } else if (input.charAt(i) == ' ' && !stacked) {
                sb = new StringBuffer(temp);
                sb.reverse();
                result.append(sb);
                result.append(' ');
                temp = new StringBuffer("");

            } else {
                temp.append(input.charAt(i));
            }
        }
        // 마무리
        sb = new StringBuffer(temp);
        sb.reverse();
        result.append(sb);

        //결과 출력
        System.out.println(result.toString());
    }
}

