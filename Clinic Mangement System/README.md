# ASTU Clinic Management System

## Overview
The ASTU Clinic Management System is a console-based application developed in C++ to manage patient records and operations for various departments in a clinic. The system supports adding new patients, viewing patient lists, managing patient queues, and switching between departments.

---

## Features

1. **Patient Management**
   - Add new patients to the system with their details.
   - Maintain separate queues for normal and critically ill patients.

2. **Departmental Management**
   - Manage patients for different departments:
     - General Clinic
     - Heart Clinic
     - Lung Clinic
     - Plastic Surgery

3. **Queue Management**
   - Add patients at the beginning or end of the queue.
   - Move patients to a doctor (remove from the queue).

4. **Data Output**
   - Display detailed patient records.
   - Save patient data to a file (`patient_info.txt`) for future reference.

5. **Interactive Menu**
   - User-friendly menu for navigating various operations.

---

## Functionalities

### 1. Add a Patient
Add a new patient with the following details:
- First Name
- Last Name
- Age
- Blood Group
- Gender
- Unique ID
- Phone Number

The system validates the blood group and ensures unique IDs for patients.

### 2. Manage Queues
- Add critically ill patients to the beginning of the queue.
- Add normal patients to the end of the queue.
- Move the first patient in the queue to the doctor.

### 3. Department Selection
Switch between four departments:
- General Clinic
- Heart Clinic
- Lung Clinic
- Plastic Surgery

Each department maintains its own patient queue.

### 4. View and Save Patient Records
- View the list of patients in the current department.
- Save all patient records to `patient_info.txt`.

---

## File Storage
### **patient_info.txt**
- Patient records are saved in this file in an organized format.
- Each patient's details include:
  - Name
  - Gender
  - Age
  - Blood Group
  - ID
  - Phone Number

---

## Usage Instructions

### **Main Menu**
1. **Select Department**
   Choose a department to manage (General, Heart, Lung, or Plastic Surgery).
2. **Manage Patients**
   Perform operations such as adding patients, viewing the queue, or sending patients to the doctor.
3. **Exit**
   Exit the application after saving records.

### **Department Menu**
- **[1] Add Normal Patient**  
  Add a patient to the end of the queue.
- **[2] Add Critically Ill Patient**  
  Add a patient to the beginning of the queue.
- **[3] Take Patient to Doctor**  
  Remove the first patient from the queue and display their details.
- **[4] Display List**  
  View all patients in the queue.
- **[5] Change Department or Exit**  
  Return to the main menu or exit the system.

---

## Example Patient Details
### Input Example
```
First name    : John  
Last name     : Doe  
Blood Group   : A+  
Gender (m/f)  : m  
Age           : 30  
ID            : 101  
Mobile number : 1234567890  
```

### Output Example
```
Patient Data:
First Name     : John  
Last Name      : Doe  
Gender         : m  
Age            : 30  
Blood Group    : A+  
ID             : 101  
Mobile Number  : 1234567890  
```

---

## Developer Team
| Name                       | ID           | Section |
|----------------------------|--------------|---------|
| Mohammed Sadik             | UGR/30960/15 | 34      |
| Kulud Mohammed             | UGR/30809/15 | 34      |
| Rahel Eshetu               | UGR/31116/15 | 34      |
| Mekhluqat Abdulwehab       | UGR/30876/15 | 34      |
| Natnael Ati                | UGR/31043/15 | 34      |
| Abdanur Jihad              | UGR/19578/12 | 34(ADD) |

---

## Compilation and Execution

### Compile
Use the following command to compile the program:
```bash
g++ -o clinic_management clinic_management.cpp
```

### Execute
Run the compiled program:
```bash
./clinic_management
```

---

## Notes
- The application uses `system("cls")` for screen clearing, which is platform-specific. Modify it for non-Windows systems.
- The program employs linked lists to manage patient queues for each department.
- All input and output operations are performed via the console.

---

## License
This project is developed for educational purposes and is not intended for commercial use.
```