#include<stdio.h>

int _year(int year)
{
	if(((year%4==0)&&(year%100!=0))||(year%400==0))
	return 1;
	else return 0;
} 

void solve()
{
	int year=1777,day=30,month=4;
	for(int i=1;i<8113;i++)
	{
	
		if(day==30)
		{
			if((month==4)||(month==6)||(month==9)||(month==11))
			{
				day=0;
				month++;
			}
		} 
		if(day==31)
		{
			if((month==1)||(month==3)||(month==5)||(month==7)||(month==8)||(month==10)||(month==12))
			{
				day=0;
				month++;
			}
		}
		if(_year(year))
		{
			if((day==29)&&(month==2))
			{
				day=0;
				month++;
			}
		} 
		else if((day==28)&&(month==2))
	         {
	         	day=0;
	         	month++;
			 }	
		if(month==13)
		{
			year++;
			month=1;
			 
	    }	 
	    day++;
	   
	}
	printf("%d %d %d",year,month,day);
	return;
}








int main()
{
	solve();
	return 0;
 } 
