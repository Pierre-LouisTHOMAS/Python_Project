CREATE DATABASE AirlineDatabase; -- Creating the database

USE AirlineDatabase; -- Selecting the database

-- Creating the Client table
CREATE TABLE User (
    User_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Type ENUM('Guest', 'Member', 'Employee') NOT NULL,
    Category ENUM('regular', 'senior', 'child', 'NULL') DEFAULT 'NULL',
    Discount DECIMAL(5,2),
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255)
);
UPDATE User SET Discount = 40.00 WHERE Category = 'child';
UPDATE User SET Discount = 30.00 WHERE Category = 'senior';
UPDATE User SET Discount = 15.00 WHERE Category = 'regular';
UPDATE User SET Discount = 90.00 WHERE Type = 'Employee';

-- Creating the Flight table
CREATE TABLE Flight (
    Flight_ID INT PRIMARY KEY AUTO_INCREMENT,
    Departure_Date DATETIME NOT NULL,
    Arrival_Date DATETIME NOT NULL,
    Departure_Airport VARCHAR(255) NOT NULL,
    Arrival_Airport VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL
);

-- Creating the Reservation table
CREATE TABLE Reservation (
    Reservation_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_ID INT,
    Flight_ID INT,
    Number_of_Tickets INT NOT NULL,
    Total_Payment DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID)
);
