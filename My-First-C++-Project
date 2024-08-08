#include<iostream>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<iomanip>
#include<fstream>

using namespace std;

struct patient {
    string firstname;
    string lastname;
    int age;
    char blood[5];
    char gender;
    int id;
    int phone_number;
    patient*next;
};

class link {
    patient *head, *last;
    public:
    link() // Constuctor
    {
        head=NULL;
        last=NULL;
    }
    patient input();
    void insertatend();
    void insertatbeg();
    void getpatientout();
    void listofpatients();
    int search(int);
    char departmentname[50];
    };

int link :: search(int item) {
    if(head==NULL)
    return false;
    else {
        int flag = 0;
        patient*p=new patient();
        p = head;
        while( p -> next != NULL && p -> id != item ){
            p = p -> next;
        }
        if( p -> id == item){
            flag = 1;
            return true;
        }
        if(flag == 0)
        return false;
    }
}
int readnumber(){
    char b[20];
    cin.getline(b, sizeof(b));
    return atoi(b);
}

patient link :: input(){
    int flag = 0;
    patient *p = new patient();
    std::cout<< "\n    Please Enter Data for Patient\n";
    std::cout << "\n    First name    : ";
    getline(cin, p -> firstname);
    getline(cin, p -> firstname);
    std::cout << "    Last name     : ";
    getline(cin, p -> lastname);
    again :
    std::cout << "    Blood Group   : ";
    cin >> p -> blood;
    if((strcmp(p -> blood, "A+") == 0) || (strcmp(p -> blood, "a+") == 0) || (strcmp(p -> blood, "A") == 0) || (strcmp(p -> blood, "a") == 0) ||
       (strcmp(p -> blood, "A-") == 0) || (strcmp(p -> blood, "a-") == 0) || (strcmp(p -> blood, "B+") == 0) || (strcmp(p -> blood, "b+") == 0) ||
       (strcmp(p -> blood, "B") == 0) || (strcmp(p -> blood, "b") == 0) || (strcmp(p -> blood, "B-") == 0) || (strcmp(p -> blood, "b-") == 0) ||
       (strcmp(p -> blood, "O+") == 0) || (strcmp(p -> blood, "o+") == 0) || (strcmp(p -> blood, "O") == 0) || (strcmp(p -> blood, "o") == 0) ||
       (strcmp(p -> blood, "O-") == 0) || (strcmp(p -> blood, "o-") == 0) || (strcmp(p -> blood, "AB+") == 0) || (strcmp(p -> blood, "ab+") == 0) ||
       (strcmp(p -> blood, "AB") == 0) || (strcmp(p -> blood, "ab") == 0) || (strcmp(p -> blood, "AB-") == 0) || (strcmp(p -> blood, "ab-") == 0))
            flag = 1;
    if(flag == 0)
    {
    std::cout<<"\n Invalid Blood Group try Again..\n\n";
    goto again;
    }

        std::cout<<"    Gender (m/f)  : ";
        cin>> p->gender;
        std::cout<<"    Age           : ";
        cin>>p->age;
        std::cout<<"    ID            : ";
        cin>>p->id;
        std::cout<<"    Mobile number : ";
        cin>>p->phone_number;

        if(search(p->id)){
        p->id=0;
        std::cout << "\n Data not valid. Operation canceled.";
        }
        return *p;
}
void output(patient *p){
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
std::cout<<"\n Patient data:\n";
std::cout<<"\n First Name     : "<<p->firstname;
std::cout<<"\n Last Name      : "<<p->lastname;
std::cout<<"\n Gender         : "<<p->gender;
std::cout<<"\n Age            : "<<p->age;
std::cout<<"\n Blood group    : "<<p->blood;
std::cout<<"\n Id             : "<<p->id;
std::cout<<"\n Mobile Number  : "<<p->phone_number;
std::cout<<"\n\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
}
void link::insertatbeg(){
patient*p=new patient();
*p=input();
if(p->id==0)
return;
if(head==NULL){
head=p;
last=p;
p->next=NULL;
}
else
p->next=head;
head=p;
std::system("cls");
std::cout << "\n\tPatient added:";
output(p);
}
void link:: insertatend(){
patient*p=new patient();
*p = input();
if(p->id==0)
    return;
if(head==NULL){
    head=p;
    last=p;
    p->next=NULL;
}
else{
    p->next=NULL;
    last->next=p;
    last=p;
}

std::system("cls");
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
std::cout<<"\n |-- ASTU CLINIC MANAGEMENT SYSTEM --|";
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
std::cout<<"\n  ----------PATIENT ADDED---------|";
output(p);
}
void link :: getpatientout(){
std::system("cls");
if(head==NULL){
    std::cout<<"\n  No Patient to operate";
              }
else{
patient*p=new patient();
p=head;
head=head->next;
std::cout << "\n  Patient to operate:";
output(p);
    }
}
void link :: listofpatients(){
if(head==NULL){
std::cout<<"\n No patient";
              }
std::system("cls");
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
std::cout<<"\n |-- ASTU CLINIC MANAGEMENT SYSTEM --|";
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
patient*p=new patient;
p=head;
ofstream write("patient_info.txt", ios::app);
while(p!=NULL)
{
std::cout<<"\n Patient data:\n";
std::cout<<"\n First Name  : "<<p->firstname;
std::cout<<"\n Last Name   : "<<p->lastname;
std::cout<<"\n Gender      :"<<p->gender;
std::cout<<"\n Age         :"<<p->age;
std::cout<<"\n Blood Group :"<<p->blood;
std::cout<<"\n ID          :"<<p->id;
std::cout<<"\n Mobile Number : "<<p->phone_number;
std::cout<<"\n\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
    write<<"\n=======================//====================== \n";
    write<<"\n"<<setw(20)<<" Patient data:\n";
    write<<"\n"<<setw(20)<<" First Name: "<<p->firstname;
    write<<"\n"<<setw(20)<<" Last Name: "<<p->lastname;
    write<<"\n"<<setw(20)<<" Gende : "<<p->gender;
    write<<"\n"<<setw(20)<<" Age: "<<p->age;
    write<<"\n"<<setw(20)<<" Blood Group: "<<p->blood;
    write<<"\n"<<setw(20)<<" Mobile Number: "<<p->id;
p=p->next;
}
write.close();
std::cout<<"\n";
}
void departmentmenu (link* q){
int choice= 0;
patient p;
while (choice != 5){
std::system("cls");
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
std::cout<<"\n |-- ASTU CLINIC MANAGEMENT SYSTEM --|";
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc \n";
std::cout<<"\n"<<q->departmentname;
std::cout<<"\n[1] Add normal patient\n";
std::cout<<"[2] Add critically ill patient \n";
std::cout<<"[3] Take patient to Doctor\n";
std::cout<<"[4] Display list\n";
std::cout<<"[5] Change department or exit\n";
std::cout<<"\n Please enter your choice : ";
cin>>choice;
std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
switch (choice)
    {
    case 1:
    q->insertatend();
    std::cout << "\n Press any key";
    getch();
    break;
    case 2:
    q->insertatbeg();
    std::cout << "\n Press any key";
    getch();
    break;
    case 3:
    q->getpatientout();
    std::cout<<"\n Press any key";
    getch();
    break;
    case 4:
    std::system("cls");
    q->listofpatients();
    std::cout<<"\n Press any key";
    getch();
    break;
    }
}
}

