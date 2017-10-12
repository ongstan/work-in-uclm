package org.uclm;

import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static String minus(String st, int steps) {
        return st.substring(0, st.length() - steps);
    }

    public static void main(String[] args) {

        String src = "abc xyz + 1 -";

        StringTokenizer st = new StringTokenizer(src);

        Stack<String> stack = new Stack<>();

        String finalString = "";

        while (st.hasMoreElements()) {
            String currentString = (String) st.nextElement();
            char firstLetterOfCurrentString = currentString.charAt(0);

            if ((int) firstLetterOfCurrentString <= 45) {
                if (firstLetterOfCurrentString == '+') {
                    String tmpString = stack.pop();
                    finalString += stack.pop()+tmpString ;
                } else if (firstLetterOfCurrentString == '-') {
                    finalString = minus(finalString, Integer.parseInt(stack.pop()));
                }
            } else {
                stack.push(currentString);
            }
        }
        System.out.println(finalString);
    }
}
