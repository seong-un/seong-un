import java.io.*;
import java.math.BigInteger;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BigInteger A = new BigInteger(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		String operator = st.nextToken();
		
		st = new StringTokenizer(br.readLine());
		BigInteger B = new BigInteger(st.nextToken());
		
		if (operator.equals("*")) {
			System.out.println(A.multiply(B));
		} else {
			System.out.println(A.add(B));
		}
	}
}