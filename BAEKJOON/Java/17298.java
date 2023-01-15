import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int count = Integer.parseInt(br.readLine());
        int[] arr = new int[count];
        int[] result = new int[count];

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        for(int i = 0;i<count;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> big = new Stack<Integer>();

        for (int i = count - 1; i >= 0; i--) {
            while (true) {
                if (big.isEmpty()) {
                    result[i] = -1;
                    break;
                } else if (big.peek() > arr[i]) {
                    result[i] = big.peek();
                    break;
                } else {
                    big.pop();
                }
            }
            big.push(arr[i]);
        }
        // 결과 출력
        for (Integer num : result) {
            bw.write(num + " ");
        }
        bw.flush();
        bw.close();
    }
}
