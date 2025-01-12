import java.io.*;
import java.util.*;

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int max_result = Integer.MIN_VALUE;
	static int min_result = Integer.MAX_VALUE;
	
	static void calculate(int[] A, int[] operator, int[] cases, int n, int idx) {
		if(idx == n) {
			int total = A[0];
			for (int i=0; i<n; i++) {
				if (cases[i] == 1) {
					total += A[i+1];
				} else if (cases[i] == 2) {
					total -= A[i+1];
				} else if (cases[i] == 3) {
					total *= A[i+1];
				} else if (cases[i] == 4) {
					if (total >= 0) {
						total /= A[i+1];						
					} else {
						total = -total;
						total /= A[i+1];
						total = -total;
					}
				}
			}
			max_result = Math.max(max_result, total);
			min_result = Math.min(min_result, total);
			return;
		}
		
		for (int i=1; i<5; i++) {
			if (operator[i-1] == 0) continue;
			operator[i-1] -= 1;
			cases[idx] = i;
			calculate(A, operator, cases, n, idx + 1);
			operator[i-1] += 1;
			cases[idx] = 0;			
		}
	}
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int[] A = new int[N];
		for (int i=0; i<N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		int[] operator = new int[4];
		for (int i=0; i<4; i++) {
			operator[i] = Integer.parseInt(st.nextToken());
		}
		int[] cases = new int[N-1];
		calculate(A, operator, cases, N-1, 0);
		System.out.println(max_result);
		System.out.println(min_result);
	}
}