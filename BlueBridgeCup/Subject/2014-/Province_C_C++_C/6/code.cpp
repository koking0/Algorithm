#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;
bool check(int num0,int num){
	string s1,s2;
	stringstream ss0;
	ss0<<num0;
	ss0>>s1;
	stringstream ss1;
	ss1<<num;
	ss1>>s2;
	sort(s1.begin(),s1.end());
	sort(s2.begin(),s2.end());
	if(s1==s2) return true;
	else return false;
}
int main(){
	int ans=0;
	for(int a=1;a<10;a++)
	{
		for(int b=0;b<10;b++)
		{
			if(b!=a)
			{
				for(int c=0;c<10;c++)
				{
					if(c!=a&&c!=b)
					{
						for(int d=0;d<10;d++)
						{
							if(d!=a&&d!=b&&d!=c)
							{
								int num0=a*1000+b*100+c*10+d;
								int num1=a*(b*100+c*10+d);
								int num2=(a*10+b)*(c*10+d);
								if(check(num0,num1))
								{
									cout<<a<<" * "<<b*100+c*10+d<<" num1="<<num1<<endl;
									ans++;
								}
								if(((a*10+b)<(c*10+d))&&check(num0,num2))
								{
									cout<<a*10+b<<" * "<<c*10+d<<" num2="<<num2<<endl;
									ans++;
								}
							}
						}
					}
				}
			}
		}
	}
	cout<<"ans="<<ans<<endl;
	return 0;
}

