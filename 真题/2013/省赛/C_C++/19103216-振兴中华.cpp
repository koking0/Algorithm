#include<stdio.h>
int count=0;
void road(int row,int line,int arr[][5])
{
	if(arr[row][line]==7)//从0开始跳到7则为一条完整路线 
		count++;
	
	if(line+1<5 && arr[row][line+1]==arr[row][line]+1)//横向走 
		road(row,line+1,arr);
		
	if(row+1<4 && arr[row+1][line]==arr[row][line]+1)//纵向走 
		road(row+1,line,arr);
}
int main()
{
	int arr[4][5]={
	            {0,1,2,3,4},
	            {1,2,3,4,5},
			    {2,3,4,5,6},
			    {3,4,5,6,7}};
	road(0,0,arr);
	printf("%d",count);
	return 0;			   
}
