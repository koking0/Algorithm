#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    char a[100];
    int n, i = 0;
    cin >> n;
    if (n == 0) cout << '0' << endl;
    while (n != 0) {
        switch (n % 16) {
            case 10:
                a[++i] = 'A';
                break;
            case 11:
                a[++i] = 'B';
                break;
            case 12:
                a[++i] = 'C';
                break;
            case 13:
                a[++i] = 'D';
                break;
            case 14:
                a[++i] = 'E';
                break;
            case 15:
                a[++i] = 'F';
                break;
            default:
                a[++i] = n % 16 + '0';
                break;
        }
        n /= 16;
    }
    for (int j = i; j > 0; j--)
        cout << a[j];
    return 0;
}
