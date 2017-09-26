public class Binary{
	
	public static void main (String args[]){

		int [] example = {1, 2, 3, 4, 5, 6};
		System.out.println(search(example, 5, 0, 5));
	}

	public static int search(int [] data, int target, int start, int end){
		if (start > end){
			return -1;
		}

		else {
			int middle = (start + end) / 2;
			
			int compResult = target - data[middle];
			if (compResult == 0){
				return middle;
			}
			else if (compResult < 0){
				return search(data, target, start, middle - 1);
			}
			else{
				return search(data, target, middle + 1, end);
			}
		}
	}
}

		
