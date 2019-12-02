//
// Created by alex on 2019/11/11.
//

#include <iostream>
#include <sstream>

using namespace std;

void i2s(int num, string &str){
    stringstream ss;
    ss << num;
    ss >> str;
}

bool check(string basicString) {
    int num[10] = {0};
    for (int i = 0; i < basicString.length(); ++i)
        num[basicString[i] - 48]++;
    for (int i = 0; i < 10; ++i)
        if (num[i] > 1) return false;
    return true;
}

void solve() {
    //我年龄的立方是个4位数。我年龄的4次方是个6位数。这10个数字正好包含了从0到9这10个数字，每个都恰好出现1次。
    for (int i = 0; i < 100; ++i) {
        int pow3 = i * i * i, pow4 = i * i * i * i;

        if (pow3 > 999 && pow3 < 10000 && pow4 > 99999 && pow4 < 1000000){
            string str3, str4;
            i2s(pow3, str3);
            i2s(pow4, str4);
            if (check(str3 + str4)) cout << i << " " << pow3 << " " << pow4 << endl;
        }
    }
}

int main(){
    solve();
    return 0;
}