import java.util.Scanner;
public class Leap{
public static void main(String[]args){
Scanner input=new Scanner(System.in);

System.out.print("Enter year: ");
int years=input.nextInt();

if (years % 4 == 0){
System.out.println("it is a leap year");
}
else if(years % 100 != 0){
System.out.println("it is not a leap year");
}
else if(years % 400 == 0){
System.out.println("it is a leap year");
}

}
}

