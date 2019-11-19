#include<iostream>
using namespace std;

struct prize
{
	int num, newnum, cha;
};
prize goods[9000];

int fanzhuan(int x)
{
	if (x % 10 == 0)
		return 0;
	int a[4];
	for (int i = 0; i < 4; i++)
	{
		a[i] = x % 10;
		if (a[i] == 3 || a[i] == 4 || a[i] == 7)
			return 0;
		if (a[i] == 6)
			a[i] = 9;
		else if (a[i] == 9)
			a[i] = 6;
		x = x / 10;
	}
	return a[0] * 1000 + a[1] * 100 + a[2] * 10 + a[3];
}

void solve()
{
	int m = 0;
	for (int i = 1000; i < 10000; i++)
	{
		if (fanzhuan(i) == 0)
			continue;
		if (fanzhuan(i) - i <= -300 || (fanzhuan(i) - i >= -200) && (fanzhuan(i) - i <= 800) || fanzhuan(i) - i >= 900)
			continue;
		goods[m].num = i;
		goods[m].newnum = fanzhuan(i);
		goods[m].cha = fanzhuan(i) - i;
		m++;
	}
	for (int i = 0; i < 9000; i++)
	{
		if (goods[i].cha > 800)
			continue;
		for (int j = 0; j < 9000; j++)
		{
			if (goods[j].cha < -200)
				continue;
			if (goods[i].cha + goods[j].cha == 558)
				cout << "赔200多的原价为" << goods[i].num << "，赚八百多的原价为"<<goods[j].num<<endl;
		}
	}
}

int main()
{
	solve();
	return 0;
}
