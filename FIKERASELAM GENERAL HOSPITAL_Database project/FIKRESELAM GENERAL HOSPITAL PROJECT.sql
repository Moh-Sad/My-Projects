-- Fikreselam General Hospital SQL queries --

-- DOCTOR TABLE --
CREATE TABLE Doctor (
    DoctorID INT PRIMARY KEY,
    Firstname VARCHAR(50) NOT NULL,
    Lastname VARCHAR(50) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    Status VARCHAR(20),
    Email VARCHAR(100) UNIQUE NOT NULL
);

-- Create (Insert)
INSERT INTO Doctor (DoctorID, Firstname, Lastname, Password, Description, Status, Email)
VALUES (1, 'Mohammed', 'Sadik', 'hard_to_open', 'Cardiologist', 'Active', 'mohsad.7676@hospital.com');

-- Read (Select)
SELECT * FROM Doctor;

-- Update
UPDATE Doctor
SET Status = 'Inactive'
WHERE DoctorID = 1;

-- Delete
DELETE FROM Doctor
WHERE DoctorID = 1;


-- PATIENT TABLE --
CREATE TABLE Patient (
    PatientID INT PRIMARY KEY,
    Firstname VARCHAR(50) NOT NULL,
    Middlename VARCHAR(50),
    Lastname VARCHAR(50) NOT NULL,
    Sex CHAR(1) NOT NULL CHECK (Sex IN ('M', 'F')),
    Birthdate DATE NOT NULL,
    Nationality VARCHAR(50),
    PhoneNumber VARCHAR(15),
    CardNumber VARCHAR(20) UNIQUE,
    TAT INT,
    Age INT,
    Address VARCHAR(255),
    BloodGroup VARCHAR(3),
    Occupation VARCHAR(50)
);

-- Create (Insert)
INSERT INTO Patient (PatientID, Firstname, Middlename, Lastname, Sex, Birthdate, Nationality, PhoneNumber, CardNumber, TAT, Age, Address, BloodGroup, Occupation)
VALUES (101, 'Gelila', 'Tilahun', 'Aweqe', 'F', '1985-08-20', 'Ethiopian', '0912345678', 'C12345', 5, 19, '04', 'O+', 'Engineer');

-- Read (Select)
SELECT * FROM Patient;

-- Update
UPDATE Patient
SET PhoneNumber = '0912345679'
WHERE PatientID = 101;

-- Delete
DELETE FROM Patient
WHERE PatientID = 101;


-- LAB TABLE --
CREATE TABLE Lab (
    LabID INT PRIMARY KEY,
    LabNo VARCHAR(20) NOT NULL,
    LabReport TEXT,
    Date DATE,
    Category VARCHAR(50)
);

-- Create (Insert)
INSERT INTO Lab (LabID, LabNo, LabReport, Date, Category)
VALUES (1, 'L123', 'Blood Test', '2024-09-01', 'Hematology');

-- Read (Select)
SELECT * FROM Lab;

-- Update
UPDATE Lab
SET LabReport = 'Updated Blood Test Report'
WHERE LabID = 1;

-- Delete
DELETE FROM Lab
WHERE LabID = 1;


-- INPATIENT TABLE --
CREATE TABLE Inpatient (
    PatientID INT NOT NULL,
    RoomNumber INT NOT NULL,
    DateOfAdmission DATE,
    BID INT,
    Advance DECIMAL(10, 2),
    LabNo INT,
    PRIMARY KEY (PatientID, RoomNumber),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (LabNo) REFERENCES Lab(LabID)
);

-- Create (Insert)
INSERT INTO Inpatient (PatientID, RoomNumber, DateOfAdmission, BID, Advance, LabNo)
VALUES (101, 301, '2024-09-10', 1, 500.00, 1);

-- Read (Select)
SELECT * FROM Inpatient;

-- Update
UPDATE Inpatient
SET Advance = 600.00
WHERE PatientID = 101;

-- Delete
DELETE FROM Inpatient
WHERE PatientID = 101;


-- OUTPATIENT TABLE --
CREATE TABLE Outpatient (
    PatientID INT NOT NULL,
    BID INT,
    LabNo INT,
    Date DATE,
    PRIMARY KEY (PatientID),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (LabNo) REFERENCES Lab(LabID)
);

