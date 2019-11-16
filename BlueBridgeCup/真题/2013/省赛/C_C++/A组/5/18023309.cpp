#include <iostream>

using namespace std;

char* prefix(char* haystack_start, char* needle_start){
	// neddle_start 前缀		haystack_start 主串
	char* haystack = haystack_start;
	char* needle = needle_start;
	
	while(*haystack && *needle){
		if(*(haystack++) != *(needle++)) return NULL;  //填空位置
		// ++ 自增运算符的优先级比 * 取值运算符高
	}
	
	if(*needle) return NULL;
	
	return haystack_start;
}

int main(){
	cout << prefix("abcd1234", "abc") << endl;
	return 0;
}
