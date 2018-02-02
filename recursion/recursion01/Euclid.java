public class Euclid{

	public static void main(String args[]){
		
		System.out.println(euclid(100, 25));
	}

	public static int euclid(int a, int b){
		
		if (b > a){
			int tmp = b;
			b = a;
			a = tmp;
		}

		int d = a % b;

		if (d == 0){
			return b;
		}

		else{
			return euclid(b, d);
		}

	}
}

			
