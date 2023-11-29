


#include<iostream>
using namespace std;

class node {
private:
    char name[10];
    long prn;
    node* next;

public:
    node() {
        prn = 0;
        next = NULL;
    }

    friend class list;
};

class list {
private:
    node* president;
    node* secretary;
    int count;

public:
    list() {
        president = new node;
        secretary = new node;
        president->next = secretary;
        count = 0;
    }

    void gethead();
    void gettail();
    void addmember();
    void displaylist();
    void remove();
    void display_count();
    void disp_rev();
    friend void display_reverse(list*, node*);
};

void list::gethead() {
    count++;
    cout << "Enter Name of President:" << endl;
    cin >> president->name;
    cout << "Enter PRN of President:" << endl;
    cin >> president->prn;
}

void list::gettail() {
    count++;
    cout << "Enter the name of the secretary:" << endl;
    cin >> secretary->name;
    cout << "Enter PRN of secretary:" << endl;
    cin >> secretary->prn;
    secretary->next = NULL;
}

void list::addmember() {
    count++;
    node* tmp = new node;
    cout << "Enter Member name:\n";
    cin >> tmp->name;
    cout << "Enter PRN of Member:\n";
    cin >> tmp->prn;

    node* current = president;
    node* currentminus1 = NULL;

    while (current->next != NULL && current->prn < tmp->prn) {
        currentminus1 = current;
        current = current->next;
    }

    if (currentminus1 == NULL) {
        tmp->next = president;
        president = tmp;
    }
    else {
        currentminus1->next = tmp;
        tmp->next = current;
    }
}

void list::display_count() {
    cout << "Member count: " << count << endl;
}

void list::displaylist() {
    node* current = president;
    while (current != NULL) {
        cout << "Name of the Member:" << current->name << endl;
        cout << "PRN of the Member:" << current->prn << endl;
        current = current->next;
    }
}

void list::remove() {
    count--;
    long pno = 0;
    cout << "Enter the PRN of the member to be removed:" << endl;
    cin >> pno;

    node* current = president;
    node* currentminus1 = NULL;

    while (current != NULL && current->prn != pno) {
        currentminus1 = current;
        current = current->next;
    }

    if (current != NULL) {
        if (currentminus1 == NULL) {
            president = current->next;
        }
        else {
            currentminus1->next = current->next;
        }
        delete current;
    }
    else {
        cout << "Member Not found!" << endl;
        count++;
    }
}

void list::disp_rev() {
    display_reverse(this, president);
}

void display_reverse(list* a, node* head) {
    // Your implementation here
}

int main() {
    list a;
    a.gethead();
    a.gettail();

    int choice = 0;
    while (true) {
        cout << "Enter Choice:\n1.Add Member\n2.Delete Member\n3.Display No of Members\n4.Display Members\n5.Display in Reverse\n6.Exit\n";
        cin >> choice;

        switch (choice) {
        case 1:
            a.addmember();
            break;
        case 2:
            a.remove();
            break;
        case 3:
            a.display_count();
            break;
        case 4:
            a.displaylist();
            break;
        case 5:
            a.disp_rev();
            break;
        case 6:
            return 0;
        default:
            cout << "Wrong choice\n";
            break;
        }
    }

    return 0;
}
