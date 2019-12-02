//
// Created by alex on 2019/11/11.
//

#include <iostream>

using namespace std;

const int NUM = 39;

int func(int temp, int step) {
    if (temp > NUM) return 0;

    if (temp == NUM) return step % 2 == 0 ? 1 : 0;

    return func(temp + 1, step + 1) + func(temp + 2, step + 1);
}

void solve() {
    cout << func(0, 0) << endl;
}

int main(){
    solve();
    return 0;
}