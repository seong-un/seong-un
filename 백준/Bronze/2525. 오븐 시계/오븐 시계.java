import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int C = Integer.parseInt(st.nextToken());
		
		B += C;
		if (B >= 60) {
			A += B/60;
			B %= 60;
		}
		
		if (A >= 24) A %= 24;
		System.out.println(A + " " + B);
		
	}
}