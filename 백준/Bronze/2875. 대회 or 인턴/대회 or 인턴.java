import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		for (int k=0; k<K; k++) {
			if (N > M * 2) N--;
			else M--;
		}
		
		if (M==0) System.out.println(0);
		else System.out.println(Math.min(N/2, M));
	}
}