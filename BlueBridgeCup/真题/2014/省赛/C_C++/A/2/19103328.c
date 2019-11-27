#include <stdio.h>
int main(){
	int n=1;
	int count;
	for(n=1;n<11;n++){
		count=2*n+1;
	}
	printf("连续对折十次，中间切一刀能得到%d条面条\n",count);
return 0;
}
