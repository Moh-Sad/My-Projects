# Fikreselam General Hospital Database System

This repository contains the design and implementation of a database management system for **Fikreselam General Hospital**. The system is designed to manage various aspects of hospital operations, including doctors, patients, labs, rooms, billing, and associated companies.

## Table of Contents

- [Overview](#overview)
- [Entities and Relationships](#entities-and-relationships)
- [Database Design](#database-design)
  - [Conceptual ER Diagram](#conceptual-er-diagram)
  - [Logical Design](#logical-design)
- [Features](#features)
- [Getting Started](#getting-started)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

The database system for Fikreselam General Hospital is designed to handle complex interactions between hospital entities, including:
- **Doctors**: Manage doctor profiles and their relationships with patients.
- **Patients**: Store detailed patient information, both inpatients and outpatients.
- **Labs**: Maintain lab details and their interactions with patients.
- **Rooms**: Track room occupancy by inpatients.
- **Billing**: Manage billing details for hospital services.
- **Companies**: Record agreements with insurance companies.

---

## Entities and Relationships

### Key Entities
1. **Doctor**
2. **Patient** (Inpatient and Outpatient)
3. **Lab**
4. **Room**
5. **Bill**
6. **Company**
7. **Employee**

### Relationships
- **Medicates**: Doctors medicate patients.
- **Checks**: Labs check patients.
- **Occupies**: Patients occupy rooms.
- **Issues**: Bills are issued to patients.
- **Provides**: Companies provide agreements for patients.

---

## Database Design

### Conceptual ER Diagram

The conceptual ER diagram models the relationships and attributes of all entities in the database. Below is an overview of the key entities:

#### Entities and Attributes
- **Doctor**
  - Attributes: `Firstname`, `Lastname`, `DoctorID`, `Password`, `Description`, `Status`, `Email`

- **Patient**
  - Attributes: `PatientID`, `Firstname`, `Middlename`, `Lastname`, `Sex`, `Birthdate`, `Nationality`, `PhoneNumber`, `CardNumber`, `TAT`, `Age`, `Address`, `Photo`, `BloodGroup`, `Occupation`

- **Lab**
  - Attributes: `LabID`, `LabNo`, `LabReport`, `Date`, `Category`

- **Room**
  - Attributes: `RoomName`, `RoomNumber`

- **Bill**
  - Attributes: `BillNumber`, `ServiceType`, `BID`, `BillDescription`, `Quantity`, `DiscountPercent`, `BillStatus`, `BillDate`

- **Company**
  - Attributes: `CompanyID`, `AgreementDate`, `ExpiryDate`, `Authorizer`, `AuthorizedDate`, `AgreementDescription`, `InsuranceName`, `CompanyName`, `Address`, `TinNumber`, `CompanyCode`, `Discount`, `PercentValue`, `PriceDescription`

---

### Logical Design

The logical design converts the ER diagram into relational schemas with appropriate data types and constraints:

#### Example Schema: Doctor Table
| Column        | Data Type     | Constraints            |
|---------------|---------------|------------------------|
| `DoctorID`    | INT           | PRIMARY KEY            |
| `Firstname`   | VARCHAR(255)  |                        |
| `Lastname`    | VARCHAR(255)  |                        |
| `Password`    | VARCHAR(255)  |                        |
| `Description` | TEXT          |                        |
| `Status`      | VARCHAR(50)   |                        |
| `Email`       | VARCHAR(255)  | UNIQUE                 |

Other tables and their detailed schemas are included in the design document.

---

## Features

1. **Comprehensive Data Management**: Handles multiple entities and relationships for efficient hospital operations.
2. **Relational Integrity**: Ensures data consistency using primary and foreign keys.
3. **Scalable Design**: Suitable for both small clinics and large hospitals.
4. **User-Friendly**: Intuitive design for easy database interaction.

---

## Getting Started

### Prerequisites
- **Database Management System (DBMS)**: MySQL, PostgreSQL, or similar.
- **Development Tools**: SQL editor, version control (e.g., Git).

### Installation

To set up the **Fikreselam General Hospital Database System**, follow these steps carefully:

#### Step 1: Clone the Repository
Start by downloading the project files from GitHub to your local machine:
```bash
git clone https://github.com/yourusername/fikreselam-hospital-db.git
cd fikreselam-hospital-db
```

#### Step 2: Install a Database Management System (DBMS)
Ensure you have a compatible DBMS installed on your system. This project works with:
- [MySQL](https://dev.mysql.com/downloads/mysql/)
- [PostgreSQL](https://www.postgresql.org/download/)

Download and install your preferred DBMS if it’s not already set up.

#### Step 3: Create a New Database
1. Open your DBMS (e.g., MySQL Workbench, PostgreSQL pgAdmin, or a terminal).
2. Create a new database where the schema will be imported:
   ```sql
   CREATE DATABASE fikreselam_hospital;
   ```

#### Step 4: Import the Schema
Import the provided `database.sql` file into your newly created database to set up the necessary tables and relationships.

**Using MySQL Command-Line**:
```bash
mysql -u your_username -p fikreselam_hospital < database.sql
```

**Using PostgreSQL Command-Line**:
```bash
psql -U your_username -d fikreselam_hospital -f database.sql
```

**Using a GUI Tool**:
- Open your DBMS tool (e.g., MySQL Workbench, pgAdmin).
- Connect to your database and select the `fikreselam_hospital` database.
- Use the import or query tool to execute the `database.sql` file.

#### Step 5: Verify Setup
Check that the tables were created successfully:
- Run `SHOW TABLES;` (MySQL) or `\dt` (PostgreSQL) to list all tables.
- Run a simple query to confirm the data integrity. For example:
  ```sql
  SELECT * FROM doctor;
  ```

#### Step 6: Connect Your Application
Update your application’s database connection settings to use the `fikreselam_hospital` database. Typical settings include:
- **Host**: `localhost`
- **Database Name**: `fikreselam_hospital`
- **Username**: `your_username`
- **Password**: `your_password`
