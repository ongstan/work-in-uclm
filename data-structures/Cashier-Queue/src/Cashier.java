package src;

import java.util.ArrayDeque;
import java.util.Queue;

public class Cashier<T> implements Comparable<Cashier<T>> {
    private int id;
    private int efficiency;
    private int totalTime;
    private T t;
    private Queue<T> currentQueue;

    public Cashier(int id, int efficiency, int totalTime) {
        this.id = id;
        this.efficiency = efficiency;
        this.totalTime = totalTime;
        this.currentQueue = new ArrayDeque<>();
    }

    public T getT() {
        return t;
    }

    public int getID() {
        return id;
    }

    public int getEfficiency() {
        return efficiency;
    }

    public int getTotalTime() {
        return totalTime;
    }

    public Queue<T> getCurrentQueue() {
        return currentQueue;
    }

    public void setTotalTime(int totalTime) {
        this.totalTime = totalTime;
    }

    @Override
    public int compareTo(Cashier<T> o) {
        return this.currentQueue.size() - o.currentQueue.size();
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    // FIXME: 29/10/17 fix the cashier time
    @Override
    public String toString() {
        return "Cashier{" +
                "id='" + id + '\'' +
                ", efficiency=" + efficiency +
                ", totalTime=" + totalTime +
                ", currentQueue=" + currentQueue +
                '}';
    }
}