-- Create (Insert)
INSERT INTO Outpatient (PatientID, BID, LabNo, Date)
VALUES (102, 2, 2, '2024-09-11');

-- Read (Select)
SELECT * FROM Outpatient;

-- Update
UPDATE Outpatient
SET LabNo = 3
WHERE PatientID = 102;

-- Delete
DELETE FROM Outpatient
WHERE PatientID = 102;


-- COMPANY TABLE --
CREATE TABLE Company (
    CompanyID INT PRIMARY KEY,
    AgreementDate DATE,
    ExpiryDate DATE,
    Authorizer VARCHAR(100),
    AuthorizedDate DATE,
    AgreementDescription TEXT,
    InsuranceName VARCHAR(100),
    CompanyName VARCHAR(100),
    Address VARCHAR(255),
    TinNumber VARCHAR(20),
    CompanyCode VARCHAR(20),
    Discount DECIMAL(5, 2),
    PercentValue DECIMAL(5, 2),
    PriceDescription TEXT
);

-- Create (Insert)
INSERT INTO Company (CompanyID, AgreementDate, ExpiryDate, Authorizer, AuthorizedDate, AgreementDescription, InsuranceName, CompanyName, Address, TinNumber, CompanyCode, Discount, PercentValue, PriceDescription)
VALUES (1, '2024-01-01', '2025-01-01', 'Ayesha Awel', '2024-01-02', 'Standard Insurance Agreement', 'XYZ Insurance', 'XYZ Corp', 'Adama', 'TIN12345', 'C123', 10.00, 5.00, 'Standard pricing for hospital services');

-- Read (Select)
SELECT * FROM Company;

-- Update
UPDATE Company
SET Discount = 12.00
WHERE CompanyID = 1;

-- Delete
DELETE FROM Company
WHERE CompanyID = 1;


-- BILL TABLE --
CREATE TABLE Bill (
    BillNumber INT PRIMARY KEY,
    ServiceType VARCHAR(100),
    BID INT,
    BillDescription TEXT,
    Quantity INT,
    DiscountPercent DECIMAL(5, 2),
    BillStatus VARCHAR(20),
    BillDate DATE
);

-- Create (Insert)
INSERT INTO Bill (BillNumber, ServiceType, BID, BillDescription, Quantity, DiscountPercent, BillStatus, BillDate)
VALUES (1, 'Consultation', 1, 'General consultation', 1, 5.00, 'Paid', '2024-09-12');

-- Read (Select)
SELECT * FROM Bill;

-- Update
UPDATE Bill
SET BillStatus = 'Pending'
WHERE BillNumber = 1;

-- Delete
DELETE FROM Bill
WHERE BillNumber = 1;


-- ROOM TABLE --
CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    RoomName VARCHAR(50)
);

-- Create (Insert)
INSERT INTO Room (RoomName, RoomNumber)
VALUES ('Surgery', 301);

-- Read (Select)
SELECT * FROM Room;

-- Update
UPDATE Room
SET RoomName = 'Children'
WHERE RoomNumber = 301;

-- Delete
DELETE FROM Room
WHERE RoomNumber = 301;


-- EMPLOYEE TABLE --
CREATE TABLE Employee (
    EmployeeID SERIAL PRIMARY KEY,
    Firstname VARCHAR(50),
    Lastname VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255)
);

-- Create (Insert)
INSERT INTO Employee (Firstname, Lastname, Email, PhoneNumber, Address)
VALUES ('Mikiyas', 'Kasshun', 'Miki5454@hospital.com', '0912345678', 'Addis Ababa');

-- Read (Select)
SELECT * FROM Employee;

-- Update
UPDATE Employee
SET PhoneNumber = '0912345679'
WHERE Email = 'Miki5454@hospital.com';

-- Delete
DELETE FROM Employee
WHERE Email = 'Miki5454@hospital.com';


