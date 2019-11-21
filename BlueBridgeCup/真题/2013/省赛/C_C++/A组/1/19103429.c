#include<stdio.h>
int rn(int year)
{
   int month2;
   if(year%4==0 && year%400!=0 || year%400==0)
      month2=29;
   else
      month2=28;
   return month2;
}
int main()
{
    int year=1791;
    int month=12;
    int day=15;
    int sum1=5343;
    int sum2=8113;
    day=1;month=1; year+=1;sum1=sum1+31-15+1;
    for(int i=1;i<=(8113-5343+31-15+1)/365+1;i++)
   {
    switch(month)
    {
      case 1:
        sum1+=31;
        month+=1;     
        if(sum2-sum1<rn(year))
        break;
      case 2:
        sum1+=rn(year);
        month+=1;     
        if(sum2-sum1<31)
        break;
      case 3:
        sum1+=31;
        month+=1;     
        if(sum2-sum1<30)
        break;
      case 4:
        sum1+=30;
        month+=1;   
        if(sum2-sum1<31)
        break;
      case 5:
        sum1+=31;
        month+=1;     
        if(sum2-sum1<30)
        break;
      case 6:
        sum1+=30;
        month+=1;    
        if(sum2-sum1<31)
        break;
      case 7:
        sum1+=31;
        month+=1;    
        if(sum2-sum1<31)
        break;
      case 8:
        sum1+=31;
        month+=31; 
        if(sum2-sum1<30)
        break; 
      case 9:
        sum1+=30;
        month+=1; 
        if(sum2-sum1<31)
        break;     
      case 10:
        sum1+=31;
        month+=1;   
        if(sum2-sum1<30)
        break;
      case 11:
        sum1+=30;
        month+=1;
        if(sum2-sum1<31)
        break;
      case 12:
        sum1+=31;
        month=1;
        year+=1;
        if(sum2-sum1<31)
        break;
    }
   }
    day=day+(sum2-sum1);
    printf("%d年%d月%d日",year,month,day);
    return 0;
}
