#include <stdio.h>

int main()
{
	int cnt_1,cnt_2;
	//cnt_1表示跨1个台阶的次数，cnt_2表示跨两个台阶的次数 ，cnt_2为奇数次 
	
	int sum = 0;
	for(cnt_2=1;cnt_2<=19;cnt_2+=2)
	{
		int k=1;
		cnt_1 = 39 - cnt_2;
		for(int i=1 ; i<=cnt_2 ; i++)
		{
			k = k * cnt_1-- / i;	
		}
		printf("%d\n",k);
		sum += k;
	}
	printf("%d",sum);
	
	return 0;
}
