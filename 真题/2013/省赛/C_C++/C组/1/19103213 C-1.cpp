#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

int num[10];

int judge(int age)
{
	int s=1;
	int lifang = pow(age,3);
	int sicifang = pow(age,4);
	if(lifang/1000 == 0||sicifang/10000 == 0)
		s=0;
	else
	{
		while(lifang)
		{	
			num[lifang%10]++;
			lifang /= 10;
		}
		while(sicifang)
		{
			num[sicifang%10]++;
			sicifang /= 10;
		}
		for(int i=0;i<10;i++)
		{
			if(num[i] != 1 )
				s=0;
		}
	}
	return s;
}

int main()
{
	for(int i=10;i<100;i++)
	{
		for(int j=0;j<10;j++)
			num[j] = 0;
		if(judge(i)==1)
			cout<<i<<endl;
	}
	return 0;
}
