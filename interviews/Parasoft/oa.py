1:
 
def isAlphabitized(x, context):
    reader = BufferedReader(x.getReader())
    line = reader.readLine()     # This line reads the first line of the data but does not print it out.
    while line != None:
        Application.showMessage(reader.readLine())    # This line prints data from the second line

Correct way:

def isAlphabitized(x, context):
    reader = BufferedReader(x.getReader())
    line = reader.readLine()
    while line != None:
        Application.showMessage(line) 
        line = reader.readLine()


2:
def func(arr: list) -> int:
    res = float('inf')
    for i in range(len(arr)):
        res = max(res, arr[i]+arr[i-1])
    return res


3.
def func(n):
    prime = [2]
    num = 3
    while len(prime) < n:
        for p in prime:
            if num % p == 0:
                break
        else:
            prime.append(num)
        num += 2  # skip the even num
    return prime[-1]


4.

public class RationalNumber {
    private int numerator;
    private int denominator;

    private RationalNumber (int numerator, int denominator) {
        if (denominator == 0) {
            throw new IllegalArgumentException("Denominator could not be 0.");
        }
        if (denominator < 0) {
            numerator *= -1;
            denominator *= -1;
        }
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public int getDenominator() {
        return denominator;
    }

    public int getNumerator() {
        return numerator;
    }

    public void setDenominator(int denominator) {
        this.denominator = denominator;
    }

    public void setNumerator(int numerator) {
        this.numerator = numerator;
    }

    public void printDecimal() {
        System.out.println(String.valueOf((double) numerator / denominator));
    }

    public void printFraction() {
        System.out.println(String.format("%d / %d", numerator, denominator));
    }

    private RationalNumber add(RationalNumber num) {
        int newDenominator = denominator * num.getDenominator();
        int newNumerator = numerator * num.getDenominator() + denominator * num.getNumerator();
        return simplifiedRationalNumber(newNumerator, newDenominator);
    }

    private RationalNumber subtract(RationalNumber num) {
        int newDenominator = denominator * num.getDenominator();
        int newNumerator = numerator * num.getDenominator() - denominator * num.getNumerator();
        return simplifiedRationalNumber(newNumerator, newDenominator);
    }

    private RationalNumber multiple(RationalNumber num) {
        int newDenominator = denominator * num.getDenominator();
        int newNumerator = numerator * num.getNumerator();
        return simplifiedRationalNumber(newNumerator, newDenominator);
    }

    private RationalNumber divide(RationalNumber num) {
        int newDenominator = denominator * num.getNumerator();
        int newNumerator = numerator * num.getDenominator();
        return simplifiedRationalNumber(newNumerator, newDenominator);
    }

    private RationalNumber simplifiedRationalNumber(int numerator, int denominator) {
        int gcd = gcd(numerator, denominator);
        int newDenominator = denominator / gcd;
        int newNumerator = numerator / gcd;
        return new RationalNumber(newNumerator, newDenominator);
    }

    private int gcd(int num1, int num2) {
        if (num2 == 0) {
            return num1;
        }
        return gcd(num2, num1%num2);
    }

    public String toString() {
        return String.valueOf((double) numerator / denominator);
    }

    public static void main(String[] args) {
        RationalNumber num1 = new RationalNumber(30, -80);
        RationalNumber num2 = new RationalNumber(-5, -8);
        System.out.println(num1.add(num2));
        System.out.println(num1.subtract(num2));
        System.out.println(num1.multiple(num2));
        System.out.println(num1.divide(num2));
    }
}

