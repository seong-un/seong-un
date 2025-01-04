import java.io.*;
import java.util.*;

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	public static void main(String[] args) throws Exception {
		int N = Integer.parseInt(br.readLine());
		int[] dp = new int[N+1];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int T = Integer.parseInt(st.nextToken());
			int P = Integer.parseInt(st.nextToken());
			dp[i+1] = Math.max(dp[i], dp[i+1]);
			if (i+T >= N+1) continue;
			dp[i+T] = Math.max(P + dp[i], dp[i+T]);
		}
		dp[N] = Math.max(dp[N], dp[N-1]);
		System.out.println(dp[N]);
	}
}