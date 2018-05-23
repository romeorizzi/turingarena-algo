import java.util.Scanner;

abstract class Skeleton {
    private static final Scanner in = new Scanner(System.in);

    static final int nColors;
    int blackScore(int c1, int c2, int c3, int c4) {
        System.out.printf("%d\n", 1);
        System.out.printf("%d\n", 0);
        System.out.printf("%d %d %d %d\n", c1, c2, c3, c4);
        System.out.flush();
        int ans;
        ans = in.nextInt();
        return ans;
    }

    int whiteScore(int c1, int c2, int c3, int c4) {
        System.out.printf("%d\n", 1);
        System.out.printf("%d\n", 1);
        System.out.printf("%d %d %d %d\n", c1, c2, c3, c4);
        System.out.flush();
        int ans;
        ans = in.nextInt();
        return ans;
    }

    abstract void play();

    static {
        nColors = in.nextInt();
    }

    public static void main(String args[]) {
        Solution solution = new Solution();
        solution.play();
        System.out.printf("%d\n", 0);
    }
}

