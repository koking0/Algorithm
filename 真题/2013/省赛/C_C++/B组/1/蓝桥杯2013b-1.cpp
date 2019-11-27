#include<stdio.h>
#include<stdlib.h>

int zyear[12] = { 31,0,31,30,31,30,31,31,30,31,30,31 };

//闰年返回为真
bool RorP(int year)
{
	if (year % 100 == 0)
	{
		if (year % 400 == 0)
			return true;
		else return false;
	}
	else if (year % 4 == 0)
		return true;
	else return false;
}

int main()
{
	int year, month, day, sumday = 1;
	year = 1791, month = 12, day = 15;
	do
	{
		day++;
		if (RorP(year)) zyear[1] = 29;
		else zyear[1] = 28;
				if (day > zyear[month-1])
				{
					month++;
					day = 1;
				}
				if (month > 12)
				{
					month = 1;
					year++;
				}
			sumday++;
	} while (sumday <=2770);
	printf("%d-%d-%d", year, month, day);
	return 0;
}