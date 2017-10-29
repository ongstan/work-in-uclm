package src;

import java.util.LinkedList;
import java.util.List;

public class CashierFactory {

    private static final Integer EFFICIENCY_CELL = 20;

    static List<Cashier<Customer>> generateCashiers() {
        List<Cashier<Customer>> cashiers = new LinkedList<>();

        for (int i = 0; i < 10; i++) {
            Cashier<Customer> cashier = new Cashier<Customer>(i,(int)(Math.random()*EFFICIENCY_CELL),0);
            cashiers.add(cashier);
        }

        for (Cashier cashier: cashiers){
            System.out.println(cashier.toString());
        }

        return cashiers;
    }

}
