class Stack{
	private:
		int num;	// Õ»ÈÝÁ¿
		int idx;	// Õ»¶¥Ö¸Õë  
		int* data;	// Õ»ÖÐÔªËØ 
	public:
		Stack(int n) {
			this->num = n;
			this->idx = -1;
			this->data = new int[n];
		}
		~Stack() {
			delete [] this->data;
		}
		bool empty() {
			return this->idx == -1;
		}
		bool full() {
			return this->idx == this->num - 1;
		}
		void push(int x) {
			if (this->full()) {
				cout << "over flow" << endl;
				return;
			}
			this->data[++this->idx] = x;
		}
		void pop() {
			if (this->empty()) {
				cout << "under flow" << endl;
				return;
			}
			this->idx--;
		}
		int top() {
			if (this.empty()) {
				cout << "under flow" << endl;
				return;
			}
			return this->data[this->idx];
		}
};
