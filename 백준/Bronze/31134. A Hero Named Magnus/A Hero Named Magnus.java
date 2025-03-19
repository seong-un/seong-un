import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine().trim());  // 첫 줄 입력

        for (int t = 0; t < T; t++) {
            long n = Integer.parseInt(br.readLine().trim());  // 다음 줄 입력
            System.out.println(2 * n - 1);
        }
    }
}
