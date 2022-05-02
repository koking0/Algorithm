#include<cstdio>

int run(int year)
{
	return ((year % 4 == 0 && year % 100 != 0 )|| year % 400 == 0) ? 1 : 0;
}

void solve()
{
	int year = 1777, month = 4, day = 30;
	int last = 8113;
	for (int i = 1; i < last; i++)
	{
		day++;
		if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10) && day == 32)
		{
			day = 1;
			month++;
		}
		if (month == 12 && day == 32)
		{
			day = 1;
			month = 1;
			year++;
		}
		if ((month == 4 || month == 6 || month == 9 || month == 11) && day == 31)
		{
			day = 1;
			month++;
		}
		if (month == 2)
		{
			if (run(year) == 1 && day == 30)
			{
				day = 1;
				month++;
			}
			else if (run(year) == 0 && day == 29)
			{
				day = 1;
				month++;
			}
		}
	}
	printf("%dÄê%02dÔÂ%02dÈÕ", year, month, day);
}

int main()
{
	solve();
}