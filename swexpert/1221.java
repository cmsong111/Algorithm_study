import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(bf.readLine());

        final String[] planet = new String[]{"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};

        for (int testCase = 1; testCase <= T; testCase++) {
            int[] count = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            bf.readLine();
            st = new StringTokenizer(bf.readLine());

            while (st.hasMoreTokens()) {
                String text = st.nextToken();
                switch (text) {
                    case "ZRO": {
                        count[0]++;
                        break;
                    }
                    case "ONE": {
                        count[1]++;
                        break;
                    }
                    case "TWO": {
                        count[2]++;
                        break;
                    }
                    case "THR": {
                        count[3]++;
                        break;
                    }
                    case "FOR": {
                        count[4]++;
                        break;
                    }
                    case "FIV": {
                        count[5]++;
                        break;
                    }
                    case "SIX": {
                        count[6]++;
                        break;
                    }
                    case "SVN": {
                        count[7]++;
                        break;
                    }
                    case "EGT": {
                        count[8]++;
                        break;
                    }
                    case "NIN": {
                        count[9]++;
                        break;
                    }
                }
            }
            System.out.println("#" + testCase);
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < count[i]; j++) {
                    System.out.print(planet[i] + " ");
                }
                System.out.println("");
            }
        }
    }
}