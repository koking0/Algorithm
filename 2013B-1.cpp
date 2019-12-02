#include<stdio.h>

int main()

{

       int a[4][5]={{2,2,2,2,1},{2,2,2,2,1},{2,2,2,2,1},{1,1,1,1,1}},i,j,sum=1;

       for(i=0;i<4;i++)

       for(j=0;j<5;j++)

      

       sum*=a[i][j];

       printf("%d",sum);

}
