package Week03;

import java.security.PrivateKey;

/* 
Design and implement a Java application to simulate a Hotel Room Service 
Management System where multiple service requests are handled concurrently 
using multithreading. 
 
i.In a hotel, different room service tasks such as room cleaning, food delivery, and 
maintenance may occur at the same time. To efficiently manage these tasks, the 
application should create separate threads for each service request so that they can 
execute concurrently rather than sequentially. 
ii.Create individual threads for different service operations using Java thread creation 
techniques (Thread class or Runnable interface). Each thread should simulate a service 
task by displaying status messages and pausing execution using the sleep() method to 
represent processing time. 
iii.The main program should start multiple threads simultaneously and demonstrate 
concurrent execution of hotel service tasks.
*/
class Service implements Runnable{
    private String name;
    private int room;
    private long time;
    Service( String name, int r, long t){
        this.name = name;
        room =r;
        time =r;
    }
    @Override
    public void run() {
        try{
            System.out.println("Thread Running: "+Thread.currentThread()+" Service: "+name+ "Room no :"+room);
            for( int i =1;i<5;i++)
            Thread.sleep(time);
            }
            catch(InterruptedException e){
                System.out.println("Thread interruted");
            }
        System.out.println("Done service:\t"+ name + "\tfor "+room);
    }
}

class Process_payment implements Runnable{
    int mode;
    long sleep;
    int room;
    Process_payment(int step,int r){
        mode = step;
        room =r;
        if(step == 0){
            sleep = 1000;
        }
        if(step == 1){
            sleep = 30000;
        }
        else{
            sleep = 5000;
        }
    }
    public void run(){
        try{
            System.out.println("Thread Running: "+Thread.currentThread()+" Step: "+mode+ "Room no :"+room);
            for( int i =0;i<mode;i++)
            Thread.sleep(sleep);
            }
            catch(InterruptedException e){
                System.out.println("Thread interruted");
            }
        System.out.println("Done processing step\t:"+mode+ "\tfor "+ room);
        }
}

public class Hotel_room_service {
    public static void main(String[] args){
    Thread t1 = new Thread(new Service("cleaning", 10,100000));
    Thread t2 = new Thread(new Service("Food delivery",100,1));;
    Thread t3 = new Thread(new Service("Maintainance",101,1));
    Thread t4 = new Thread(new Process_payment(2,101));
    Thread t5 = new Thread(new Process_payment(1,131));
    Thread t6 = new Thread(new Process_payment(0,102));
    Thread t7 = new Thread(new Process_payment(2,109));
    t3.setPriority(Thread.MAX_PRIORITY);
    t1.start();
    t2.start();
    try{
    t2.join();
    }catch(InterruptedException e){
        System.out.println(e);
    }
    t3.start();
    t4.start();;
    t5.start();
    t6.start();
    t7.start();
    }
    
}
/*
Thread Running: Thread[#22,Thread-1,5,main] Service: Food deliveryRoom no :100
Thread Running: Thread[#21,Thread-0,5,main] Service: cleaningRoom no :10
Done service:   cleaning        for 10
Done service:   Food delivery   for 100
Thread Running: Thread[#23,Thread-2,10,main] Service: MaintainanceRoom no :101
Thread Running: Thread[#24,Thread-3,5,main] Step: 2Room no :101
Thread Running: Thread[#25,Thread-4,5,main] Step: 1Room no :131
Thread Running: Thread[#26,Thread-5,5,main] Step: 0Room no :102
Done processing step    :0      for 102
Done service:   Maintainance    for 101
Done processing step    :2      for 101
Done processing step    :1      for 131
PS C:\Users\Student\Documents\AIML_B
*/