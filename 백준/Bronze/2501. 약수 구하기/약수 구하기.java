import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		for (int n=1; n<=N; n++) {
			if (N % n == 0) {
				K--;
				
				if (K == 0) System.out.println(n);
			}
		}
		
		if (K > 0) System.out.println(0);
	}
}