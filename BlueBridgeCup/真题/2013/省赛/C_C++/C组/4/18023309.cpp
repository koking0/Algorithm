//
// Created by alex on 2019/11/25.
//

#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int a[] = {2, 3, 4, 5, 6, 7, 8, 10, 12, 14};
bool isEqual(int *a) {
    int sum = 16+a[0]+a[1]+13;
    return (
            sum == a[2]+a[3]+11+a[4]&&
            sum == 9+a[5]+a[6]+a[7]&&
            sum == a[8]+15+a[9]+1&&
            sum == 16+a[2]+9+a[8]&&
            sum == a[0]+a[3]+a[5]+15&&
            sum == a[1]+11+a[6]+a[9]&&
            sum == 13+a[4]+a[7]+1&&
            sum == 16+a[3]+a[6]+1&&
            sum == 13+11+a[5]+a[8]
    );

}
int main() {
    while(next_permutation(a, a+10)) {
        if(isEqual(a)) {
            cout << a[7] << endl;
        }
    }
    return 0;
}