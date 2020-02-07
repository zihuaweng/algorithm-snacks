/*
 * @(#)Shopping.java
 *
 * Copyright: Copyright (c) 2020 Zihua Weng (zihuaw2@uci.edu)
 *
 */

import java.io.*;
import java.util.List;
import java.util.StringJoiner;

/**
 * Class to hold application main method.
 */
public class Shopping {

    // Define the default files.
    private static final String DATA_DIR = "./data/";
    private static final String PRODUCTS_FILE = DATA_DIR + "products.txt";
    private static final String RECEIPT_FILE = DATA_DIR + "receipt.txt";
    private static final String SHOPPING_LIST_FILE = DATA_DIR + "shopping_list_1.txt";
    private static final String UNITS_FILE = DATA_DIR + "units.txt";

    /**
     * Read shopping lists and return the sales tax. One shopping list txt file is expected, which
     * contains one product record per line.
     * For example:
     * <p>
     * <code>1 imported box of chocolates at 10.00</code>
     * <p>
     * If no shopping list provided, then the application reads the default file "product_list.txt".
     *
     * @param args product list txt file.
     */
    public static void main(String[] args) throws IOException {
        String shoppingListFilePath = SHOPPING_LIST_FILE;
        String receiptFilePath = RECEIPT_FILE;

        // Check the number of parameters.
        if (args.length == 2) {
            shoppingListFilePath = args[0];
            receiptFilePath = args[1];
        } else if (args.length == 1) {
            shoppingListFilePath = args[0];
        }

        // Check if input files exists.
        if (!new File(shoppingListFilePath).exists()) {
            System.err.println("Could not find " + shoppingListFilePath);
        }

        // Initialize the product database.
        DataBase db;
        db = new DataBase(PRODUCTS_FILE, UNITS_FILE);

        // Initialize the shopping cart.
        ShoppingCart shoppingCart = new ShoppingCart();

        // Open the given shopping list txt file.
        BufferedReader productListFile = new BufferedReader(new FileReader(shoppingListFilePath));

        // Put products in shopping cart.
        while (productListFile.ready()) {
            shoppingCart.addProduct(new Product(db, productListFile.readLine()));
        }

        // Close the product list file.
        productListFile.close();

        // Check out and print the
        checkOut(shoppingCart, receiptFilePath);
    }

    /**
     * Check out for shopping receipt.
     * The receipt includes the name of all the items and their price (including tax),
     * finishing with the total cost of the items, and the total amounts of sales taxes paid.
     *
     * @param shoppingCart ShoppingCart object contains products, tax and prices.
     */
    private static void checkOut(ShoppingCart shoppingCart, String receiptFileName) throws IOException {
        // Get shopping items list
        List<Product> productList = shoppingCart.getShoppingCart();

        // Initiate invoice output file
        FileWriter receipt = new FileWriter(receiptFileName);

        StringJoiner joiner;
        String productRecord;
        for (Product product : productList) {
            joiner = new StringJoiner(" ");
            joiner.add(Integer.toString(product.getCount()));
            if (product.isImported()) {
                joiner.add("imported");
            }
            if (!product.getUnit().equals("")) {
                joiner.add(product.getUnit()).add("of");
            }
            joiner.add(product.getName() + ":");
            joiner.add(String.format("%.2f", product.getCost()));

            productRecord = joiner.toString();
            System.out.println(productRecord);

            receipt.write(productRecord + "\n");
        }
        productRecord = "Sales Taxes: " + String.format("%.2f", shoppingCart.getTotalSalesTax()) + "\n" +
                "Total: " + String.format("%.2f", shoppingCart.getTotalCost()) + "\n";
        System.out.println(productRecord);
        receipt.write(productRecord);
        receipt.close();
    }

}
