import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int eye1 = Integer.parseInt(st.nextToken());
		int eye2 = Integer.parseInt(st.nextToken());
		int eye3 = Integer.parseInt(st.nextToken());
		
		if (eye1 == eye2 && eye2 == eye3) {
			System.out.println(10000 + eye1 * 1000);
		} else if (eye1 == eye2 || eye1 == eye3) {
			System.out.println(1000 + eye1 * 100);
		} else if (eye2 == eye3) {
			System.out.println(1000 + eye2 * 100);
		} else {
			System.out.println(Math.max(eye1, Math.max(eye2, eye3)) * 100);
		}
	}
}