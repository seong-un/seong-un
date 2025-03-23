import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<Long> Fibonacci = new ArrayList<>();
		Fibonacci.add(0L);
		Fibonacci.add(1L);
		
		int length = 0;
		for (int i=1; i<n; i++) {
			length = Fibonacci.size();
			Fibonacci.add(Fibonacci.get(length-1) + Fibonacci.get(length-2));
		}
		
		if (n == 0) System.out.println(0);
		else if (n ==  1) System.out.println(1);
		else System.out.println(Fibonacci.get(length));
	}
}