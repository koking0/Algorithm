#include <iostream> 

using namespace std;

class ShareStack {
	private:
		int num;	// Õ»ÈÝÁ¿
		int idx1;	// 1ºÅÕ»¶¥Ö¸Õë  
		int idx2;	// 2ºÅÕ»¶¥Ö¸Õë  
		int* data;	// Õ»ÖÐÔªËØ 
	public:
		 ShareStack(int n) {
		 	this->num = n; 
		 	this->idx1 = -1;
		 	this->idx2 = n;
		 	this->data = new int[n];
		 }
		 ~ShareStack() {
			delete [] this->data;
		}
		 bool s1Empty() {
		 	return this->idx1 == -1;
		 } 
		 bool s2Empty() {
		 	return this->idx2 == this->num;
		 } 
		 bool full() {
		 	return this->idx2 - this->idx1 == 1;
		 }
		 void s1Push(int x) {
		 	if (this->full()) {
		 		cout << "over flow" << endl;
		 		return;
			 }
			 this->data[++this->idx1] = x;
		 }
		 void s2Push(int x) {
		 	if (this->full()) {
		 		cout << "over flow" << endl;
		 		return;
			 }
			 this->data[--this->idx2] = x;
		 }
		 void s1Pop() {
		 	if (this->s1Empty()) {
		 		cout << "under flow" << endl;
		 		return;
			 }
			 this->idx1--;
		 }
		 void s2Pop() {
		 	if (this->s2Empty()) {
		 		cout << "under flow" << endl;
		 		return;
			 }
			 this->idx2++;
		 }
		 int s1Top() {
		 	if (this->s1Empty()) {
		 		cout << "under flow" << endl;
		 		return -1;
			 }
			 return this->data[this->idx1];
		 }
		 int s2Top() {
		 	if (this->s2Empty()) {
		 		cout << "under flow" << endl;
		 		return -1;
			 }
			 return this->data[this->idx2];
		 }
};
