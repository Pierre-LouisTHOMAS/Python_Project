CREATE DATABASE FlightReservation; -- Creating the database

USE FlightReservation; -- Selecting the database

-- Creating the Client table
CREATE TABLE Client (
    Client_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Type ENUM('Guest', 'Member') NOT NULL,
    Category ENUM('regular', 'senior', 'child', 'NULL') DEFAULT 'NULL',
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255)
);

-- Creating the Flight table
CREATE TABLE Flight (
    Flight_ID INT PRIMARY KEY AUTO_INCREMENT,
    Departure_Date DATETIME NOT NULL,
    Arrival_Date DATETIME NOT NULL,
    Departure_Airport VARCHAR(255) NOT NULL,
    Arrival_Airport VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL
);

-- Creating the Employee table
CREATE TABLE Employee (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL
);

-- Creating the Reservation table
CREATE TABLE Reservation (
    Reservation_ID INT PRIMARY KEY AUTO_INCREMENT,
    Client_ID INT,
    Flight_ID INT,
    Number_of_Tickets INT NOT NULL,
    Total_Payment DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID),
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID)
);
