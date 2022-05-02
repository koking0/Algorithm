#include <iostream>
using namespace std;

int judge(int x,int y)
{
	if(x==3||y==4) 
		return 1;
	else
		return judge(x+1,y)+judge(x,y+1);
}

int main() 
{
	cout<<judge(0,0)<<endl;
	return 0;
}
