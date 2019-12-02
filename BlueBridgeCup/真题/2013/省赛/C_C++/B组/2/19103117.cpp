#include<stdio.h>

int main() {

    int a, b, c, d, e, x, y, m, n, i = 0;

    for (a = 1; a < 10; a++)
        for (b = 1; b < 10; b++)
            for (c = 1; c < 10; c++)
                for (d = 1; d < 10; d++)
                    for (e = 1; e < 10; e++) {
                        m = a * 10 + b;
                        n = c * 100 + d * 10 + e;
                        x = a * 100 + d * 10 + b;
                        y = c * 10 + e;

                        if (m * n == x * y && a != b && a != c && a != d && a != e && b != c && b != d && b != e &&
                            c != d && c != e && d != e)

                            i++;
                    }
    printf("%d", i);
    return 0;
}
