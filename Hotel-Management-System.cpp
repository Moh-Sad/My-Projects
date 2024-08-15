#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
//Structure to hold information about room
struct Room{
    double price=0;
    string name_1="";
    string name_2;
    int room_no;
    bool occupied;
    string food;
    string drink;
    bool massage;
    bool steam;
    bool spa;
    bool swimming;
    Room *next;
};
double food_price[11]={99.9,79.9,69.9,49.9,39.9,109.9,45.9,119.9,59.9,71.9,64.67};
double drink_price[7]={99.9,79.9,69.9,49.9,39.9,109.9,45.9};
double service_price[4]={119.9,59.9,71.9,64.67};
double price_storage=0;
//Class for linked list of rooms
class RoomList{
    private:
        Room *head, *tail;
    public:
        RoomList(){
            head = NULL;
            tail = NULL;
        }

        //Function to add a new room to the list
        void addRoom(int no){
            Room *temp = new Room;
             temp->name_1="";

            temp->name_2="";
            temp->room_no = no;
            temp->occupied = false;
            temp->food = "";
            temp->drink = "";
            temp->massage = false;
            temp->steam = false;
            temp->spa = false;
            temp->swimming = false;
            temp->next = NULL;
            if(head == NULL){
                head = temp;
                tail = temp;
            }
            else{
                tail->next = temp;
                tail = temp;
            }
        }

        //Function to check if a room is occupied
        bool isOccupied(int no ){
            Room *temp = head;
            while(temp != NULL){
                if(temp->room_no == no){
                    if(temp->occupied == true){
                        return true;
                    }
                    else{
                        return false;
                    }
                }
                temp = temp->next;
            }
            return true; //if room number not found, assume it's occupied
        }

        //Function to display the food menu
        void displayFoodMenu(){
            cout << "\nFOOD MENU\n";
            cout << "1. DORO WET\n2. SALAD\n3. PIZZA\n4. BURGUR\n5. LAZAGNA\n6. KITFO\n7. SALMON\n8. ASTU COMBO (SPECIAL)\n9. SUSHI\n10. DORO ARUSTO\n11. SHERO\n";
        }

        //Function to display the drink menu
        void displayDrinkMenu(){
            cout << "\nDRINK MENU\n";
            cout << "1. SOFTDRINK\n2. WHISKEY\n3. BLACKLEVEL\n4. WINE\n5. TELA\n6. TEJE\n7. WATER\n";
        }

        //Function to display the list of services
        void displayServices(){
            cout << "\nSERVICES\n";
            cout << "1. MASSAGE\n2. STEAM\n3. SPA\n4. SWIMMING\n";
        }

      // Function to reserve a room and take order from user
int reserveRoom(int no) {
    Room *temp = head;
    while (temp != NULL) {
        if (temp->room_no == no) {
            if (temp->occupied == true) {
                cout << "\nROOM IS ALREADY OCCUPIED BY ANOTHER CUSTUMER.\n";
            } else {
                string first_name, father_name;
                cout << "\n                \nROOM " << temp->room_no << " IS AVALIABLE.\n";
                cout << "\nPLEASE ENTER CUSTEMER'S FIRST NAME: ";
                cin >> first_name;
                cout << "\nPLEASE ENTER CUSTEMER'S FATHER NAME: ";
                cin >> father_name;
                temp->name_1 = first_name;
                temp->name_2 = father_name;

                cout << "\nENTER FOOD ORDER (ENTER 0 FOR NO ORDER):\n";
                displayFoodMenu();
                int food_choice;
                cin >> food_choice;
                if (food_choice > 0 && food_choice <= 11) {
                    temp->food = "FOOD " + to_string(food_choice);
                    temp->price += food_price[food_choice - 1];
                } else {
                    temp->food = "";
                }

                cout << "\nPLEASE ENTER DRINK ORDER (ENTER 0 FOR NO ORDER):\n";
                displayDrinkMenu();
                int drink_choice;
                cin >> drink_choice;
                if (drink_choice > 0 && drink_choice <= 7) {
                    temp->drink = "DRINK " + to_string(drink_choice);
                    temp->price += drink_price[drink_choice - 1];
                } else {
                    temp->drink = "";
                }

                cout << "\nPLEASE ENTER THE SERVICE YOU WANT (ENTER 0 FOR NONE):\n";
                displayServices();
                int service_choice;
                cin >> service_choice;
                switch (service_choice) {
                    case 1:
                        temp->massage = true;
                        temp->price += service_price[0];
                        break;
                    case 2:
                        temp->steam = true;
                        temp->price += service_price[1];
                        break;
                    case 3:
                        temp->spa = true;
                        temp->price += service_price[2];
                        break;
                    case 4:
                        temp->swimming = true;
                        temp->price += service_price[3];
                        break;
                    default:
                        temp->massage = false;
                        temp->steam = false;
                        temp->spa = false;
                        temp->swimming = false;
                        break;
                }
                temp->occupied = true;
                cout << "\nROOM " << temp->room_no << " HAS BEEN RESERVED.\n\n";
                cout << "THANKS FOR USING THIS SERVICE!!!\n\n";
                cout << "Total price is $" << temp->price << endl;
            }
            return 0;
        }
        temp = temp->next;
    }
    cout << "ROMM NUMBER NOT FOUND.\n";
    return 0;
}
// Function to remove a guest from a room

void removeGuest(int no){
    Room *temp = head;
    while(temp != NULL){
        if(temp->room_no == no){
            if(temp->occupied == true){
                temp->occupied = false;
                temp->name_1 = "";
                temp->name_2 = "";
                temp->food = "";
                temp->drink = "";
                temp->massage = false;
                temp->steam = false;
                temp->spa = false;
                temp->swimming = false;
                cout << "\nGUST HAS BEEN REMOVED FROM ROOM NUMER " << temp->room_no << ".\n";
                return;
            }
            else{
                cout << "\nROOM IS NOT OCCUPIED BY .\n";
                return;
            }
        }
        temp = temp->next;
    }
    cout << "ROOM IS NOT FOUND.\n";
}


