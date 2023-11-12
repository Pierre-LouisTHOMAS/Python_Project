-- Inserting data into the User table
-- INSERT INTO User (First_Name, Last_Name, Type, Category, Email, Password)
-- VALUES ('Pilou', 'Thomas', 'Employee', 'NULL', 'pl.pl@pl.com', '123'),
--       ('Tryst', 'Dubois', 'Member', 'regular', 'tryst.tryst@tryst.com', '1234'),
--       ('Eva', 'Eva', 'Guest', 'NULL', 'eva.eva@eva.com', '12'),
--       ('Charlie', 'Moreau', 'Member', 'senior', 'charlie.moreau@example.com', 'charlie123'),
--       ('David', 'Petit', 'Member', 'child', 'david.petit@example.com', 'david456'),
--       ('Frank', 'Roux', 'Member', 'regular', 'frank.roux@example.com', 'frank789'),
--       ('Grace', 'Vidal', 'Guest', 'NULL', 'grace.vidal@example.com', NULL),
--       ('Hugo', 'Fontaine', 'Member', 'senior', 'hugo.fontaine@example.com', 'hugo1011'),
--       ('Iris', 'Mercier', 'Guest', 'NULL', 'iris.mercier@example.com', NULL),
--       ('Jack', 'David', 'Member', 'regular', 'jack.david@example.com', 'jack1213');

-- Inserting data into the Flight table
INSERT INTO Flight (Departure_Date, Arrival_Date, Departure_Airport, Arrival_Airport, Price)
VALUES ('2023-11-01 10:00:00', '2023-11-01 12:30:00', 'Paris CDG', 'London Heathrow', 100.50),
       ('2023-11-02 15:30:00', '2023-11-02 18:00:00', 'New York JFK', 'Paris CDG', 350.75),
       ('2023-11-03 20:00:00', '2023-11-04 08:00:00', 'Tokyo Haneda', 'Los Angeles LAX', 550.20),
       ('2023-11-04 06:00:00', '2023-11-04 09:00:00', 'Berlin Tegel', 'Rome Fiumicino', 120.80),
       ('2023-11-05 12:00:00', '2023-11-05 14:30:00', 'Sydney Kingsford', 'Auckland', 200.60),
       ('2023-11-06 13:00:00', '2023-11-06 16:30:00', 'Cairo', 'Johannesburg', 250.10),
       ('2023-11-07 09:00:00', '2023-11-07 11:30:00', 'Moscow Sheremetyevo', 'Istanbul', 170.90),
       ('2023-11-08 07:00:00', '2023-11-08 10:00:00', 'Rio de Janeiro', 'Buenos Aires', 180.00),
       ('2023-11-09 18:00:00', '2023-11-09 21:00:00', 'Beijing', 'Seoul Incheon', 220.35),
       ('2023-11-10 16:30:00', '2023-11-10 20:00:00', 'Mumbai', 'Dubai', 300.50);

-- Inserting data into the Reservation table
-- Assuming User_ID and Flight_ID auto-increment starts from 1
INSERT INTO Reservation (User_ID, Flight_ID, Number_of_Tickets, Total_Payment)
VALUES (1, 1, 2, 201.00),
       (2, 2, 1, 350.75),
       (3, 3, 4, 2200.80),
       (4, 4, 3, 362.40),
       (5, 5, 2, 401.20),
       (6, 6, 1, 250.10),
       (7, 7, 3, 512.70),
       (8, 8, 4, 720.00),
       (9, 9, 2, 440.70),
       (10, 10, 1, 300.50);
