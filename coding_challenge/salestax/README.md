## Sales Tax Calculator

This application helps you calculate the sales tax and create receipt for your purchase.

### Setup
#### Dependency
Java SE 8 or higher 
#### Compiling and running the current system
- First, unzip the salestax.zip file into a working directory. In order to compile the system, open a 
command prompt window (or start a Linux terminal), change the working directory to "salestax" and type the following:
```
javac ./src/*.java -d ./bin/
```
The compile command above creates the class files. 
- After that, you can run the system by typing:
```
java -classpath ./bin Shopping your_shopping_list_file.txt your_receipt_output_file.txt
```
The first parameter is your shopping list file and the second parameter is receipt output file name. 

You could also run the application with 
```
java -classpath ./bin Shopping
```
Then the default parameter is "shopping_list_1.txt" and "src/receipt.txt".

Alternatively, you could run the application using the batch file. 
```
sh run.sh
```
#### Testing
Try the following 3 input file for testing.
- data/shopping_list_1.txt 
- data/shopping_list_2.txt 
- data/shopping_list_3.txt 

### Input
It reads products from a given txt file with the following format:

```text
1 imported bottle of perfume at 27.99 1 bottle of perfume at 18.99
1 packet of headache pills at 9.75
1 imported box of chocolates at 11.25
```

### Output
It returns the following output for the above example.
The receipt includes total cost of each product, total sales tax for all items and total cost of current purchase.
```text
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68
```

### DataBase
- As the sales tax rate is different according to the item category, you might want to help the application find out 
the specific category for your items. The application reads data from "data/products.txt" for item category. This first 
column is category name and the second is product name. Add your new items with the same format into the file as needed. 

Category|item
--|--
Book | book 
Food | chocolate bar 
Food | chocolates 
Medical | headache pills 
Others | music CD 
Others | perfume 

- The database also stores units for all items. Add your new unit in "data/units.txt" file as following format 
(one unit per line):
```text
bottle
box
packet
``` 
