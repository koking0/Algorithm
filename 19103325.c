#include<stdio.h>

int main () {
    int i;
    int f[10];
    f[0] = 2;
    f[1] = 3;
    for(i = 1; i <= 10; i++) {
        f[i] = 2 * f[i - 1] - 1;
    }
    printf ("%d", f[10]);

    return 0;
}
