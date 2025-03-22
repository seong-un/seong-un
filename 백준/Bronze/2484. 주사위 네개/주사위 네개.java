import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		int result = 0;
		int eye1, eye2, eye3, eye4;
		for (int n=0; n<N; n++) {
			st = new StringTokenizer(br.readLine());
			eye1 = Integer.parseInt(st.nextToken());
			eye2 = Integer.parseInt(st.nextToken());
			eye3 = Integer.parseInt(st.nextToken());
			eye4 = Integer.parseInt(st.nextToken());
			
			if (eye1 == eye2 && eye2 == eye3 && eye3 == eye4) {
				result = Math.max(result, 50000+eye1*5000);
			} else if ((eye1 == eye2 && eye2 == eye3)
					|| (eye1 == eye2 && eye2 == eye4)
					|| (eye1 == eye3 && eye3 == eye4)) {
				result = Math.max(result, 10000+eye1*1000);
			} else if (eye2 == eye3 && eye3 == eye4) {
				result = Math.max(result, 10000+eye2*1000);
			} else if (eye1 == eye2 && eye3 == eye4) {
				result = Math.max(result, 2000+eye1*500+eye3*500);
			} else if ((eye1 == eye3 && eye2 == eye4)
					|| (eye1 == eye4 && eye2 == eye3)) {
				result = Math.max(result, 2000+eye1*500+eye2*500);
			} else if (eye1 == eye2 || eye1 == eye3 || eye1 == eye4) {
				result = Math.max(result, 1000+eye1*100);
			} else if (eye2 == eye3 || eye2 == eye4) {
				result = Math.max(result, 1000+eye2*100);
			} else if (eye3 == eye4) {
				result = Math.max(result, 1000+eye3*100);
			} else {
				result = Math.max(result, 100*Math.max(eye1, Math.max(eye2, Math.max(eye3, eye4))));
			}	
		}
		
		System.out.println(result);
	}
}