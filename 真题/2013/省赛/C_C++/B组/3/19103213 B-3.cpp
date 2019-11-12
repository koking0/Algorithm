#include<iostream>
using namespace std;

int count=0;
void go(int stair,int step)
{
	if(stair<0)
	 	return; 
	if(stair==0)
	{
	 	if(step%2 == 0)
		 	count++;
	 	return;
	}
	go(stair-1,step+1);
	go(stair-2,step+1);
}
int main()
{
	go(39,0);
	cout<<count<<endl;
	return 0; 
}
