#include<iostream>
using namespace std;

int a[6]={0,0,0,8,8,8};
int b[6]={1,1,4,5,6,7};
int c[6]={0};
int temp[6]={0};
int MAX=0;

void count()
{
   int m=0,x1=0,x2=0;
   for(int i=0;i<6;i++){
     x1=x2=0;
   	 for(int j=0;j<6;j++){
   	 	if(c[i]>a[j])
   	 		x1++;
   	 	else
   	 		break;
   	 }

   	 for(int j=0;j<6;j++){
   	 	if(c[i]>b[j])
   	 		x2++;
   	 	else
   	 		break;
   	 }

   	 m+=x1*x2;
   }
   if(m>MAX){
   	for(int i=0;i<6;i++){
   		temp[i]=c[i];
   	}
   	MAX=m;
   }
}

void dfs(int n,int cur,int sum)
{
	if(sum>24) return;
	if(n==6)
	{
		if(sum==24){//计算概率
			count();
		}
		return;
	}
	for(int i=cur;i<9;i++)
	{
		if((5-n)*8>=24-sum-i) //剪枝
		{
			c[n]=i;
			dfs(n+1,i,sum+i);
			c[n]=0;
		}
	}

}

int main()
{
	dfs(0,0,0);

	for(int i=0;i<6;i++)
		cout<<temp[i]<<" ";
		cout<<endl;
	return 0;
}