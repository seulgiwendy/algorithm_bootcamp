public class ArrayPrinter{

	public static void main (String args[]){
		
		int [] testArray = {1, 2, 3, 4, 5, 6};
		System.out.println(arrayPrint(6, testArray));
	}

	public static int arrayPrint(int count, int [] array){

		if (count == 0){
			return 0;
		}

		else{
			return arrayPrint(count - 1, array) + array[count - 1];
		}
	}
}