    //Function to display the details of a room
    void displayRoom(int no){
        Room *temp = head;
        while(temp != NULL){
            if(temp->room_no == no){
                cout << "########################################################### \n";
                cout << "#  ROOM " << temp->room_no << " DETAILS:\n";
                cout << "#  IS ROOM OCCUPIED :      #  " << (temp->occupied ? "YES OCCUPIED" : "NO ") << endl;
                cout << "#  CUSTUMER FULL NAME      #  "<<temp->name_1<<" "<<temp->name_2<<endl;
                cout << "#  FOOD OREDERED:          #  " << temp->food << endl;
                cout << "#  DRINK OREDERED:         #  " << temp->drink << endl;
                cout << "#  SERVICES OREDERED:      #  ";
                if(temp->massage){
                    cout << "  MASSAGE \n";
                }
                if(temp->steam){
                    cout << "  STEAM \n";
                }
                if(temp->spa){
                    cout << "  SPA \n";
                }
                if(temp->swimming){
                    cout << "  SWIMMING \n";
                }
                cout << "\n#  THE TOTAL PRICE IS      #  $ "<<temp->price<<endl;
                cout << "\n########################################################### \n";
                cout << endl;
                return;
            }
            temp = temp->next;
        }
        cout << "ROOM IS NOT FOUND .\n";
    }
    void saveToFile(const string& filename) {
    ofstream file(filename);
    if (!file) {
        cout << "Error opening file.\n";
        return;
    }

    Room* temp = head;
    while (temp != NULL) {
        file << temp->room_no << endl;
        file << temp->occupied << endl;
        file << temp->name_1 << endl;
        file << temp->name_2 << endl;
        file << temp->food << endl;
        file << temp->drink << endl;
        file << temp->massage << endl;
        file << temp->steam << endl;
        file << temp->spa << endl;
        file << temp->swimming << endl;

        temp = temp->next;
    }

    file.close();
    cout << "Room information saved to file: " << filename << endl;
}

// Function to load room information from a file
void loadFromFile(const string& filename) {
    ifstream file(filename);
    if (!file) {
        cout << "Error opening file.\n";
        return;
    }

    // Clear existing room data
    while (head != NULL) {
        Room* temp = head;
        head = head->next;
        delete temp;
    }

    int room_no;
    bool occupied;
    string name_1, name_2, food, drink;
    bool massage, steam, spa, swimming;

    while (file >> room_no) {
        file >> occupied;
        file.ignore();
        getline(file, name_1);
        getline(file, name_2);
        getline(file, food);
        getline(file, drink);
        file >> massage;
        file >> steam;
        file >> spa;
        file >> swimming;

        Room* temp = new Room;
        temp->room_no = room_no;
        temp->occupied = occupied;
        temp->name_1 = name_1;
        temp->name_2 = name_2;
        temp->food = food;
        temp->drink = drink;
        temp->massage = massage;
        temp->steam = steam;
        temp->spa = spa;
        temp->swimming = swimming;
        temp->next = NULL;
        if (head == NULL) {
            head = temp;
        }
        else {
            Room* current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = temp;
        }
    }

    file.close();
    cout << "Room information loaded from file: " << filename << endl;
}
};


