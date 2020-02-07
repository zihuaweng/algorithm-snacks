/*
 * @(#)DataBase.java
 *
 * Copyright: Copyright (c) 2020 Zihua Weng (zihuaw2@uci.edu)
 *
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;

/**
 * A <code>DataBase</code> provides access to products with their according category and unit.
 * This class include parsing in store product list and maintain a product HashMap and a unit HashSet
 * for looking up information.
 */
public class DataBase {
    private HashMap<String, String> productCategory = new HashMap<>();
    private HashSet<String> productUnit = new HashSet<>();

    /**
     * Construct a database that provides access to product and according category.
     *
     * @param productFileName the name of product file
     */
    public DataBase(String productFileName, String unitsFileName) throws IOException {
        // Open the given files
        BufferedReader objProductFile = new BufferedReader(new FileReader(productFileName));
        BufferedReader objUnitsFile = new BufferedReader(new FileReader(unitsFileName));

        // Parse file to productCategory
        String line;
        String[] parts;

        while (objProductFile.ready()) {
            line = objProductFile.readLine();
            parts = line.split(" ", 2);
            productCategory.put(parts[1], parts[0]);
        }

        // Parse file to productUnit
        while (objUnitsFile.ready()) {
            line = objUnitsFile.readLine();
            productUnit.add(line.strip());
        }

        // Close files
        objProductFile.close();
        objUnitsFile.close();
    }

    /**
     * Return product category for given product name.
     * As the product file is incomplete now, we assume that the default product category is "Others".
     */
    public String getProductCategory(String name) {
        return productCategory.getOrDefault(name, "Others");
    }

    /**
     * Return if the database contains the product.
     */
    public boolean isProductInDataBase(String name) {
        return productCategory.containsKey(name);
    }

    /**
     * Return if the given string is unit.
     */
    public boolean isUnitInDataBase(String unit) {
        return productUnit.contains(unit);
    }

    public HashMap<String, String> getProductCategory() {
        return productCategory;
    }

    public HashSet<String> getProductUnit() {
        return productUnit;
    }
}
