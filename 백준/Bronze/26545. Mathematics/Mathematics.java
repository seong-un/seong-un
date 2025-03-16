import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int result = 0;
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			result += Integer.parseInt(st.nextToken());
		}
		System.out.println(result);
	}
}