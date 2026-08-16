 publicn Main 
{
    public static void main(String[]args){
     
      int number=131;
      int temp=number ;
      int rev=0;
      while(number>0){
        digit=number%10;
        rev=rev*10+digit;
         
        number=number/10;


        }

        if(temp==rev){
            System.out.println("Polindrome Number ",temp);
   
        }
        else{
             System.out.println(" Not Polindrome Number ",temp);
        }

      




    }
}