#include<stdio.h>

int main() {
    int step, down, right, n;
    n = 1;
    for (step = 1; step <= 7; step++) {
        if (down != 3 && right != 4) {
            n *= 2;
            down++;
            right++;
        } else if (down >= 3) {
            n += 1;
            right++;
        } else if (right >= 4) {
            n += 1;
            down++;
        }
    }
    printf("%d", n);
    return 0;
}
