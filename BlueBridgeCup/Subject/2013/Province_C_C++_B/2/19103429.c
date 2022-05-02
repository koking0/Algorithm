#include<stdio.h>

int main()
{
    int a,b,c,d,e,n;
    n=0;
    for(a=1;a<10;a++)
    {
      for(b=1;b<10;b++)
      {
        if(a==b)
          b+=1;
        for(c=1;c<10;c++)
        {
          if(c==a || c==b)
             c+=1;
          for(d=1;d<10;d++)
          {
            if(d==a || d==b || d==c)
               d+=1;
            for(e=1;e<10;e++)
            {
              if(e==a || e==b || e==c || e==d)
                 e+=1;
              if((a*10+b)*(c*100+d*10+e)==(a*100+d*10+b)*(c*10+e))
                 n+=1;
            }
          }
        }
      }
    }
    printf("%d",n);
    return 0;
}
