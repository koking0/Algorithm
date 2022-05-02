#include <iostream>
using namespace std;
int main()
{
	int N,K,r=100001,l=1,ans=0,h[100000],w[100000];
	cin>>N>>K;
	for(int i=0;i<N;i++)
		cin>>h[i]>>w[i];
	while(l<=r)
	{
		int mid=(l+r)/2,cnt=0;
		for(int i=0;i<N;i++)
			cnt+=(h[i]/mid)*(w[i]/mid);
		if(cnt>=K)
		{
			l=mid+1;
			ans=mid;
		}
		else
			r=mid-1;
	}
	cout<<ans<<endl;
	return 0;
}
