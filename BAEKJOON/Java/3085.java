import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int checkMax(char[][] arr, int size) {
        int count = 0, result = 0;

        // 가로 체크
        for (int i = 0; i < size; i++) {
            count = 1;
            for (int j = 0; j < size - 1; j++) {
                if (arr[i][j] == arr[i][j + 1]) {
                    count++;
                } else {
                    count = 1;
                }
                if (count > result) {
                    result = count;
                }
            }
        }

        //세로 체크
        for (int i = 0; i < size; i++) {
            count = 1;

            for (int j = 0; j < size - 1; j++) {
                if (arr[j][i] == arr[j + 1][i]) {
                    count++;
                } else {
                    count = 1;
                }
                if (count > result) {
                    result = count;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int size = Integer.parseInt(br.readLine());

        char[][] arr = new char[size][size];
        int result = 0;

        // 배열 입력 받기
        for (int i = 0; i < size; i++) {
            String input = br.readLine();

            for (int j = 0; j < input.length(); j++) {
                arr[i][j] = input.charAt(j);
            }
        }

        int max = 0;

        // 사탕 위치 바꾸기 (가로)
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size - 1; j++) {
                char temp[][] = new char[size][size];

                for (int k = 0; k < size; k++) {
                    System.arraycopy(arr[k], 0, temp[k], 0, arr[k].length);
                }

                char temp2 = temp[i][j];
                temp[i][j] = temp[i][j + 1];
                temp[i][j + 1] = temp2;


                if (result < checkMax(temp, size)) {
                    result = checkMax(temp, size);
                }
                if (result == size) {
                    System.out.println(result);
                    return;
                }

            }
        }

        // 사탕 위치 바꾸기 (세로)
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size; j++) {
                char temp[][] = new char[size][size];

                for (int k = 0; k < size; k++) {
                    System.arraycopy(arr[k], 0, temp[k], 0, arr[k].length);
                }

                char temp2 = temp[i][j];
                temp[i][j] = temp[i + 1][j];
                temp[i + 1][j] = temp2;

                if (result < checkMax(temp, size)) {
                    result = checkMax(temp, size);
                }
                if (result == size) {
                    System.out.println(result);
                    return;
                }
            }
        }
        System.out.println(result);
    }
}

