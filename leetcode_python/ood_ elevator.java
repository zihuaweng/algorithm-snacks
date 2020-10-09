public class User {
private name;
public pressButton(int toFloor) {
    Request req = new Request( toFloor);
    RequestProcessCenter  center = RequestProcessCenter.getInstance();
    center.addRequest(req);
}
}
public class Request {
    private int toFloor;
    public Request(int _toFloor) {
        toFloor = _toFloor;
    }
    public getToFloor() {
        return toFloor;
}
}
public class Elevator {
    public static Elevator instance = null;
    private int currentFloor;
    public static Elevator( ) {
        if (instance == null) {  // late loading and eager loading
                    // connection pool
            synchronized (Elevator.class) {
                instance = new Elevator();
}
}
return instance;
}
public getInstance() {
    if (instance == null) {
            synchronized (SingletonDemo.class) {
                instance = new Elevator();
}
}
return instance;
}
public getCurrentFloor() {
    return currentFloor;
}
public moveToTargetFloor(int toFloor) {
    currentFloor = toFloor;
}
public void moveUp();
public void moveDown();
}
public RequestProcessCenter implements runnable {
    public LinkedList<Request> queue;
public RequestProcessCenter( ) {
        queue = new LinkedList<Request>( );
}
public void run() {
        while ( true ) {
            processRequest( )
}
}
public void addRequest(Request request) {
    queue.add(request);
}
public void removeRequest(Request request) {
    queue.remove(request);
}
public Request getNextRequest( ) {
    Request shortestReq = null;
    int shortest = Integer.MAX_VALUE;
    int curFloor = Elevator.getInstance( ).getCurrentFloor( );
    for (Request item : queue) {
        int distance = Math.abs(curFloor - item.getToFloor( ) );
        if (distance < shortest) {
            shortest = distance;
            shortestReq = item;
}
}
return shortestReq;
}
public void processRequest( ) {
    Request req = getNextRequest( );
if (req != null) {
        int toFloor = req.getToFloor( );
        Elevator.getInstance.moveToTargetFloor( toFloor);
        queue.remove(req);
}
   
}
}

