import java.util.Scanner;
public class Pizzawahala{
public static void main(String[]args){
Scanner input=new Scanner(System.in);
int sapaslice= 4;                             
int smallslice= 6;                                    
int bigslice=8;                                        
int odogwuslice=12;
int sapaprice=2000;
int smallprice=2000;
int bigprice=3000;
int odogwuprice=4200;                         
System.out.println("""

Welcome to Iya Scambirah Pizza!!
What is the number of people?
""");
int numberofpeople=input.nextInt();
input.nextLine();
System.out.println("""
What Pizza Type would you like Sir/Ma
Sapa Size.
Small Money.
Big Boys.
Odogwu.
""");
String typeofpizza=input.nextLine();
int pizzaslices=0;
int pizzaprices=0;

if(typeofpizza.equalsIgnoreCase("Sapa Size")){
pizzaslices=sapaslice;
pizzaprices=sapaprice;
}
else if(typeofpizza.equalsIgnoreCase("Small Money")){
pizzaslices=smallslice;
pizzaprices=smallprice;
}
else if(typeofpizza.equalsIgnoreCase("Big Boys")){
pizzaslices=bigslice;
pizzaprices=bigprice;
}
else if (typeofpizza.equalsIgnoreCase("Odogwu")){
pizzaslices=odogwuslice;
pizzaprices=odogwuprice;
}
int boxes=1;

while(boxes * pizzaslices < numberofpeople){
boxes++;
}
int bill=boxes * pizzaprices;
int leftoverpizza=boxes * pizzaslices - numberofpeople;


System.out.println("Number of boxes of pizza to buy =" + boxes + "boxes");
System.out.println("Number leftover slice after serving=" + leftoverpizza + "slices");
System.out.println("Prices=" + bill);

}

}

















