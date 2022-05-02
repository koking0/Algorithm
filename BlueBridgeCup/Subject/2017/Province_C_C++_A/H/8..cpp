#include <iostream>
#include <cstring>
using namespace std;
int n,g,ans=0,num[101];
bool bun[10000];
int gcd(int a,int b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}
int main()
{
	bun[0]=true;
	memset(num,0,sizeof(num));
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>num[i];
		if(i==1) g=num[i];
		else g=gcd(num[i],g);
		for(int j=0;j<10000;j++)
			if(bun[j]) bun[j+num[i]]=true;
	}
	if(g!=1)
	{
		cout<<"INF"<<endl;
		return 0;
	}
	for(int i=0;i<10000;i++)
	{
		if(!bun[i]) ans++;
	}
	cout<<ans<<endl;
	return 0;
}
