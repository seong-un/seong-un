import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		String alphabet = st.nextToken();
		
		HashMap<String, Integer> dict = new HashMap<>();
		for (int i=0; i<alphabet.length(); i++) {
			String index = alphabet.substring(i, i+1);
			if (dict.get(index) == null) dict.put(index, 0);
			dict.put(index, dict.get(index) + 1);
		}
		
		String[] words = {"B", "R", "O", "N", "Z", "E", "S", "I", "L", "V", "E", "R"};
		
		int result = 0;
		boolean for_break = true;
		while (true) {
			for (int i=0; i<12; i++) {
				String word = words[i];
				if (dict.get(word) == null || dict.get(word) == 0) {
					for_break = false;
					break;
				}
				dict.put(word, dict.get(word) - 1);
			}
			if (!for_break) break;
			result++;
		}
		
		System.out.println(result);
	}
}