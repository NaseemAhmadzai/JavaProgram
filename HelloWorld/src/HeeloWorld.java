import java.util.Scanner;
public class HeeloWorld {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
            System.out.println("My Name is Naseem Ahmadzai");
           
//              Answer for Questions no :1
//                for a the answer is 0
//                for b the answer is 2.0
//                for c the answer is 0.25
//                in d there is syntax error because 4.0 is float not int
//                for e the answer is 0.0
            
              System.out.println(1/4);
              System.out.println(4.0/2);
              System.out.println(1.0/4.0);
              double x = 1/4;
              System.out.println(x);
            
//            Answer for Questions no :2
//              int y = (int) Math.PI; the answer is 3
//              System.out.println(y); the answer is 3
//              int d = (int) (Math.PI*20); 
//              System.out.println(d); the answer is 62
                
              
//              Answer for question no:3
//               for a the answer is 4
//               for b the answer is 0.0
//               for c the syntax is incorrect becuase we cant change int to double using this method:(   int y = (double) 8;)
//               for d the answer is 2
//               for e the answer  is 5
        
              int s = (int)4.99;
              System.out.println(s);
              double w = (int)0.999;
              System.out.println(w);
//              int y = (int)4.99/(int)2.5;  
//              System.out.println(y);
              int v = (int) (4.5 / 0.9);
              System.out.println(v);  
              
              
              
//            Answer for question no:4
//              For a the answer is here:
//            Scanner V =new Scanner(System.in);
//            System.out.println("Enter the radius:");
//            double r= V.nextDouble();
//            double  area=Math.PI * r*r;
//            System.out.println("Area of Circle is: " + area);   
//            
//            
            
//              I Comment the Upper code becuase the code in C will not work Becuase there is same variable which is r :
              
              
              
              
            
//          For b the answer is here:  
            int x1,x2,y1,y2;
            double dis;
            Scanner sc=new Scanner(System.in);
            System.out.println("enter x1 point");
            x1=sc.nextInt();
            System.out.println("enter y1 point");  
            y1=sc.nextInt();
            System.out.println("enter x2point");
            x2=sc.nextInt();
	        System.out.println("enter y2 point");
	        y2=sc.nextInt();
	        dis=Math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
	        System.out.println("distancebetween"+"("+x1+","+y1+"),"+"("+x2+","+y2+")===>"+dis);
            
	        
	        
//	       For c the answer is here
           
	        double A=0;
	        double P = 0;
	        double r = 0;
	        double n = 0;
	        Scanner m=new Scanner(System.in);
            System.out.println("Enter p");
            P=sc.nextDouble();
            System.out.println("Enter r");
            r=sc.nextDouble();
            System.out.println("Enter n");
            n=sc.nextDouble();
	        A = P * Math.pow((1+r), n);
	        
	        
	        System.out.println("The total amount earned is: "+A);
	        
	        
	        
	        
	        
	        
	        
	        
	        
	        
	        
	        
	        
	        
//	       For d The answer is here:
	        //variables
	        int dice1;
	        int dice2;
            
	        //Call the welcome method
	        welcome();
	      

	 }
    public static void welcome() {
        System.out.println("Welcome to a Lucky (for me) Dice Game!");
	    int roll2,roll=0;    
        int dice1=(int)(Math.random()*6+1);
        int dice2=(int)(Math.random()*6+1);
        int sum= dice1 + dice2;

        System.out.println("Roll: total = " +sum); 

        if (sum==2|| sum==3|| sum==12){
        System.out.println("Sorry with a " + sum + " You LOSE :("); }
        else if(sum==7 || sum==11) { 
        System.out.println("Woah!!! With a " + sum + " You WIN!!!!!!!"); } 
        else{ 
        	if(sum==4 ||sum==5 ||sum==6 ||sum==8 ||sum==9 ||sum==10) {
        		
        		roll=sum;
                dice1=(int)(Math.random()*6+1);
                dice2=(int)(Math.random()*6+1);
                
        
                roll2 = dice1 + dice2;
                System.out.println("You rolled "+roll2+"  ");
			    if(roll2== 7){
			    	System.out.println("Sorry with a " + sum + " You LOSE :(");
			    }
			    if (roll == roll2) {
			    System.out.println("You Win !");
			    
			    }
        
     } 
        
        }} 
	        
	        
	        
	        
	        
	        
	        
                
 }
              
      

































