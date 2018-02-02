import java.util.Scanner;

public class StringPrinter{
	String target;

	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.println("출력할 문자열 입력.");
		String input = sc.nextLine();
		StringPrinter sp = new StringPrinter();
		sp.printer(input);
	}

	public void printer(String input){

		if (input.length() == 0){
			return;
		}
		
		else{
			System.out.print(input.charAt(0));
			printer(input.substring(1));
		}
	}
}

