public class Recursion2{
	
	public static void main (String args[]){
		int n = 100;
		System.out.println(func(n));
	}

	public static int func(int n){
		if (n == 0){
			return 0;
		}

		else{
			
			return n + func(n - 1);
		}
	}
}

