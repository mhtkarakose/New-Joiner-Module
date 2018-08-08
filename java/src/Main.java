public class Main {

    public static int[] fiboArray = new int[100];
    public static int[] digitArray = new int[100];

    public static void LoadFiboArray(){
        int n1=1,n2=1,n3,i,count=30;
        // System.out.print(n1+" "+n2);//printing 0 and 1
        fiboArray[1]=1;
        fiboArray[2]=2;

        for(i=2;i<count;i++)//loop starts from 2 because 0 and 1 are already printed
        {
            n3=n1+n2;
            fiboArray[i] = n3;
            n1=n2;
            n2=n3;
        }// end for
    } // end LoadFiboArray

    public static void LoadPowerOfDigitArray(){

        int PowerOfTwo = 0;

        for(int i = 1; i < 20; i++){
            PowerOfTwo = (int)Math.pow(2, i);
            digitArray[i] = String.valueOf(PowerOfTwo).length();
        }
    }

    public static void main(String[] args) {

        int length = 7;
        int height = 2;
        int boardNumber = 1;
        int boardDigitNumber = 1;

        LoadFiboArray();
        LoadPowerOfDigitArray();

        for (int i = 0; i <= height; i++)
        {
            if (i % 2 == 0)
            {
                System.out.print(fiboArray[boardNumber]+ " ");
                boardNumber++;
            }

            for (int j = 0; j <= length; j++)
            {
                if (j % 2 == 0)
                {
                    System.out.print(digitArray[boardDigitNumber]+ " ");
                    boardDigitNumber++;
                }
                else if (j != length || i % 2 != 0)
                {
                    System.out.print(fiboArray[boardNumber]+ " ");
                    boardNumber++;
                }
            }
            System.out.println("");
        } // end for
    } // end main
} // end class

