import java.util.Scanner;
public class FathersAge{
public static void main(String[]args){
Scanner input=new Scanner(System.in);


System.out.print("Enter current father's age: ");
int fatherAge=input.nextInt();
System.out.print("Enter current son's age: ");
int sonAge=input.nextInt();

int Years=2 * sonAge;
int Yearssum=Years - fatherAge;
 
System.out.print("The father's age is " + Yearssum +  "years older");



}
}

