public class Sequential{
	
	public static void main (String args[]){
		
		int [] example = {1, 2, 3, 4, 5, 6};
		int begin = 0;
		int end = example.length;
		int target = 3;

		System.out.println(search(example, begin, end, target));
	}

	public static int search(int[] data, int begin, int end, int target){
		
		if (begin > end){
			return -1;
		}

		else if(target == data[begin]){
			return begin;
		}

		else{
			System.out.println("아직 못 찾았읍니다...");
			return search(data, begin + 1, end, target);
		}
	}
}


	

		
				

