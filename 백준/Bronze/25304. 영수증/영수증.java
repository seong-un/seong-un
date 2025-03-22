import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int X = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		
		int a, b;
		int sum = 0;
		for (int n=0; n<N; n++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			
			sum += a * b;
		}
		
		if (sum == X) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}