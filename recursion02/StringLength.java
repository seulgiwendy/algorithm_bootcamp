import java.util.Scanner;

public class StringLength{
	
	String target;
	int length;

	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		StringLength sl = new StringLength();

		System.out.println("길이를 잴 문자열을 입력");
		String input = sc.nextLine();
		
		System.out.println(sl.checker(input));

	}

	public int checker(String input){
		
		this.target = input;

		if (target.equals("")){
			return 0;
		}

		else{
			return 1 + checker(target.substring(1));
		}
	}
}

			
