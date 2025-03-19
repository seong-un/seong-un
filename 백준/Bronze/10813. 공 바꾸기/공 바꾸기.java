import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] balls = new int[N+1];
		for (int n=1; n<N+1; n++) {
			balls[n] = n;
		}
		
		int temp = 0;
		for (int m=0; m<M; m++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			temp = balls[i];
			balls[i] = balls[j];
			balls[j] = temp;
		}
		
		for (int n=1; n<N+1; n++) {
			System.out.print(balls[n] + " ");
		}
	}
}