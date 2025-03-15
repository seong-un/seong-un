import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int score;
		for (int i=0; i<2; i++) {
			score = 0;
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<5; j++) {
				int point = Integer.parseInt(st.nextToken());
				
				if (j==0) score += point * 6;
				else if (j==1) score += point * 3;
				else if (j==2) score += point * 2;
				else if (j==3) score += point * 1;
				else score += point * 2;				
			}
			
			System.out.print(score + " ");
		}
	}
}