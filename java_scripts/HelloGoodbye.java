/***************************************************************
 * Compilation: javac HelloWorld.java
 * Execution:   java  HelloWorld
 *
 * Prints "Hello name1 and name2" then on a new line "Goodbye 
 * name1 and name2".
 *
 * Input(s):
 *              string name1
 *              string name2
 *
 * Output(s):
 *             Print statement "Hello name1 and name2"
 *                             "Goodbye name1 and name2"
 *
 * % java HelloGoodbye Jack Stephanie
 * Hello Jack and Stephanie
 * Goodbye Jack and Stephanie
 *
 * Author: Jack Rossetti
 * Date:   21-09-30
 * 
 ***************************************************************/

public class HelloGoodbye {

    public static void main(String argv[]) {
	System.out.print("Hello ");
	System.out.print(argv[0]);
	System.out.print(" and ");
	System.out.print(argv[1]);
	System.out.print("\n");
	System.out.print("Goodbye ");
	System.out.print(argv[0]);
	System.out.print(" and ");
	System.out.print(argv[1]);
	System.out.print("\n");
	System.exit(0);
    }
    
}
