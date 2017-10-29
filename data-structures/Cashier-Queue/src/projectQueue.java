package src;


import java.util.Collections;
import java.util.List;

public class projectQueue {
    
    public static boolean isAllFinished(List<Cashier<Customer>> cashiers) {
        for (Cashier cashier : cashiers) {
            if(cashier.getCurrentQueue().size() != 0)
                return false;
        }
        return true;
    }

    public static void intoQue(List<Customer>customers, List<Cashier<Customer>>cashiers){
        for(Customer customer:customers){
            Collections.sort(cashiers);
            customer.setAllTime(cashiers.get(0).getEfficiency());
            cashiers.get(0).getCurrentQueue().add(customer);
        }
    }

    public static void flushCashier(List<Cashier<Customer>> cashiers){
        for(Cashier<Customer> cashier: cashiers){
            cashier.setTotalTime(cashier.getTotalTime() + 1);
            for(Customer customer:cashier.getCurrentQueue()){
//                (Customer)customer
                customer.flushAllTime();
            }
        }
    }

    public static void checkPeek(List<Cashier<Customer>> cashiers){
        for(Cashier<Customer> cashier: cashiers){
            if(cashier.getCurrentQueue().peek().getAllTime() == 0){
                cashier.getCurrentQueue().remove();
            }
        }
    }

    public static void main(String[] args) {

        //loop for 100 customers;
        //loop 10 customers , 1 will be elder.

        //loop for 10 cashiers.
        //
//        CustomerFactory.generateCustomers();
        List<Cashier<Customer>> cashiers = CashierFactory.generateCashiers();

        int time = 0;
        while(isAllFinished(cashiers)){
            // every second add every cashier's time
            time += 1;
            // flush cashier work time and top customer's waittime
            flushCashier(cashiers);

            // FIXME: 29/10/17 haven't implement jump line
        }

    }
}
