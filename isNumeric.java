import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        try{
        Double.parseDouble(s); 
            System.out.println("Yes");
        
    } catch (NumberFormatException | NullPointerException | InputMismatchException nfe) {
            System.out.println("No");
        
                       
        }
        
        
        
    }
}