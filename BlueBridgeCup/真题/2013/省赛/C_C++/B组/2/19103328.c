#include <stdio.h>
int main(){
	int count=0;
	int a,b,c,d,e;
	for(a=1;a<10;++a){
		for(b=1;b<10;++b){
			if(b!=a){
				for(c=1;c<10;++c){
					if(c!=b&&c!=a){
						for(d=1;d<10;++d){
							if(d!=c&&d!=b&&d!=a){
								for(e=1;e<10;++e){
									if(e!=d&&e!=c&&e!=b&&e!=a){
										if((a*10+b)*(c*100+d*10+e)==(a*100+d*10+b)*(c*10+e)){
											count++;
											printf("a=%d",a);
											printf("b=%d",b);
											printf("c=%d",c);
											printf("d=%d",d);
											printf("e=%d",e);
											printf("(%d*10+%d)*(%d*100+%d*10+%d)==(%d*100+%d*10+%d)*(%d*10+%d)\n",a,b,c,e,a,d,b,c,e);										
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	printf("count=%d",count);
	return 0;	
}
