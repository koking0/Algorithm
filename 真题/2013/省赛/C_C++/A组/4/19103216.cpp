#include <stdio.h>

int get_num(int n)
{
	int alter = n;
	int arr[4];
	int k=-1;
	int flag = 1;
	for(int i=0;i<4;i++)
	{
		arr[i] = n%10;
		switch(arr[i])
		{
			case 0:		    break;
			case 1:		    break;
			case 2:arr[i]=5;break;
			case 5:arr[i]=2;break;
			case 6:arr[i]=9;break;
			case 8:			break;
			case 9:arr[i]=6;break;
			default: flag=0;
		}
		n /= 10;
	}
	if(flag)
		k = arr[0]*1000+arr[1]*100+arr[2]*10+arr[3] - alter;
	return k;
}

int main()
{
	int i,j;
	
	for(i=1000;i<10000;i++)
	{
		if(i%10 != 0)
		{
			int sum_1 = get_num(i);
			if(sum_1>-300 && sum_1<-200)
			{
				
				for(j=1000;j<10000;j++)
				{
					if(j%10 != 0)
					{
						int sum_2 = get_num(j);
						if(sum_2>800 && sum_2<900)
						{
							int key = sum_1 + sum_2;
							if(key==558)
							{
								printf("第一个价牌是：%d\n第二个价牌是：%d",i,j);
								return 0;
							}
						}
					}
				}
			}
		}
	}
}
