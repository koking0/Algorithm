#include<stdio.h>
int main(){
	int x,y;
	for(x=0;x<100;x++){
		for(y=0;y<100;y++){
			if(2.3*x+1.9*y==82.3&&x<y){
				printf("他买了%d罐啤酒\n",x);
			}
		}
	}
	
return 0;	
	
	
}
