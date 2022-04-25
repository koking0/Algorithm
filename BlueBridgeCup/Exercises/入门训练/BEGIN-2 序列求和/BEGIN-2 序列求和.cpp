#include <stdio.h>

int main() {
    unsigned long long n, index;
    unsigned long long sum;

    scanf("%d", &n);
    if (n % 2 == 0) {
        sum = (n / 2) * (1 + n);
    } else {
        sum = (n / 2) * (1 + n) + (n / 2) + 1;
    }

    printf("%lld", sum);
    return 0;
}
