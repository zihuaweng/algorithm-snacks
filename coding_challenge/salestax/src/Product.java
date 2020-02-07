/*
 * @(#)Product.java
 *
 * Copyright: Copyright (c) 2020 Zihua Weng (zihuaw2@uci.edu)
 *
 */

import java.util.Arrays;

/**
 * This class represents a record of a Product. This class contains a product's information
 * and calculates the its sales salesTax.
 */
public class Product {

    private final double SALES_TAX_RATE = 0.10;
    private final double SALES_TAX_RATE_EXEMPT = 0.00;
    private final double SALES_TAX_RATE_IMPORTED = 0.05;

    private int count;
    private String name;
    private String unit = "";
    private double price;
    private String category;
    private double salesTax;
    private double salesTaxRate;
    private double importedTaxRate;
    private boolean isImported = false;

    /**
     * Constructs a product record by parsing the given string. The argument <code>sInput</code> is
     * space-separated string. The first field is the product count. The last one is the unit price.
     * Between the above two is the product name. If the product name starts with "imported" then it
     * is a imported product.
     * Here is an example:
     * <p>
     * <code>1 imported box of chocolates at 10.00</code>
     * <p>
     *
     * @param db     the DataBase object contains all product and their according category
     * @param sInput the string to be parsed representing a product record
     */
    public Product(DataBase db, String sInput) {
        String[] sInputList = sInput.split(" ");
        this.count = Integer.parseInt(sInputList[0]);
        this.price = Double.parseDouble(sInputList[sInputList.length - 1]);
        int index = 1;

        // Imported keyword is always the second word.
        if (sInputList[index].equals("imported")) {
            this.isImported = true;
            index++;
        }

        if (db.isUnitInDataBase(sInputList[index])) {
            this.unit = sInputList[index];
            // Unit is always follow by "of" in product record, so index need to add 2.
            index += 2;
        }

        this.name = String.join(" ", Arrays.copyOfRange(sInputList, index, sInputList.length - 2));
        this.category = db.getProductCategory(name);

        setTaxRates();
        calculateTax();
    }

    /**
     * Constructs a product record by parsing the given parameters.
     *
     * @param db         reference to the database object
     * @param count      number of this product
     * @param name       product name
     * @param unit       product unit
     * @param price      product unit price
     * @param isImported whether it is a imported product
     */
    public Product(DataBase db, int count, String name, String unit, double price, Boolean isImported) {
        this.count = count;
        this.name = name;
        this.unit = unit;
        this.price = price;
        this.category = db.getProductCategory(name);
        this.isImported = isImported;
        setTaxRates();
        calculateTax();
    }

    /**
     * Set sales tax and imported sales tax.
     * Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products
     * that are exempt.
     * Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
     */
    private void setTaxRates() {
        // Sales salesTax for books, food, and medical products are exempt.
        if (category.equals("Food") || category.equals("Medical") || category.equals("Book")) {
            this.salesTaxRate = SALES_TAX_RATE_EXEMPT;
        } else {
            this.salesTaxRate = SALES_TAX_RATE;
        }
        // Imported product charged additional 5 percent sales tax.
        this.importedTaxRate = (isImported) ? SALES_TAX_RATE_IMPORTED : SALES_TAX_RATE_EXEMPT;
    }

    /**
     * Calculate the total salesTax for the product and round sales tax up to the nearest 0.05.
     */
    private void calculateTax() {
        salesTax = count * price * (salesTaxRate + importedTaxRate);
        salesTax = Math.ceil(salesTax * 20) / 20.0;
    }

    public int getCount() {
        return count;
    }

    public String getName() {
        return name;
    }

    public String getUnit() {
        return unit;
    }

    public double getPrice() {
        return price;
    }

    public double getCost() {
        return price + salesTax;
    }

    public String getCategory() {
        return category;
    }

    public double getSalesTax() {
        return salesTax;
    }

    public boolean isImported() {
        return isImported;
    }
}
