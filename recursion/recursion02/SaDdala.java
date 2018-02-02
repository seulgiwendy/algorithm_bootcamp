public class SaDdala{

	private static final String INTRO = "일급 1달라는 너무 적소, 4딸라. 4딸라로 합시다.";
	int dollar = 1;

	public static void main (String args[]){
		SaDdala sd = new SaDdala();	
		System.out.println(INTRO);
		sd.FourDollars();
	}

	public void FourDollars(){
		
		if (dollar == 4){
			System.out.println("can't help with this. alright. four dollars!");
			System.out.println("오케이, 사딸라, 땡큐! 사딸라!");
		}

		else{
			System.out.println(dollar + " dollars.");
			System.out.println("사딸라.");
			dollar++;
			FourDollars();
		}

	}
}

