/*1.	Create a Book class with private data members including book ID, book title, author name, price, and availability status. 
Provide public setter methods to assign values to these data members and public getter methods to retrieve their values. 
Include validation in setter methods to ensure that the price is a positive value.*/
package Week01;
import java.util.Scanner;
public class Book{

    private int bookid;
    private String title;
    private String author;
    private float price;
    private boolean availability;
    Book(){

    }
    //getter methods
    public void get_bookid(int id){
        this.bookid = id;
    }
    public void get_title(String title){
        this.title = title;
    }

    public void get_author(String author){
        this.author = author;
    }
    public void get_price(float price){
    this.price = price;
    }
    
    public void get_availabality(boolean availability){
        this.availability = availability;
    }


    // validation for price
    public boolean check_price(){
        return price >= 0;
    }
  
}

class demomain{
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        Book b= new Book();
        System.out.println("Enter the Book id, name of author, title, availabality status and price.");
        b.get_bookid(scn.nextInt());
        scn.nextLine();
        String author = scn.nextLine();
        b.get_author((author));
        b.get_availabality(scn.nextBoolean());
        scn.nextLine();
        b.get_title(scn.nextLine());
        b.get_price(scn.nextFloat());
        //check if price is valid
        if(!b.check_price()){
            System.out.println("enter a non negetive number");
            b.get_price(scn.nextFloat());
        }
        scn.close();
    }
}