#include <stdio.h>

int turn(int n)
{
	int x,z,flag;
	int i,j;
	int arr[4];
	x=n;
	flag=1;
	z=-1;
	for(i=0;i<4;i++)
	{
		arr[i]=x%10;
		x/=10;
	
	switch(arr[i])
	  {
		case 1: break;
		case 2: arr[i]=5; break;
		case 5: arr[i]=2; break;
		case 6: arr[i]=9; break;
		case 8: break;
		case 9: arr[i]=6; break;
		case 0: break;
		default: flag=0;  break;
	  }   
	}
	if(flag)
	z=arr[3]+arr[2]*10+arr[1]*100+arr[0]*1000-n;
	return z;
}
int main()
{
	int a1,a2;
	
	for(int i=1000;i<10000;i++)
	{
		if(i%10!=0)
		{
		
		a1=turn(i);
		
		if(a1<-200&&a1>-300)
		{
			for(int j=1000;j<10000;j++)
			{
				a2=turn(j);
				if(a2>800&&a2<900)
				{
					if((a1+a2)==558)
					{
						printf("%d",i);
						return 0;
					}
				}
			}
			
		}
	  }
	}
	return 0;
}









