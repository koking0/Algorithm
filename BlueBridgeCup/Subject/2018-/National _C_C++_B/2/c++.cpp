#include <iostream>
#include <cstring>

using namespace std;

int light[31];
long long n=0;

void dfs(int num) {
    if (num == 30) {
        n++;
        return;
    }
    if (light[num - 1] == 0) {
        light[num] = 1;
        dfs(num + 1);
        light[num] = 0;
    }
    dfs(num + 1);
}

int main() {
    dfs(0);
    cout << n << endl;
    return 0;
}