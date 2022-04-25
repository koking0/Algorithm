#include<stdio.h>
int main() {
    int a = 0;
    int b = 0;
    for (a = 1; a < 20; a++) {
        for (b = 1; b < 20; b++) {
            if (b - a > 8)
                break;
            else {
                if (a * b == 6 * (a + b))
                    printf("%d %d\n", a, b);
            }
        }
    }
    return 0;
}
