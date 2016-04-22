class SolveArray{

    public static int Solver(int A[]){

        int count = 0;
        int i = 0;
        while (A[i]!=-1){
            count += 1;
            i = A[i];
        }
        return count;

    }
}

public class ArrayNode{

    public static void main(String[] args){

       int[] arrayNodes = {1,3,4,4,-1};

       SolveArray solveit = new SolveArray();
       int tmp = solveit.Solver(arrayNodes);
       System.out.println(tmp);

    }   
}
