CREATE TABLE Account_Type(
    account_Type_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    account_Type_Name VARCHAR(128) NOT NULL,
    account_Type_Description VARCHAR(128) NOT NULL,
    interest_Rate  NOT NULL
);

CREATE TABLE Transaction_Type(
    transaction_Type_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    transaction_Type VARCHAR(128) NOT NULL
);

CREATE TABLE Account(
    account_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    account_Name VARCHAR(128) NOT NULL,
    account_Type_ID INTEGER NOT NULL,
    balance INTEGER NOT NULL,
    FOREIGN KEY(account_Type_ID) REFERENCES Account_Type(account_Type_ID)
);

CREATE TABLE Customer(
    customer_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    customer_Name VARCHAR(128) NOT NULL,
    customer_Address VARCHAR(128) NOT NULL,
    gender VARCHAR(128) NOT NULL,
    account_ID INTEGER NOT NULL,
    ssn INTEGER NOT NULL,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(128) NOT NULL,
    FOREIGN KEY(account_ID) REFERENCES Account(account_ID)
);

CREATE TABLE account_Transaction(
    transaction_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    transaction_Type_ID INTEGER NOT NULL,
    date VARCHAR(128) NOT NULL,
    amount INTEGER NOT NULL,
    transfer_Account_ID INTEGER,
    transfer_Account_Name VARCHAR(128),
    account_ID INTEGER NOT NULL,
    FOREIGN KEY(transaction_Type_ID) REFERENCES Transaction_Type(transaction_Type_ID),
    FOREIGN KEY(account_ID) REFERENCES Account(account_ID)
);

INSERT INTO Account_Type(account_Type_Name, account_Type_Description, interest_Rate)
    VALUES("Checking", "An account that store money for everyday personal use", 0);
INSERT INTO Account_Type(account_Type_Name, account_Type_Description, interest_Rate)
    VALUES("Saving", "An account that store money for long term saving", 5);
INSERT INTO Account_Type(account_Type_Name, account_Type_Description, interest_Rate)
    VALUES("Business", "An account that handles business transactions that has more than $10,000", 2);


INSERT INTO Transaction_Type(transaction_Type)
    VALUES("Deposit");
INSERT INTO Transaction_Type(transaction_Type)
    VALUES("Withdraw");
INSERT INTO Transaction_Type(transaction_Type)
    VALUES("Wire transfer");

INSERT INTO Account(account_Type_ID, account_Name, balance)
    VALUES(1,"Jordi", 2500);
INSERT INTO Account(account_Type_ID, account_Name, balance)
    VALUES(1, "Stacey", 4000);
INSERT INTO Account(account_Type_ID, account_Name, balance)
    VALUES(2, "Arthur", 6000);
INSERT INTO Account(account_Type_ID, account_Name, balance)
    VALUES(3, "Jasmin", 15000);

INSERT INTO Customer(customer_Name, customer_Address, gender, account_ID, ssn, password, email)
    VALUES("Jordi Greaves", "2273 Grim Avenue”, “male”, 1, 680237360, “hardtoguesspassword”, “Jordigreaves@email.com”);
INSERT INTO Customer(customer_Name, customer_Address, gender, account_ID, ssn, password, email)
    VALUES(“Stacey Whitaker”, “3966 Bolman Court”, “female”, 2, 425050469, “nevergoingtoguess”, “Staceywhitaker@email.com”);
INSERT INTO Customer(customer_Name, customer_Address, gender, account_ID, ssn, password, email)
    VALUES(“Arthur Bowden”, “2963 West Fork Drive”, “male”, 3, 541689664, “icantremember”, “Authurbowden@email.com”);
INSERT INTO Customer(customer_Name, customer_Address, gender, account_ID, ssn, password, email)
    VALUES(“Jasmin Ray”, “4529 Werninger Street”, “female”, 4, 520767522, “omgpassword”, “Jamsminray@email.com”);

INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(1, "3/15/2020", 375, NULL, NULL, 1);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(1, "5/20/2020", 550, NUll, NULL, 2);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(1, "6/1/2020", 3000, NUll, NULL, 3);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(2, "8/27/2020", 200, NULL, NULL, 1);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(2, "9/17/2020", 500, NULL, NULL, 2);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(2, "1/29/2021", 1000, NULL, NULL, 1);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(3, "2/25/2021", 800, 2, "Stacey", 1);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(3, "4/28/2021", 670, 1, "Jordi", 2);
INSERT INTO account_Transaction(transaction_Type_ID, date, amount, transfer_Account_ID, transfer_Account_Name, account_ID)
    VALUES(3, "6/17/2021", 2000, 4, "Jasmin", 3);