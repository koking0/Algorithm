#include <stdio.h>
#define X 5
#define Y 4
int main() 
{
    int a[X][Y];
    int i, j;
    for (j = 0; j < Y; j++) 
	      {
           a[0][j] = 1;
        }
    for (i = 1; i < X; i++) 
	      {
           a[i][0] = 1;
        }
    for (i = 1; i < X; i++) 
	      {
           for (j = 1; j < Y; j++)
		           {
                   a[i][j] = a[i-1][j] + a[i][j-1];
               }
        }
    printf("%d", a[X-1][Y-1]);
    return 0;
}
