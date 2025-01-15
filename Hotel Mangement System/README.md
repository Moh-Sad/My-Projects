# ASTU Five-Star International Hotel Management System

## Overview
This project implements a hotel management system for the **ASTU Five-Star International Hotel**. It allows the management of room reservations, guest information, orders, and services through a user-friendly console-based application. The program is built using C++ and employs a linked list data structure for room management.

---

## Features
1. **Room Management**
   - Add new rooms to the system.
   - Check if a room is occupied.
   - Reserve or release rooms for guests.

2. **Order Management**
   - Order food and drinks for guests.
   - Choose from various services (massage, steam, spa, swimming).

3. **Data Persistence**
   - Save room and guest information to a file.
   - Load data from a file to continue from the last saved state.

4. **Guest Details**
   - View detailed information about guests and their orders.
   - Remove guests from rooms.

5. **Interactive Menu**
   - Console-based menu for seamless navigation through the system.

---

## Functionalities
### 1. Room Reservation
Reserve rooms for guests by providing their names and selecting food, drinks, and additional services. 
- The system calculates the total cost and marks the room as occupied.

### 2. Room Details
View detailed information about any specific room, including:
- Occupancy status.
- Guest name.
- Ordered food, drinks, and services.
- Total price.

### 3. Guest Removal
Remove a guest from a room, resetting the room to its default state.

### 4. About System
Learn about the system and its functionalities.

### 5. Developed By
Displays the names and details of the development team.

---

## File Storage
### **hotel_data.txt**
All room and guest information is saved to this file, ensuring data persistence across sessions.

---

## Usage Instructions

### **Login**
1. Enter the username: `group7@gmail.com`
2. Enter the password: `123456`

### **Main Menu**
Once logged in, the following options are available:
1. **Reserve Room:** Reserve a specific room for a guest.
2. **View Room Detail:** View detailed information about a room.
3. **Remove Guest:** Remove a guest and reset the room.
4. **About System:** Learn about the system features.
5. **Developed By:** View developer details.
6. **Exit:** Save data and exit the application.

### **Reserving a Room**
1. Choose **1** from the main menu.
2. Enter the room number to reserve.
3. Input the guest's name.
4. Select food, drinks, and services.
5. View the total cost and confirm the reservation.

### **Viewing Room Details**
1. Choose **2** from the main menu.
2. Enter the room number to view its details.

### **Removing a Guest**
1. Choose **3** from the main menu.
2. Enter the room number to release.

### **Exiting the System**
1. Choose **6** from the main menu.
2. The data is automatically saved to `hotel_data.txt`.

---

## Food, Drinks, and Services Pricing

### **Food Menu**
| Item                | Price ($) |
|---------------------|-----------|
| 1. Doro Wet         | 99.90     |
| 2. Salad            | 79.90     |
| 3. Pizza            | 69.90     |
| 4. Burger           | 49.90     |
| 5. Lasagna          | 39.90     |
| 6. Kitfo            | 109.90    |
| 7. Salmon           | 45.90     |
| 8. Astu Combo       | 119.90    |
| 9. Sushi            | 59.90     |
| 10. Doro Arusto     | 71.90     |
| 11. Shero           | 64.67     |

### **Drink Menu**
| Item                | Price ($) |
|---------------------|-----------|
| 1. Softdrink        | 99.90     |
| 2. Whiskey          | 79.90     |
| 3. Blacklevel       | 69.90     |
| 4. Wine             | 49.90     |
| 5. Tela             | 39.90     |
| 6. Teje             | 109.90    |
| 7. Water            | 45.90     |

### **Services**
| Service             | Price ($) |
|---------------------|-----------|
| 1. Massage          | 119.90    |
| 2. Steam            | 59.90     |
| 3. Spa              | 71.90     |
| 4. Swimming         | 64.67     |

---

## Developer Team
| Name                 | ID              | Section |
|----------------------|-----------------|---------|
| Mohammed Sadik       | UGR/30960/15   | 5       |
| Mahlet Tiumay        | UGR/30847/15   | 5       |
| Megersa Lamessa      | UGR/30864/15   | 5       |
| Meron Kifle          | UGR/30895/15   | 5       |
| Milion Mengistu      | UGR/30932/15   | 5       |
| Esmael Keder         | UGR/22520/13   | 5       |

---

## Compilation and Execution
1. Compile the code using:
   ```bash
   g++ -o hotel_management hotel_management.cpp
   ```
2. Run the compiled program:
   ```bash
   ./hotel_management
   ```

---

## Notes
- Ensure the file `hotel_data.txt` is in the same directory as the program.
- Use `Ctrl+C` to exit the program during execution if necessary.
- Screen clearing commands (`system("cls")`) may need modification for non-Windows platforms.

---

## License
This project is developed for educational purposes and is not intended for commercial use.
```