-- MEDICATES RELATIONSHIP TABLE --
CREATE TABLE Medicates (
    DoctorID INT,
    PatientID INT,
    PRIMARY KEY (DoctorID, PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);

-- ISSUES RELATIONSHIP TABLE (for billing patients) --
CREATE TABLE Issues (
    BillNumber INT,
    PatientID INT,
    PRIMARY KEY (BillNumber, PatientID),
    FOREIGN KEY (BillNumber) REFERENCES Bill(BillNumber),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);




-- Query Optimization for FIKRESELAM GENERAL HOSPITAL Database --

-- 1. INDEXING: Improve Search and Join Performance
-- Adding indexes to frequently used columns in WHERE clauses and JOIN conditions
CREATE INDEX idx_patient_firstname ON Patient(Firstname);
CREATE INDEX idx_patient_lastname ON Patient(Lastname);

CREATE INDEX idx_doctor_firstname ON Doctor(Firstname);
CREATE INDEX idx_doctor_lastname ON Doctor(Lastname);

-- Index for PatientID in Inpatient, Outpatient, Bill, and relationship tables
CREATE INDEX idx_inpatient_patientid ON Inpatient(PatientID);
CREATE INDEX idx_outpatient_patientid ON Outpatient(PatientID);
CREATE INDEX idx_bill_bid ON Bill(BID);

-- Index for DoctorID and PatientID in Medicates table
CREATE INDEX idx_medicates_doctorid ON Medicates(DoctorID);
CREATE INDEX idx_medicates_patientid ON Medicates(PatientID);

-- 2. AVOID SELECT *: Select Only Necessary Columns
-- Reducing unnecessary columns in SELECT queries improves query performance
SELECT Firstname, Lastname, PhoneNumber FROM Patient;

-- 3. JOIN FILTERING: Apply WHERE Clauses Early
-- Reducing the number of rows being joined by filtering data early
SELECT P.Firstname, P.Lastname, D.Firstname, D.Lastname
FROM Patient P
JOIN Medicates M ON P.PatientID = M.PatientID
JOIN Doctor D ON M.DoctorID = D.DoctorID
WHERE P.Sex = 'F';  -- Filtering by Sex before the join

-- 4. QUERY BATCHING: Use UNION Instead of Multiple Queries
-- Combining multiple similar queries using UNION to reduce round-trips to the database
SELECT Firstname, Lastname FROM Patient WHERE BloodGroup = 'O+'
UNION
SELECT Firstname, Lastname FROM Patient WHERE BloodGroup = 'A+';

-- 5. LIMIT ROWS WITH PAGINATION: Fetching Data in Chunks
-- Using LIMIT and OFFSET to handle large datasets in a more efficient manner
SELECT * FROM Patient
LIMIT 10 OFFSET 0;  -- Fetch 10 records starting from the first

-- 6. OPTIMIZING COUNT: Use COUNT(Column) Instead of COUNT(*)
-- Using indexed columns in COUNT queries improves speed
SELECT COUNT(PatientID) FROM Patient;  -- Using PatientID, an indexed column

-- 7. USE EXISTS INSTEAD OF IN: Faster Existence Check
-- EXISTS stops searching once the first match is found, making it faster than IN
SELECT Firstname, Lastname
FROM Patient P
WHERE EXISTS (SELECT 1 FROM Medicates M WHERE M.PatientID = P.PatientID AND M.DoctorID = 1);

-- 8. QUERY CACHING: Use Prepared Statements for Repeated Queries
-- Prepared statements can save execution plans, reducing the overhead for repeated queries
PREPARE get_pending_bills (TEXT) AS
SELECT BillNumber, BillDate FROM Bill WHERE BillStatus = $1;

EXECUTE get_pending_bills('Pending');  -- Executing the cached/prepared query

-- 9. OPTIMIZING GROUP BY WITH INDEXES
-- Indexes on columns used in GROUP BY improve performance
CREATE INDEX idx_doctor_group ON Doctor(DoctorID);  -- Index on DoctorID

SELECT D.Firstname, D.Lastname, COUNT(M.PatientID) AS NumberOfPatients
FROM Doctor D
JOIN Medicates M ON D.DoctorID = M.DoctorID
GROUP BY D.DoctorID;

-- 10. ANALYZING QUERY PLANS: Using EXPLAIN to Understand Execution
-- Analyze the performance of a query to see if it's using indexes and optimized paths
EXPLAIN ANALYZE 
SELECT D.Firstname, D.Lastname, COUNT(M.PatientID) AS NumberOfPatients
FROM Doctor D
JOIN Medicates M ON D.DoctorID = M.DoctorID
GROUP BY D.DoctorID;