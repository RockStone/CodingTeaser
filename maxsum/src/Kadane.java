import java.lang.Math;

public class Kadane {
	public static void main(String[] args) {
		int[] array = { 2, 3, 1, -7, 0, -5, 4, -1, -1, 6 };
		int maxSum = -999;
		int maxStartIdx = 0;
		int maxEndIdx = 0;
		int currMaxSum = 0;
		int currStartIdx = 0;
		int currEndIdx = 0;
		
		for (; currEndIdx < array.length; currEndIdx++) {
			System.out.println("maxSum: " + maxSum + " currMaxSum: " + currMaxSum);
			System.out.println("maxStartIdx: " + maxStartIdx + " maxEndIdx: " + maxEndIdx);
			System.out.println("currStartIdx: " + currStartIdx + " currEndIdx: " + currEndIdx);
			
			currMaxSum += array[currEndIdx];
			if (currMaxSum > maxSum) {
				maxSum = currMaxSum;
				maxStartIdx = currStartIdx;
				maxEndIdx = currEndIdx;
			}
			
			if (currMaxSum < 0) {
				currMaxSum = 0;
				currStartIdx = currEndIdx + 1;
			}
		}
		
		System.out.println("maxSum: " + maxSum + " currMaxSum: " + currMaxSum);
		System.out.println("maxStartIdx: " + maxStartIdx + " maxEndIdx: " + maxEndIdx);
		System.out.println("currStartIdx: " + currStartIdx + " currEndIdx: " + currEndIdx);
		
		maxSum = -999;
		currMaxSum = 0;

		for (int i = 0; i < array.length; i++) {
			System.out.println("maxSum: "+ maxSum + " currMaxSum: " + currMaxSum);
			currMaxSum = Math.max(array[i], currMaxSum + array[i]);
			maxSum = Math.max(maxSum, currMaxSum);
		}
		
		System.out.println("maxSum: "+ maxSum + " currMaxSum: " + currMaxSum);

	}
}
