package Week02;
/*
Program concepts:
Using wrapper class objects
demonstrating autobxing and unxing
using enum
using enum constructor and methods
*/
enum Booking_type{
    SUITE(20000),
    STANDARD(10000),
    DELUXE(15000);

    private double price;

    Booking_type(double price){
        this.price = price;
    }
    public double value(){
        return price;
    }
}

class Hotel_billing{
    private Integer roomno;
    private Double base;
    private Integer days;
    private double final_bill = 0.0;
    private Booking_type type;

    Hotel_billing(int rno,int days, Booking_type bt){
        // auto boxing
        roomno = rno;
        this.base = bt.value();
        type = bt;
        this.days = days;
    }
    public void calculate_bill(int rate){
        double bill = base;
        //unboxing 
        bill = bill+ rate*days;
        final_bill = bill;
    }
    public void display_bill(){
        if(final_bill<= 0){
            calculate_bill(300);
        }
        System.out.println("The final bill for room number "+ roomno+"\nbilling type: "+type+"\nrs: "+final_bill);
    }
}
public class Main {
    public static void main(String[] args){
        Booking_type r1 = Booking_type.DELUXE;
        Booking_type r2 = Booking_type.SUITE;
        Hotel_billing room1 = new Hotel_billing(100,10,r1);
        Hotel_billing room2 = new Hotel_billing(101,9,r2);
        room1.display_bill();
        room2.calculate_bill(500);
        room2.display_bill();
    }
}


/* 
wrapper class helps to wrap your primitive data type
hold the premitive type as a object inside the wrapper class
for every data type there is a data type

the object of wrapper class holds the fields of the primitive data types

primitive to object: auto boxing
object to primitice: unboxing

need for wrapper class
helps converts primitive to object type
collection framework hold objects and not primitive data type
object is needed to synchronization of multithreading
multithreading: parallel processing

int b;
Integer a;
b = 34;
a = b;
this is auto wrapping converting primitive to wrapper object (auto boxing)
AutoBoxing and unboxing

Enumeration
Special type used to define a group of named comstants
readability, maintainability and type safety in programs by assigning meaningful names to intger values
user cannot create object for the enum class. 
example
enum Trafficlights {
red, green, yellow
}

trafficlight x = trafficlight.red;

Enum with switch statements

Enum methods and constructirs, can be executed seperately for each constant
enum color{
red, green, blue

private color ()  // the enum constructor should be private
{
sop("constructor for :" +this);
}

public void display () // this is a enum method
{
sop("current color is:"+ this);

}

}
// output
constructor for red
constructor for blue
constructor for green
color is red
*/