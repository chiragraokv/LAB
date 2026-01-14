/*2.Create a base class named Room to represent general room details in a hotel. The class should contain data members such as room number, room type, and base price.
 Implement multiple constructors (constructor overloading) in the Room class to initialize room objects in different ways, such as:
 i.	Initializing only the room number and type
ii.	Initializing room number, type, and base price
iii.Create a derived class named DeluxeRoom that inherits from the Room class using single inheritance. 
        The derived class should include additional data members such as free Wi-Fi availability and complimentary breakfast. 
        Implement appropriate constructors in the derived class that invoke the base class constructors using the super keyword.
iv.Create a main class to instantiate objects of both Room and DeluxeRoom using different constructors and display the room details. 
        This application should clearly illustrate constructor overloading and inheritance.
 */
package Week01;

import java.util.DuplicateFormatFlagsException;

public class Room {
    private int roomno;
    private String type;
    private double base_price = 100.00;

    Room(int roomno, String type){
        this.roomno = roomno;
        this.type = type;
    }
    Room(int roomno, String type, double base){
        this.roomno = roomno;
        this.type = type;
        this.base_price = base;
    }

    public void display(){
        System.out.println("Room no: "+roomno+"\ntype : "+type+"\nPrice : "+base_price);
    }
    double put_base_price(){
        return base_price;
    }
    
}

class DeluxeRoom extends Room{
    private boolean wifi;
    private boolean breakfast;

    DeluxeRoom(int roomno, String type){
        super(roomno, type);
    }
    DeluxeRoom(int roomno, String type, double base){
        super(roomno, type, base);
    }
    DeluxeRoom(int roomno, String type, double base,boolean wifi, boolean breakfast){
        super(roomno, type, base);
        this.breakfast = breakfast;
        this.wifi = wifi;
    }
    public void display(){
        super.display();
        System.err.println("wifi available: "+wifi+"\nbreakfast available : "+breakfast);
    }

}

class demoRoom{
    public static void main(String[] args) {
        Room r = new Room(11, "single");
        Room a = new Room(22, "Double",33.44);
        DeluxeRoom dr = new DeluxeRoom(0, "ultra",33.4,true,true);
        r.display();
        a.display();
        dr.display();
    }
}
