public enum TransactionType {
  BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER
}

public enum TransactionStatus {
  SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE
}

public enum CustomerStatus {
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, CLOSED, UNKNOWN
}

public class Address {
  private String streetAddress;
  private String city;
  private String state;
  private String zipCode;
  private String country;
}





# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Customer:
  def __init__(self, name, address, email, phone, status):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__status = status
    self.__card = Card()
    self.__account = Account

  def make_transaction(self, transaction):
    None

  def get_billing_address(self):
    None


class Card:
  def __init__(self, number, customer_name, expiry, pin):
    self.__card_number = number
    self.__customer_name = customer_name
    self.__card_expiry = expiry
    self.__pin = pin

  def get_billing_address(self):
    None


class Account:
  def __init__(self, account_number):
    self.__account_number = account_number
    self.__total_balance = 0.0
    self.__available_balance = 0.0

  def get_available_balance(self):
    return self.__available_balance


class SavingAccount(Account):
  def __init__(self, withdraw_limit):
    self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
  def __init__(self, debit_card_number):
    self.__debit_card_number = debit_card_number





class Bank:
  def __init__(self, name, bank_code):
    self.__name = name
    self.__bank_code = bank_code

  def get_bank_code(self):
    return self.__bank_code

  def add_atm(self, atm):
    None


class ATM:
  def __init__(self, id, location):
    self.__atm_id = id
    self.__location = location

    self.__cash_dispenser = CashDispenser()
    self.__keypad = Keypad()
    self.__screen = Screen()
    self.__printer = Printer()
    self.__check_deposit = CheckDeposit()
    self.__cash_deposit = CashDeposit

  def authenticate_user(self):
    None

  def make_transaction(self, customer, transaction):
    None


class CashDispenser:
  def __init__(self):
    self.__total_five_dollar_bills = 0
    self.__total_twenty_dollar_bills = 0

  def dispense_cash(self, amount):
    None

  def can_dispense_cash(self):
    None


class Keypad:
  def get_input(self):
    None


class Screen:
  def show_message(self, message):
    None

  def get_input(self):
    None


class Printer:
  def print_receipt(self, transaction):
    None

# from abc import ABC, abstractmethod


class DepositSlot(ABC):
  def __init__(self):
    self.__total_amount = 0.0

  def get_total_amount(self):
    return self.__total_amount


class CheckDepositSlot(DepositSlot):
  def get_check_amount(self):
    None


class CashDepositSlot(DepositSlot):
  def receive_dollar_bill(self):
    None







public abstract class Transaction {
  private int transactionId;
  private Date creationTime;
  private TransactionStatus status;
  public boolean makeTransation();
}

public class BalanceInquiry extends Transaction {
  private int accountId;
  public double getAccountId();
}

public abstract class Deposit extends Transaction {
  private double amount;
  public double getAmount();
}

public class CheckDeposit extends Deposit {
  private String checkNumber;
  private String bankCode;

  public String getCheckNumber();
}

public class CashDeposit extends Deposit {
  private double cashDepositLimit;
}

public class Withdraw extends Transaction {
  private double amount;
  public double getAmount();
}

public class Transfer extends Transaction {
  private int destinationAccountNumber;
  public int getDestinationAccount();
}








