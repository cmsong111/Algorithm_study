public import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        // i = a
        for (int i = 2; i <= 100; i++) {
            // ii = b
            for (int ii = 2; ii <= i; ii++) {
                // iii = c
                for (int iii = ii; iii <= i; iii++) {
                    // iii = d
                    for (int iiii = iii; iiii <= i; iiii++) {
                        if (Math.pow(i, 3) == Math.pow(ii, 3) + Math.pow(iii, 3) + Math.pow(iiii, 3)) {
                            System.out.println("Cube = " + i + ", Triple = (" + ii + "," + iii + "," + iiii + ")");
                        }
                    }
                }
            }
        }
    }
}
 {
    
}
