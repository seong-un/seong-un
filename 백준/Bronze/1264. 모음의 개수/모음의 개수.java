import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			int result = 0;
			String sentence = br.readLine();
			sentence = sentence.toLowerCase();
			
			if (sentence.equals("#")) break;
			for (int i=0; i<sentence.length(); i++) {
				char letter = sentence.charAt(i);
				if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') result++;
			}
			
			System.out.println(result);
		}
	}
}