#include <stdio.h>
int main(){
	int x;
	int y;
	for(x=1;x<30;x++){
		for(y=1;y<30;y++){
			if(x*y==6*(x+y)&&x<y){
				if((y-x)<=8){
				printf("小明的较小妹妹的年龄是%d\n",x);
				}
			}
		}
	}
return 0;
} 
