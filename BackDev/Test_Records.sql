-- Inserting data into the Flight table
DELIMITER //

CREATE PROCEDURE InsertFlightsForNovember()
BEGIN
    DECLARE dayCounter INT DEFAULT 1;
    DECLARE flightCounter INT;
    DECLARE departureTime TIME;
    DECLARE arrivalTime TIME;
    DECLARE departureAirport VARCHAR(255);
    DECLARE arrivalAirport VARCHAR(255);
    DECLARE price DECIMAL(10,2);

    DECLARE airportList VARCHAR(255) DEFAULT 'Paris CDG,New York JFK,Tokyo Haneda,Berlin Tegel,Sydney Kingsford,Cairo,Moscow Sheremetyevo,Rio de Janeiro,Beijing,Mumbai';
    DECLARE airportArray VARCHAR(255);

    WHILE dayCounter <= 30 DO
        SET flightCounter = 1;

        WHILE flightCounter <= 10 DO
            SET departureTime = ADDTIME('06:00:00', SEC_TO_TIME(RAND() * 36000));
            SET arrivalTime = ADDTIME(departureTime, '02:00:00');

            SET departureAirport = SUBSTRING_INDEX(SUBSTRING_INDEX(airportList, ',', 1 + FLOOR(RAND() * 10)), ',', -1);
            SET arrivalAirport = SUBSTRING_INDEX(SUBSTRING_INDEX(airportList, ',', 1 + FLOOR(RAND() * 10)), ',', -1);
            WHILE arrivalAirport = departureAirport DO
                SET arrivalAirport = SUBSTRING_INDEX(SUBSTRING_INDEX(airportList, ',', 1 + FLOOR(RAND() * 10)), ',', -1);
            END WHILE;

            SET price = 100.0 + RAND() * 200;

            INSERT INTO Flight (Departure_Date, Arrival_Date, Departure_Airport, Arrival_Airport, Price)
            VALUES
                (CONCAT('2023-11-', LPAD(dayCounter, 2, '0'), ' ', departureTime),
                 CONCAT('2023-11-', LPAD(dayCounter, 2, '0'), ' ', arrivalTime),
                 departureAirport,
                 arrivalAirport,
                 price);

            SET flightCounter = flightCounter + 1;
        END WHILE;

        SET dayCounter = dayCounter + 1;
    END WHILE;
END //

DELIMITER ;

CALL InsertFlightsForNovember();


-- Inserting data into the Reservation table
-- Assuming User_ID and Flight_ID auto-increment starts from 1

-- INSERT INTO Reservation (User_ID, Flight_ID, Number_of_Tickets, Total_Payment)
-- VALUES (1, 1, 2, 546.7),
       -- (2, 2, 1, 167.72),
       -- (3, 3, 4, 1146.52),
       -- (4, 4, 3, 687.3),
       -- (5, 5, 2, 525.82),
       -- (6, 6, 1, 121.63),
       -- (7, 7, 3, 374.07),
       -- (8, 8, 4, 859.64),
       -- (9, 9, 2, 230.26),
      --  (10, 10, 1, 180.88);

-- UPDATE Reservation
-- INNER JOIN User ON Reservation.User_ID = User.User_ID
-- SET Total_Payment = Total_Payment - (Total_Payment * User.Discount / 100)

