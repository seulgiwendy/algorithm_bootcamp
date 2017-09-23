import java.util.*;

public class hello{
	
	public static void main (String args[]){
		String [] letters = {"a", "e", "i", "o", "u"};
		
		for (String s: letters){
			System.out.println(s);
		}

		List <String> newlist = Arrays.asList(letters);

		for (String s: newlist){
			System.out.println(s);
		}

	}
}
