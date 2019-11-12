#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int a[6],b[13];

int chongfu1(int m)
{
	int s = 0;
	for (int i = 0; i < 6; i++)
	{
		a[i] = m % 10;
		m = m / 10;
	}
	for (int i = 0; i < 5; i++)
	{
		for (int j = i + 1; j < 6; j++)
		{
			if (a[i] == a[j])
			{
				s = 1;
				break;
			}
		}
		if (s == 1)
			break;
	}
	return s;
}

int chongfu2(long long t)
{
	int s = 0;
	for (int i = 0; i < 13; i++)
	{
		if (t != 0)
		{
			b[i] = t % 10;
			t = t / 10;
		}
		else
			break;
	}
	for (int i = 0; i < 6; i++)
	{
		for (int j = 0; j < 13; j++)
		{
			if (a[i] == b[j])
			{
				s = 1;
				break;
			}
		}
		if (s == 1)
			break;
	}
	return s;
}

void solve()
{
	for (int i = 0; i < 13; i++)
	{
		b[i] = 10;
	}
	for (int i = 100000; i < 1000000; i++)
	{
		if (chongfu1(i) == 1)
			continue;
		long long t = pow(i,2);
		if (chongfu2(t) == 1)
			continue;
		cout << i << endl;
	}
}

int main()
{
	solve();
}