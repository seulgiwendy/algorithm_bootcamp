import java.util.Scanner;

public class BinaryConverter{
	
	public static void main (String args[]){
		binary(10);
		
	}
	
	public static void binary(int n){
		
		if (n < 2){
			System.out.print(n);
		}

		else{
			binary(n / 2);
			System.out.print(n % 2);
		}
	}

}

