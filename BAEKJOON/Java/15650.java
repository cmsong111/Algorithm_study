import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static void combination(int arr[], boolean visited[], int start, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }

    static void print(int arr[], boolean visited[], int n) {
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int arrMax = Integer.parseInt(st.nextToken());
        int arrLen = Integer.parseInt(st.nextToken());

        int arr[] = new int[arrMax];

        for (int i = 0; i < arrMax; i++) {
            arr[i] = i + 1;
        }

        boolean visited[] = new boolean[arr.length];

        combination(arr, visited, 0, arrMax, arrLen);
    }
}
