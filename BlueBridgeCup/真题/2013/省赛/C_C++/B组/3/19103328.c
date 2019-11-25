#include <stdio.h>
int count=0;
void sum(int stair,int step)
{
	if(stair==0&&step%2==0)
		count++;
	if(stair<0)
		return;
	sum(stair-1,step+1);
	sum(stair-2,step+1);
	
}
int main()
{
	sum(39,0);
	printf("count=%d\n",count);
	
	return 0;
}
