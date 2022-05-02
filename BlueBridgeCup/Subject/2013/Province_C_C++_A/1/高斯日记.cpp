                 



#include<stdio.h> 
int runorburun(int nian)
{
	if((nian%4==0&&nian%100!=0)||(nian%400==0))return 1;
	else
	return 0;
} 
int nian= 1777,yue=0,ri= 8113+31+28+31+30,
y1[12] = {31,28,31,30,31,30,31,31,30,31,30,31},
y2[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
int main()
{ 
	while(ri>365)
	{
		if(runorburun(nian))
		{
			ri-=366;
			nian++;
		}
		else
		{
			ri-=365;
			nian++;
		}
	}
 
	if(runorburun(nian))
	{
		yue=0;
		while(ri>y2[yue]){
			ri-=y2[yue];
			yue++;
		}
	}
	else
	{
		yue=0;
		while(ri>y1[yue])
		{
			ri-=y1[yue];
			yue++;
		}	
	}
	printf("%d %d %d\n",nian,yue+1,ri-1);
	return 0;
}
