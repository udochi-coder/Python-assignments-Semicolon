import java.util.Scanner;
public class Password{
public static void main(String[]args){
Scanner input=new Scanner(System.in);

System.out.print("Enter your password: ");
String password=input.nextLine();

int length=password.length();

if (length  > 6 && length <= 10){
 System.out.println("Medium");
}
if( length < 6 ){
System.out. println("Weak");
}
if( length > 10){
System.out.println("Strong");
}
if(length < 1){
 System.out.println("is invalid");
}

}
}

