import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class node {
    public int data;
    public node left;
    public node right;

    public node(int data) {
        this.data = data;
        left = null;
        right = null;
    }

    public void insert(int data) {
        if (data < this.data) {
            if (left == null) {
                left = new node(data);
            } else {
                left.insert(data);
            }
        } else {
            if (right == null) {
                right = new node(data);
            } else {
                right.insert(data);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int temp = Integer.parseInt(br.readLine());
        node root = new node(temp);

        String input;
        while (true) {
            input = br.readLine();
            if (input == null || input.equals("")) {
                break;
            }
            root.insert(Integer.parseInt(input));
        }

        postorder(root);

    }

    static void postorder(node root) {
        if (root == null) {
            return;
        }
        postorder(root.left);
        postorder(root.right);
        System.out.println(root.data);
    }
}
