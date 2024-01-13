-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check our crime scene reports for any clues. Found the first clue but didn't find enough to help narrow down suspect.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year=2023 AND street = 'Humphrey Street';

-- Looked through the interview transcripts as well to find the new clues from that day after the incident happened.
SELECT transcript FROM interviews WHERE month = 7 AND day = 28 AND year=2023;

-- Check second clue about ATM logs
SELECT * from atm_transactions WHERE month=7 AND day=28 AND year=2023 AND atm_location="Leggett Street";

-- Check first clue about bakery security cameras
SELECT * FROM bakery_security_logs WHERE day=28 AND month=7  AND year=2023 AND hour=10 AND minute > 15 AND minute < 25;


-- Possible suspects according to the bakery logs.
SELECT * FROM people WHERE license_plate="322W7JE";

SELECT * FROM people where license_plate="5P2BI95";

SELECT * FROM people where license_plate="94KL13X";

SELECT * FROM people where license_plate="6P58WS2";


SELECT * from people WHERE license_plate="0NTHK55";


SELECT * FROM people where license_plate="4328GD8";


SELECT * FROM people where license_plate="G412CB7";


SELECT * from people WHERE license_plate="L93JTIZ";


-- Second clue about atm_transaction that happened just before theft occurred.
SELECT * FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" and transaction_type = "withdraw";


-- Went back to get name of individual who made report
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND year=2023;

-- Realized atm log doesn't include a time to help wittle down possible suspects. Proceeding to phone call logs.


-- After some thought, and going through each clue individually, found it was too hard to pick through data so tried some nested queries with all the clues to see if I could get the killer's name.
SELECT name FROM people WHERE people.license_plate IN ( SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 and HOUR = 10 AND minute > 15 AND minute < 25) And people.id IN ( SELECT person_id FROM bank_accounts JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE atm_transactions.year = 2020 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND transaction_type = "withdraw" AND atm_transactions.act_location = "Leggett Street") And people.phone_number IN ( SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60) AND people.passport_number IN ( SELECT passport_number FROM passengers WHERE flight_id IN ( SELECT id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 ORDER BY hour, minute ASC LIMIT1 ));

-- Turns out killer's name is Bruce!
-- Looked up his license plate number and found he was at the bakery the morning of the incident and called robin to let her know make the purchase for the flight. The call lasted 48 seconds.


-- After finding killer's name, tried to search for accomplice using telephone number to no avail.
SELECT * FROM phone_calls WHERE caller="(367) 555-5533" AND month = 7 AND day = 27 AND year = 2023 AND duration < 60;

-- Afterwards thought back to previous problem and figured I would try to combine all the clues we know about the incident all the call and also included Bruce's name as the caller.
SELECT name FROM people WHERE phone_number IN ( SELECT receiver FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND caller = ( SELECT phone_number FROM people WHERE name = "Bruce") AND duration < 60);



-- Finally after obtaining the name of the accomplice ROBIN. Used the flight clue to grab the first flight in the morning and get the destination ID.
SELECT * FROM flights WHERE year = 2023 AND month = 7 AND day = 29 ORDER BY hour, minute ASC LIMIT 1;


-- Now that we have the destination airport ID, we can query the airports table using the id and see where he went.
SELECT city FROM airports WHERE id = 4;

