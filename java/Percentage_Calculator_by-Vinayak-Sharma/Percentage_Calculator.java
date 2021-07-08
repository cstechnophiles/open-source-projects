import java.util.Scanner;
public class Percentage_Calculator {
    

    public static void main(String[] args) {


        System.out.println("percentage calculator");
        Scanner sc = new Scanner(System.in);
        System.out.println("score in maths");
         float maths = sc.nextFloat();
        System.out.println("score in science");
         float science = sc.nextFloat();
       System.out.println("score in sst");
         float sst = sc.nextFloat() ;
        System.out.println("score in english");
         float english = sc.nextFloat() ;
        System.out.println("score in punjabi");
         float punjabi = sc.nextFloat();

         float marks_obtained = maths + science + sst + english + punjabi ;
         float total_marks = 500;
        float percentage = marks_obtained / total_marks * 100 ;
        System.out.println("you scored"+" "+ percentage +" "+ "marks in exam");
        



    }

}