#include<stdio.h>
  
int f(int x,int y)
{  
      if(x==3||y==4) 
	  return 1; 
	  else
      return f(x+1,y)+f(x,y+1);//从第一格开始走，向左或向右。 
}
  
int main()
{
     printf("%d",f(0,0));
     return 0;
}
