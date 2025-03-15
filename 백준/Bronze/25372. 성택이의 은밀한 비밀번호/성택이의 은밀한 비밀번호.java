import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		for (int n=0; n<N; n++) {
			st = new StringTokenizer(br.readLine());
			String password = st.nextToken();
			if (password.length() >= 6 && password.length() <= 9) {
				System.out.println("yes");
				continue;
			}
			System.out.println("no");
		}
	}
}