#include <iostream>
using namespace std;

int* createArray(int n) {
    int* arr = new int[n];               // ← Line 5
    for(int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    return arr;                       // ← Line 9  → Danger zone!
}

void printFirstElement() {
    int* ptr = createArray(5);
    cout << "First element = " << ptr[0] << endl;   // ← Line 13
    cout << "Fifth element = " << ptr[4] << endl;
    delete[] ptr;        // ← Memory free kiya
    ptr = nullptr;

}

int main() {
    printFirstElement();
    
    int* leaked = createArray(10);    // ← Line 19
    cout << "Leaked array ka 7th element = " << leaked[7] << endl;

    delete[] leaked;     // ← Leak fix!
    leaked = nullptr;
    
    cout << "Sab khatam bhai!" << endl;
    return 0;
}