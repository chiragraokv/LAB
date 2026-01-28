
/*
Topics Covered
• Synchronization methods
• Synchronization blocks
• Deadlock
• Inter-thread communication (wait(), notify()) 
*/
/*Design and implement a Java-based hotel room management application that
simulates concurrent room booking and room release operations using
multiple threads. The system must ensure data consistency when multiple
customers attempt to book or release rooms simultaneously. A hotel has a limited
number of rooms. Multiple customer threads attempt to book rooms at the same
time. If no rooms are available, the booking thread must wait.
When a room is released by another thread, the waiting booking thread must be
notified and allowed to proceed */
package Week04;


class Room_database{
    boolean[] r;
    Room_database(int no_R){
        r = new boolean[no_R];
        for(int i=0;i<no_R;i++){
            r[i] = true;
        }
    }                                           
    public synchronized void book_room(int r_number){
        try{
            while(!r[r_number]){
                System.out.println(" Customer has to wait for room "+ r_number);
                wait();
            }
    
           System.out.println("Booked room "+ r_number);
           r[r_number] =false;
        }
        catch (InterruptedException e) {
            System.out.println("Booking interrupted");
        }
    }

    public synchronized void release_room(int r_no){
        r[r_no] = true;
        System.out.println(r_no +"  Room is available");
        notify();
    }

 
}
class Booking implements Runnable{
    private int room_no;
    private Room_database rdb;
    Booking(int rn, Room_database db){
        rdb = db;
        room_no = rn; 
    }
    @Override
    public void run(){

            System.out.println("Thread Running: "+Thread.currentThread()+" Service: booking "+ room_no);
            rdb.book_room(room_no);

    }
}

class Vaccate implements Runnable{
    private int room_no;
    private Room_database rdb;
    Vaccate(int rn, Room_database db){
        rdb = db;
        room_no = rn; 
    }
    @Override
    public void run(){

            System.out.println("Thread Running: "+Thread.currentThread()+" Service: Vaccate "+ room_no);
            rdb.release_room(room_no);

    }
}

public class H_b {
    public static void main(String[] args) {
        Room_database db = new Room_database(3);
        
        Thread t1 = new Thread(new Booking(0, db));
        Thread t2 = new Thread(new Booking(1, db));
        Thread t6 = new Thread(new Booking(0, db));
        Thread t3 = new Thread(new Vaccate(0, db));
        Thread t4 = new Thread(new Vaccate(0, db));
        Thread t5 = new Thread(new Vaccate(1, db));
        t1.start();
        t2.start();
        t6.start();
        t3.start();
        t5.start();
        t4.start();
    }
    
}
/*
Thread Running: Thread[#25,Thread-4,5,main] Service: Vaccate 0
Thread Running: Thread[#22,Thread-1,5,main] Service: booking 1
Thread Running: Thread[#24,Thread-3,5,main] Service: Vaccate 0
Thread Running: Thread[#23,Thread-2,5,main] Service: booking 0
Thread Running: Thread[#26,Thread-5,5,main] Service: Vaccate 1
Thread Running: Thread[#21,Thread-0,5,main] Service: booking 0
0  Room is available
Booked room 0
1  Room is available
 Customer has to wait for room 0
0  Room is available
Booked room 1
Booked room 0
*/
