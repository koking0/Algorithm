#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int n,ans=0;
bool map[10001][10001];
int main()
{
	cin>>n;
	memset(map,0,sizeof(map));
	for(int i=0;i<n;i++)
	{
		int x1,x2,y1,y2;
		cin>>x1>>y1>>x2>>y2;
		int x_max=max(x1,x2),x_min=min(x1,x2);
		int y_max=max(y1,y2),y_min=min(y1,y2);
		for(int j=x_min;j<x_max;j++)
			for(int k=y_min;k<y_max;k++)
				map[j][k]=true;
	}
	for(int i=0;i<10000;i++)
		for(int j=0;j<10000;j++)
			if(map[i][j]) ans++;
	cout<<ans<<endl;
	return 0;
}
