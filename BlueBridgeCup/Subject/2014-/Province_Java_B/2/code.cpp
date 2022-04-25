 #include <iostream>
 #include <iomanip>
 
 using namespace std;
 
 int main() {
 	double index = 1, num = 0;
 	while(num < 15.0) {
 		num += 1 / index;
 		index++;
	 }
	 cout << fixed << setprecision(0) << "index = " << index << ", num = " << num << endl;
	 return 0;
 }
