import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = String.valueOf(br.readLine());
        String[] data = str.split(" ");

        ArrayList<Integer> array = new ArrayList<>();

        for (String i : data) {
            array.add(Integer.parseInt(i));
        }

        // Check ascending
        for (int i = 0; i < 8; i++) {
            if (array.get(i) != i + 1) {
                break;
            }
            if (i == 7) {
                System.out.println("ascending");
                return;
            }
        }

        // Check descending
        for (int i = 0; i < 8; i++) {
            if (array.get(i) != 8 - i) {
                break;
            }
            if (i == 7) {
                System.out.println("descending");
                return;
            }
        }
        // Print "mixed"
        System.out.println("mixed");
    }
}
