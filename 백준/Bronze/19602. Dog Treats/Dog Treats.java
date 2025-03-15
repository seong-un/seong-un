import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int happiness = 0;
		for (int i=1; i<4; i++) {
			st = new StringTokenizer(br.readLine());
			happiness += i * Integer.parseInt(st.nextToken());
		}
		
		if (happiness >= 10) System.out.println("happy");
		else System.out.println("sad");
	}
}