int main ()
{
int i, choice = 0;
link departments[4];
    while(choice!=5)
    {
    strcpy(departments[0].departmentname,"GENERAL CLINIC\n");
    strcpy(departments[1].departmentname,"HEART CLINIC\n");
    strcpy(departments[2].departmentname,"LUNG CLINIC\n");
    strcpy(departments[3].departmentname,"PLASTIC SURGERY\n");
    std::system("cls");
    std::cout<<"\n \xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
    std::cout<<"\n |-- ASTU CLINIC MANAGEMENT SYSTEM --|";
    std::cout<<"\n\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcc";
    std::cout<<"\n |-----------Main Menu---------------|\n\n";
    for (i =0; i < 4; i++)
    {
        std::cout<<" "<<(i+1)<<": "<<departments[i].departmentname;
        }
        std::cout<<" 5: Exit";
        std::cout<<"\n\n Please Enter your Choice :";
        choice=readnumber();
        if(choice>=1 && choice<=4)
        {
            departmentmenu(&departments[choice-1]);
        }

    }
if(choice==5)
std::cout<<"\n\t\tThank you! \n\n\n"
         <<setw(10)<< "Name" << setw(30) << "ID" << setw(25) << "Sec" << endl
         <<setw(10)<< "1.Mohammed Sadik" << setw(30) << "UGR/30960/15" << setw(19) << "34" << endl
         <<setw(10)<< "2.Kulud Mohammed" << setw(30) << "UGR/30809/15" << setw(19) << "34" << endl
         <<setw(10)<< "3.Rahel Eshetu" << setw(32) << "UGR/31116/15" << setw(19) << "34" << endl
         <<setw(10)<< "4.Mekhluqat Abdulwehab" << setw(24) << "UGR/30876/15" << setw(19) << "34" << endl
         <<setw(10)<< "5.Natnael Ati" << setw(33) << "UGR/31043/15" << setw(19) << "34" << endl
         <<setw(10)<< "6.Abdanur Jihad" << setw(31) << "UGR/19578/12" << setw(24) << "34(ADD)" << endl;
exit(0);
    }

