import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int count = Integer.parseInt(br.readLine());

        int root = Integer.parseInt(br.readLine());
        int result[] = {root};
        int temp[];

        for (int i = 1; i < count; i++) {
            // 일단 값 저장
            String[] input = br.readLine().split(" ");
            temp = new int[i + 1];
            for (int j = 0; j < i + 1; j++) {
                temp[j] = Integer.parseInt(input[j]);
            }

            // 상위 값에서 값 가져오는데 첫번째랑 마지막은 예외 처리
            // 첫번째꺼
            temp[0] = result[0] + temp[0];

            // 중간 값
            for (int j = 1; j < i; j++) {
                temp[j] = Math.max(result[j - 1], result[j]) + temp[j];
            }
            // 마지막 값
            temp[i] = result[i - 1] + temp[i];

            // Result값 저장
            result = temp;

        }

        // 최대값 구하기
        int max = 0;
        for (int i = 0; i < count; i++) {
            if (max < result[i]) {
                max = result[i];
            }
        }
        // Count 가 하나일 수 도 있으니까 예외처리 후 출력
        if (count == 1) {
            System.out.println(root);
        } else {
            System.out.println(max);
        }

    }


}