int main() {
    login:
    string username = "group7@gmail.com";
    string password = "123456";
    string input_username, input_password;

    cout << "\n                       LOG IN PAGE ";
    cout << "\n\n\n       | ENTER USERNAME     ";
    cin >> input_username;
    cout << "\n\n      |  ENTER PASSWORD     ";
    cin >> input_password;

    if (input_username == username && input_password == password) {
        system("cls");
    } else {
        system("cls");
        cout << "\n            INVALID USERNAME OR PASSWORD\n\n";
        cout << "            PLEASE TRY AGAIN !!!\n\n";
        goto login;
    }



string filename = "hotel_data.txt";
RoomList rooms;
//Add 400 rooms to the list
for(int i = 1; i <= 400; i++){
rooms.addRoom(i);
}
//Display menu and get user input
rooms.loadFromFile(filename);
int choice, room_no;

    do{
    cout << "            [--------------------------------------------------]\n";
    cout << "            [--------------------------------------------------]\n";
    cout << "       |  ASTU FIVE STAR INTERNATIONMAL HOTEL MANAGEMENT SYSTEM MENU     | \n";
    cout << "            [--------------------------------------------------]\n";
    cout << "            [--------------------------------------------------]\n";
    cout << "               |       1. RESERVE ROOM                     |          \n";
    cout << "               |       2. VIEW ROOM DETAIL                 |          \n";
    cout << "               |       3. REMOVE GUST                      |          \n";
    cout << "               |       4. ABOUT SYSTEM                     |          \n";
    cout << "               |       5. DEVELOPED BY                     |          \n";
    cout << "               |       6. Exit                             |          \n";
    cout << "               |  PLEASE ENTER YOUR CHOICE: ";
    char ch;
    cin >> choice;
    system("cls");
    cout<<endl;

switch(choice){
        case 1:
            cout << "ENTER THE ROOM NUMBER THAT YOU WANT : ";
            cin>>room_no;
            rooms.reserveRoom(room_no);
            cout << "DO YOU WANT TO CLEAR THE SCREEN [y/n]: ";
            cin >> ch;
            if (ch == 'y' || ch == 'Y')
                system("cls");
            break;
        case 2:
            cout << "ENTER THE ROOM NUMBER THAT YOU WANT TO KNOW : ";
            cin >> room_no;
            rooms.displayRoom(room_no);
            cout << "DO YOU WANT TO CLEAR THE SCREEN ? [Y/N]: ";
            cin >> ch;
            if (ch == 'y' || ch == 'Y')
                system("cls");
            break;
        case 3:
            //cout << "ENTER THE ROOM NUMBER THAT YOU WANT  : ";
            cin >> room_no;
            rooms.removeGuest(room_no);
            cout << " DO YOU WANT TO CLEAR THE SCREEN ? [Y/N]: ";
            cin >> ch;
            if (ch == 'y' || ch == 'Y')
                system("cls");
            break;
        case 4:
            cout<<"         THIS PLATFORM IS A HOTEL MANEGEMENT SYSTEMS . THE SYSTEM HAS A LOT OF FUNCTIONALITIES SUCH AS \n\n";
            cout<<"                 # RESERVE ROOM FOR GUSTS.\n";
            cout<<"                 # OREDER FOOD, DRINK AND DIFFERENT SERVICES TO GUSTES\n";
            cout<<"                 # VIEW A DETAILS ABOUT THE GUSTES\n";
            cout<<"                 # ROMOVE GUSTES FROM THE HOTEL\n\n";
            cout << "DO YOU WANT TO CLEAR THE SCREEN ? [Y/N]: ";
            cin >> ch;
            if (ch == 'y' || ch == 'Y')
                system("cls");
            break;
        case 5:
            cout<<" THIS PLATFORM IS DEVELOPED BY  :\n\n";
            cout<<"             NAME                       ID            SECTION\n\n";
            cout<<"          1. Mohammed Sadik        UGR/30960/15          5\n";
            cout<<"          2. Mahlet Tiumay         UGR/30847/15          5\n";
            cout<<"          3. Megersa Lamessa       UGR/30864/15          5\n";
            cout<<"          4. Meron Kifle           UGR/30895/15          5\n";
            cout<<"          5. Milion Mengistu       UGR/30932/15          5\n";
            cout<<"          6. Esmael Keder          UGR/22520/13          5\n";

            cout << "DO YOU WANT TO CLEAR THE SCREEN ? [Y/N]: ";
            cin >> ch;
            if (ch == 'y' || ch == 'Y')
                system("cls");
            break;
        case 6:
            cout << "  EXITING....\n";
            rooms.saveToFile(filename);
            cout<<"FILE IS SAVED SUCCESFULLY\n\n";
            cout << "THANKS FOR YOUR TIME!!\n";
            break;
        default:
            cout << "INVALID CHOICE.\n";
            break;
    }
} while(choice != 6);

return 0;
}
