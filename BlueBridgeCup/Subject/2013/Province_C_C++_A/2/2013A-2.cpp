#include<stdio.h>
  
int f(int x,int y)
{  
      if(x==3||y==4) 
	  return 1; 
	  else
      return f(x+1,y)+f(x,y+1);//�ӵ�һ��ʼ�ߣ���������ҡ� 
}
  
int main()
{
     printf("%d",f(0,0));
     return 0;
}
