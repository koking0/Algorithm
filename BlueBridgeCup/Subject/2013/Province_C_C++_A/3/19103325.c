#include<stdio.h>
#define N 4
#define M 5
int main() {
    int a[N][M];
    int i, j;
    for (j = 0; j < M; j++) {
        a[0][j] = 1;
    }
    for (i = 1; i < N; i++) {
        a[i][0] = 1;
        for (j = 1; j < M; j++) {
            a[i][j] = a[i - 1][j] + a[i][j - 1];
        }
    }
    printf("%d\n", a[N - 1][M - 1]);
    return 0;
}