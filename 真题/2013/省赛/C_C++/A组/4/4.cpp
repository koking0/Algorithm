#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct re_money{
	int num, renum, sub;
};

vector <re_money> vi_2;
vector <re_money> vi_8;

string i2s(int num){
	string str;
	stringstream ss;
	ss << num;
	ss >> str;
	return str;
}

int s2i(string str){
	int num;
	stringstream ss;
	ss << str;
	ss >> num;
	return num;
}

bool check_num(int num){
	if (!(num % 10)) return false;
	
	string str = i2s(num);
	if(str.find('3') != string::npos || str.find('4') != string::npos || str.find('7') != string::npos) return false;

	return true;
}

char reverse(char ch){
	switch (ch){
		case '6':return '9';
		case '9':return '6';
		default:return ch;
	}
}

int reverse_num(string str){
	string temp;
	for(int i = str.length() - 1; i > -1; i--)
		temp.insert(temp.end(), reverse(str[i]));
	
	return s2i(temp);
}

void solve(){
	for(int i = 1000; i < 10000; i++)
		if(check_num(i)){
			int re_num = reverse_num(i2s(i));
			struct re_money remoney;
			remoney.num = i;
			remoney.renum = re_num;
			
			if ((i - re_num > 200) && (i - re_num < 300)) {
				remoney.sub = i - re_num;
				vi_2.push_back(remoney);
			}
			if ((re_num - i > 800) && (re_num - i < 900)) {
				remoney.sub = re_num - i;
				vi_8.push_back(remoney);
			}
		}
	
	for(int i = 0; i < vi_2.size(); i++)
		for(int j = 0; j < vi_8.size(); j++)
			if(vi_8[j].sub - vi_2[i].sub == 558)
				cout << "赔了2百多的是： " << vi_2[i].num << " 赚了8百多的是： " << vi_8[j].num << endl;;
}

int main(){
	solve();
	return 0;
}
