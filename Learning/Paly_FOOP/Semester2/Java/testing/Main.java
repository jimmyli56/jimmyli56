import java.util.*;

class Main {
  public static void main(String[] args) {
    //take the following functional programming code and translate it into a class (named Converter.java)

    Scanner scan = new Scanner(System.in);

    //basic - feel free to add in conditionals
    System.out.println("Enter a temp in F and I will convert it to C");
    double faren = scan.nextDouble();
    System.out.println(faren + " degrees farenheit is the following in celcius: " + c_convert(faren));

    System.out.println("Enter a temp in C and I will convert it to F");
    double celc = scan.nextDouble();
    System.out.println(celc + " degrees farenheit is the following in celcius: " + f_convert(celc));
    scan.close();
  
  }

  static double c_convert(double temp){
    //update to convert correctly - remember parenthesis - round to 2 decimal places
    return (temp*1.1);
  }

  static double f_convert(double temp){
    //update to convert correctly - remember parenthesis - round to 2 decimal places
    return (temp/1.1);
  }
}