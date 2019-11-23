#include<iostream>

using namespace std;

int f(int x,int y){
	if(x==3||y==4)return 1;
	return f(x+1,y)+f(x,y+1);
	
	
}
int main(){
	cout<<f(0,0)<<end1;
	return 0;
}
