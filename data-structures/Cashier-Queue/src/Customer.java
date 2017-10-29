package src;

public class Customer  {

    private String id;

    private int arriveTime;

    private int originArriveTime;

    private int products;

    private boolean isElder;

    private int allTime;

    public Customer(int arriveTime, int products, boolean isElder) {
        this.arriveTime = arriveTime;
        this.originArriveTime = arriveTime;
        this.products = products;
        this.isElder = isElder;
        this.id= (isElder ? "C" : "E") + (isElder ? 2 : 1) * 22 + products * 10 + arriveTime * 20;
    }

    String getId() {
        return id;
    }

    public int getArriveTime() {
        return arriveTime;
    }

    public int getOriginArriveTime() {
        return originArriveTime;
    }

    public int getProducts() {
        return products;
    }

    public int getAllTime() {
        return allTime;
    }

    public void setAllTime(int efficiency) {
        this.allTime = this.products * efficiency;
    }

    public void flushAllTime(){
        this.allTime -= 1;
    }

    public boolean isElder() {
        return isElder;
    }


    @Override
    public String toString() {
        return "Customer{" +
                "id='" + id + '\'' +
                ", arriveTime=" + arriveTime +
                ", originArriveTime=" + originArriveTime +
                ", products=" + products +
                ", isElder=" + isElder +
                '}';
    }
}
