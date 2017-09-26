public class Max{

	public static void main (String args[]){

		int example [] = {1, 2, 3, 4, 100,  6};
		
		System.out.println(max(example, 0, 5));
	}
	
	public static int max(int [] data, int start, int end){

		if (start == end){
			
			return data[start];
		}
		
		else{
			return Math.max(data[start], max(data, start + 1, end));
		}
	}
}

