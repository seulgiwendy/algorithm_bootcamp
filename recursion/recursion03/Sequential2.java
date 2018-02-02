public class Sequential2{
	
	public static void main(String args[]){
		int example []= {1, 2, 3, 4, 5, 6};
		System.out.println(search(example, 0, 6, 6));
	}

	public static int search(int [] data, int start, int end, int target){
		
		if (start > end){
			return -1;
		}

		else{
			
			int middle = (start + end) / 2;
			if (data[middle] == target){
				return middle;
			}
			int index = search(data, start, middle - 1, target);
			if (index != -1){
				return index;
			}
			else{
				return search(data, middle + 1, end, target);
			}
		}
	}
}

