package src;

import java.util.*;

class CustomerFactory {

    private final static Integer RANDOM_CELL= 30 ;

    private final static Integer ELDER_RATE = 20;

    private final static Integer PRODUCTS_CELL = 20;

    private final static Integer CUSTOMER_NUMBERS = 10;

    public static Integer customerNumbers = 0;

    // generate 5
    static List<Customer> generateCustomers(){
        List<Customer> customerList = new LinkedList<>();

        if(customerNumbers >= 100){
            return customerList;
        }

        Set<Integer> s = new HashSet<>();
        // generate fixed size customer without time arrive conflict
        while(s.size() != CUSTOMER_NUMBERS){
            s.add(1+ (int)(Math.random() * RANDOM_CELL));
        }

        for(Integer i:s){
            Customer customer = new Customer(i,(int)(Math.random()*PRODUCTS_CELL), (int) (Math.random() * 100) <= ELDER_RATE);
            customerList.add(customer);
            customerNumbers += 1;
        }
        for(Customer c:customerList){
            System.out.println(c.toString());
        }
        return customerList;
    }
}

