import java.util.Scanner;

public class Calculadora1 {

    public float sumar(float a, float b) {
        return a + b;
    }

    public float restar(float a, float b) {
        return a - b;
    }

    public float multiplicar(float a, float b) {
        return a * b;
    }

    public float dividir(float a, float b) {
        return a / b;
    }

    public float modulo(float a, float b) {
        return a % b;
    }

    public double potencia(float a, float b) {
        return Math.pow(a, b);
    }

    public double coseno(float a) {
        return Math.cos(a);
    }

    public double seno(float a) {
        return Math.sin(a);
    }

    public static void main(String[] args) {

        Scanner nume = new Scanner(System.in);

        Calculadora1 calculadora1 = new Calculadora1();

        System.out.print("Digite la operacion (+, -, *, /, %, pow, cos, sin): ");
        String operacion = nume.next();

        System.out.println("Digite el primer valor");
        float a = nume.nextFloat();

        System.out.println("Digite el segundo valor");
        float b = nume.nextFloat();

        if (operacion.equals("+")) {
            System.out.println(calculadora1.sumar(a, b));
        }
        else if (operacion.equals("-")) {
            System.out.println(calculadora1.restar(a, b));
        }
        else if (operacion.equals("*")) {
            System.out.println(calculadora1.multiplicar(a, b));
        }
        else if (operacion.equals("/")) {
            System.out.println(calculadora1.dividir(a, b));
        }
        else if (operacion.equals("%")) {
            System.out.println(calculadora1.modulo(a, b));
        }
        else if (operacion.equals("pow")) {
            System.out.println(calculadora1.potencia(a, b));
        }
        else if (operacion.equals("cos")) {
            System.out.println(calculadora1.coseno(a));
        }
        else if (operacion.equals("sin")) {
            System.out.println(calculadora1.seno(a));
        }
    }
}