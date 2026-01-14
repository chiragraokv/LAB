package Week01;
/*3.	Design and implement a Java application to simulate a Hotel Room Booking System that demonstrates the object-oriented concepts of inheritance and runtime polymorphism.

i.	Create a base class named Room that represents a general hotel room. The class should contain data members such as room number and base tariff, 
        and a method calculateTariff() to compute the room cost.
ii.	Create derived classes such as StandardRoom and LuxuryRoom that inherit from the Room class. 
    Each derived class should override the calculateTariff() method to compute the tariff based on room-specific features such as 
    air conditioning, additional amenities, or premium services.
iii.In the main class, create a base class reference of type Room and assign it to objects of different derived classes (StandardRoom, LuxuryRoom).
        Invoke the calculateTariff() method using the base class reference to demonstrate runtime polymorphism,
        where the method call is resolved at runtime based on the actual object type
 */

    

class StandardRoom extends Room{
    private boolean ac,additional;
    StandardRoom(int roomno, String type){
        super(roomno,type);
    }
    StandardRoom(int roomno, String type, double base,boolean ac, boolean additional){
        super(roomno,type,base);
        this.ac = ac;
        this.additional = additional;
    }

    public double calculate_tarrif(int days){
        double base = put_base_price()*days;
        if(ac){
            base = base+ (0.05*base);
        }
        if(additional){
            base = base + (0.08* base);
        }
        return base;
    }
}
class LuxuryRoom extends Room{
    private boolean ac,additional,premium;
    LuxuryRoom(int roomno, String type){
        super(roomno,type);
    }
    LuxuryRoom(int roomno, String type, double base,boolean ac, boolean additional,boolean premium){
        super(roomno,type,base);
        this.ac = ac;
        this.additional = additional;
        this.premium = premium;
    }

    public double calculate_tarrif(int days){
        double base = put_base_price()*days;
        if(ac){
            base = base+ (0.05*base);
        }
        if(additional){
            base = base + (0.08* base);
        }
        if(premium){
            base = base+(base*0.1);
        }
        return base;
    }
}
public class RoomBooking {
    public static void main(String[] args) {
        LuxuryRoom lr = new LuxuryRoom(22, "single", 100.0, false, true, true);
        System.out.println("room details:\n");
        lr.display();
        System.out.println("\nfinal price for 10 days of stay: "+lr.calculate_tarrif(10));

        StandardRoom sr = new StandardRoom(22, "single", 100.0, false, true);
        System.out.println("room details:\n");
        sr.display();
        System.out.println("\nfinal price for 10 days of stay: "+sr.calculate_tarrif(10));
        
    }
    
}
