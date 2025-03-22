import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		for (int i=0; i<N*4; i++) {
			for (int n=0; n<N; n++) {
				System.out.print("@");
			}
			System.out.println();
		}
		
		for (int n=0; n<N; n++) {
			for (int i=0; i<N*5; i++) {
				System.out.print("@");
			}
			System.out.println();
		}
	}
}