import java.nio.charset.StandardCharsets;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            String encoded = sc.nextLine();
            String decoded = new String(Base64.getDecoder().decode(encoded), StandardCharsets.UTF_8);
            System.out.printf("#%d %s\n", testCase, decoded);
        }
    }
}