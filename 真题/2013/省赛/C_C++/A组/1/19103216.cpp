/*高斯出生于：1777年4月30日。
在高斯发现的一个重要定理的日记上标注着：5343，
因此可算出那天是：1791年12月15日。
高斯获得博士学位的那天日记上标着：8113   
请你算出高斯获得博士学位的年月日。*/

#include <stdio.h>

int main()
{
	int year,year_plus,month=0,day;
//4月30日为当年第120天 
	int date=8113+120-1;
	
	year_plus = date/365;
	year = 1777 + year_plus;
	for(int i=1777;i<year;i++)
	{
		if(i%400==0 || (i%100!=0&&i%4==0))
		{
			date--;
		}
	}
	int sum = date - 365*year_plus;
	
	int sum_day=0;
	int arr[12]={0,31,28,31,30,31,30,31,31,30,31,30};
	for(int i=0;i<12;i++)
	{		
		sum_day += arr[i];
		month++;
		if(sum_day+arr[i+1]>=sum)
			break;
	}
	if( (year%400==0 || (year%100!=0&&year%4==0))&&month>2 )
		sum_day++;
		
	day = sum - sum_day;
	
	if(day==0)
		day=31;
		
	if(month>9&&day>9)
		printf("%d-%d-%d",year,month,day);
	if(month>9&&day<10)
		printf("%d-%d-0%d",year,month,day);	
	if(month<10&&day>10)
		printf("%d-0%d-%d",year,month,day);
	if(month<10&&day<10)
		printf("%d-0%d-0%d",year,month,day);
	return 0;
}
