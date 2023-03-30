import java.util.Scanner;

//what library do you need for the scanner?

class Main {
    public sttatic /** what is needed in any program to run? **/(String[] args) {
      Scanner scan = new Scanner(System.in);
  
      /** feel free to change this; 
          you could enter in mm/dd/yyyy format if you use strings and split them
          resource: https://stackoverflow.com/questions/3481828/how-to-split-a-string-in-java
          then convert to string with int i=Integer.parseInt(string);
      **/
      System.out.println("Enter a month");
      int month = scan.nextInt();
      System.out.println("Enter a day");
      int day = scan.nextInt();
      System.out.println("Enter a year");
      int year = scan.nextInt();
  
      DateChecker check = //complete object declaration
      if (/** call your valid date function **/){
        System.out.println("That is a valid date");
      }
      else{
        System.out.println("OOPS!! That is NOT a valid date");
      }
      
    }
  }
  
  //DateChecker.java
  public class DateChecker{
    private int month;//include day and year...can you do it in 1 statement?
    public /**constructor**/(int m, int d, int y){
      //initialize variables
      
    }
  
    private boolean valid_month(){ //doesn't NEED to be private
      //ensure it is a valid month - can you do it in 1 line?    
    }
  
    valid_day(){ //returns T/F if it is a valid day
      if (/** you may want to write down months with 30, 31, or 28/9 days **/){
      }
      else if(month==2){
        if (leap_year()){
          //nested conditionals work, but can you make it cleaner?
        }
      }
      //how many if/else if/else conditions do you need?
    }
  
    private boolean leap_year(){
      return /** what we did on Thursday **/;
    }
  
    public boolean valid_date(){
      return ((valid_month()) && (valid_day()) /** do you need a valid_year? **/
    }
    
  }