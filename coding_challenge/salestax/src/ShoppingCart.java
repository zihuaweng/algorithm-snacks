/*
 * @(#)ShoppingCart.java
 *
 * Copyright: Copyright (c) 2020 Zihua Weng (zihuaw2@uci.edu)
 *
 */

import java.util.ArrayList;
import java.util.List;

/**
 * This class represents the collection of product records. This class contains an ArrayList which maintains
 * all Product brought, total cost and total sales tax of this shopping.
 */
public class ShoppingCart {
    // totalPrice represents price of all products excluding their sales tax.
    private double totalPrice = 0.00;
    private double totalSalesTax = 0.00;
    private List<Product> shoppingCart = new ArrayList<>();

    /**
     * Add products into shopping cart.
     *
     * @param product a Product instance.
     */
    public void addProduct(Product product) {
        shoppingCart.add(product);
        totalPrice += product.getPrice();
        totalSalesTax += product.getSalesTax();
    }

    public double getTotalPrice() {
        return totalPrice;
    }

    public double getTotalSalesTax() {
        return totalSalesTax;
    }

    /**
     * Return total price and total sales tax as totalCost.
     */
    public double getTotalCost() {
        return totalPrice + totalSalesTax;
    }

    public List<Product> getShoppingCart() {
        return shoppingCart;
    }
}
