import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;


public class MaxPath{

	private static void findMax(int[][] triangle, int ht) {
		int[] back = null;
		for(int i = 1; i < ht; i++) {
			int[] last = triangle[ht - i];
			back = rowMax(triangle[(ht - i) - 1], last);
		}
		System.out.println(back[0]);
	}
	
	private static int[] rowMax(int[] back, int[] last) {
		for (int i = 0; i < back.length; i++) {
			back[i] = back[i] + (Math.max(last[i], last[i + 1]));
		}
		return back;
	}

	private static int[][] getTriangle(String fileName, int ht) throws Exception {
		int[][] triangle = new int[ht][];
		FileReader fr = new FileReader(fileName);
		BufferedReader br = new BufferedReader(fr);

		String s;
		int i = 0;
		while ((s = br.readLine()) != null) {
			triangle[i] = new int[i + 1];
			int j = 0;
			Scanner tokens = new Scanner(s);
			while (tokens.hasNext()) {
				int value = tokens.nextInt();
				triangle[i][j++] = value;
			}
			i++;
		}

		return triangle;
	}

	public static void main(String args[]) throws Throwable {
		String fileName = "./_max.txt";
		int ht = 100;
		int[][] triangle = getTriangle(fileName, ht);
		findMax(triangle, ht);
	}
}
