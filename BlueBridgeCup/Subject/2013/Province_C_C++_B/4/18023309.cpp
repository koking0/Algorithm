#include <iostream>

using namespace std;

int main(){
    int a = 1, b = 1;
    
    for(int i = 0; i < 19; i++){
        a = a + b;
        b = a + b;
    }

    for(int i = 0; i < 100; i++){
        cout <<  a / b;
        a =  (a % b) * 10;
        if(i == 0) cout << '.';
    }

    cout << endl;

    return 0;
}
