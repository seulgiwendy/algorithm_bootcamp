public class HelloRecursion{
	
	int repeat = 5;

	public static void main (String args[]){

		HelloRecursion hr = new HelloRecursion();
		hr.printHello();
	}

	public void printHello(){
		
		if (repeat == 0){
			return;
		}

		else{
			System.out.println("hello world!");
			repeat--;
			printHello();
		}
	}
}

