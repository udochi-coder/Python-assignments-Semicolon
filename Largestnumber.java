import java.util.Scanner;
public class Largestnumber{
public static void main(Strig[]args);
Scanner input=new Scanner(System.in);
System.out.print("Enter First number");
int numOne=input.nextInt();
System.out.print("Enter Second number");
int numTwo=input.nextInt();
System.out.print("Enter Third number");
int numThree=input.nextInt();

if(numOne > numTwo && numOne > numThree){
System.out.println(numOne +" is the largest number");
}
if(numTwo > numOne && numTwo > numThree){
System.out.println(numTwo+ "is the largest number");
}
if(numThree > numOne && numThree > numTwo){
System.out.println(numThree+ "is the largest number");
}
}
}

