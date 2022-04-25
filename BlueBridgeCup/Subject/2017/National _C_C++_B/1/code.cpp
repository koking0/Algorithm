#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int ans = 0;
    string str = "MANY";
    char table[36] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z',};
    for (int i = 0; i < str.length(); i++) {
        for (int j = 0; j < 36; j++) {
            if (str[i] == table[j]) {
                ans += j * int(pow(36, str.length() - i - 1));
            }
        }
    }
    cout << ans << endl;
    return 0;
}