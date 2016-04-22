class StringSolver{

    char o = '('; 
    char c = ')';

    public int Solver(String A){

        int oCount = 0;
        int cCount = 0;
        int Equals = 0;
        
        for(int i = 0; i<A.length(); i++){
            
            
           if(A.charAt(i) == o){

                oCount += 1;

            }

            cCount = 0;
                

            for(int j = i +1; j<A.length(); j++){

                if(A.charAt(j) == c){
                    cCount += 1;
                }
            }

            if(oCount == cCount){
                
                Equals = i+1;
                break;

            }
        }

        return Equals;

    }
}

public class StringFinder{
    
    public static void main(String[] args){

    String SPasser = "(())))(";
    StringSolver solveit = new StringSolver();
    int tmp = solveit.Solver(SPasser);
    System.out.println(tmp);

    }
}
