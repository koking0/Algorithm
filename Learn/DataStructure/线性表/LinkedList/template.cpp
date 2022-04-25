#include <iostream> 

using namespace std;

typedef int DataType;	// ���� typedef ������Ԫ����������Ϊ int 

class Node {
	public:
		DataType data;	// ������ָ������Ԫ�ص����� 
		Node *next;		// ָ����ָ���̽ڵ�ĵ�ַ 
};

class LinkList {
	private:
		 Node *head;	// ͷ��� 
	public:
		LinkList() {
			/* ��ʼ��������һ���յĵ����� L */
			head = new Node;
			head->data = 0;		// ͷ������������Ϊ 0 
			head->next = NULL;	// ͷ���ĺ�̽ڵ㶨��Ϊ NULL 
		}
		void headCreateLinkList(int n) {
			/* ͷ�巨�������� 
				n - ��ʼ������ 
			*/
			if (n < 0) {
				cout << "The length of the linked list cannot be less than 0!" << endl;
				return; 
			}
			Node *item;		// item ��ʾ��ǰ���ڴ���Ľ��  
			for (int i = 0; i < n; i++) {
				item = new Node;
				cout << "Please enter the value of the " << i + 1 << "-th node value:";
				cin >> item->data;
				item->next = head->next;	// ����ǰ���ĺ�̽ڵ�����Ϊͷ���ĺ�̽ڵ� 
				head->next = item;			// ��ͷ���ĺ�̽ڵ�����Ϊ��ǰ��� 
				cout << i + 1 << "-th node value:" << item->data << endl;	
			}
		}
		void tailCreateLinkList(int n) {
			/* β�巨�������� 
				n - ��ʼ������ 
			*/
			if (n < 0) {
				cout << "The length of the linked list cannot be less than 0!" << endl;
				return; 
			}
			
			Node *tail, *item;		// tail ����ָ�������β��㣬item ��ʾ��ǰ���ڴ���Ľ��  
			tail = head;	// ��ʼ��������Ϊ�գ�β�ڵ㼴ͷ��� 
			for (int i = 0; i < n; i++) {
				item = new Node;
				cout << "Please enter the value of the " << i + 1 << "-th node value:";
				cin >> item->data;
				item->next = NULL;	// �������Ҫ���뵱ǰ�����ĩβ����� item ��һ�����ĵ�ַΪ NULL 
				tail->next = item;	// ��ǰ�����β�ڵ�ĺ�̽������Ϊ item 
				tail = item;		// ����ǰ�����β�ڵ�����Ϊ item 
				cout << i + 1 << "-th node value:" << item->data << endl;
			}
		}
		void travalLinkList() {
			if (!head || head->next == NULL) {
				cout << "The linked list is empty!" << endl;
				return;
			}
			Node *p = head;
			while (p->next != NULL) {
				p = p->next;
				cout << p->data << " -> ";
			}
			cout << "NULL" << endl;
		}
		Node * getElement(int idx) {
			/* ������� */
			Node *p = head->next;
			if (idx < 0) {
				cout << "Index value cannot be less than 0!" << endl; 
			} else if (idx == 0) {
				return p;
			} else {
				for (int i = 0; p->next && i < idx; i++) {
					p = p->next;
				}
				return p;
			}
		}
		Node * localElement(DataType e) {
			/* ��ֵ�˵� */
			if (!head || head->next == NULL) {
				cout << "The linked list is empty!" << endl;
				return NULL;
			}
			Node *p = head;
			while (p != NULL) {
				if (p->data == e) {
					return p;
				}
				p = p->next;
			}
			return p;
		}
		void insertNode(int idx, DataType v) {
			/* �ڵ� idx �������ֵΪ v �Ľ�� */
			Node *item = new Node;
			item->data = v;
			Node *p = head;
			for (int i = 0; i < idx; i++) {
				p = p->next;
			}
			item->next = p->next;
			p->next = item;
		}
}; 

int main() {
	LinkList L;
	int index, value;
	
	cout << "\t1.����������\n\t2.��������\n\t3.�����ֵ\n\t4.��ֵ�˵�\n\t5.������\n0.�˳�\n";
	
	int command = -1;
	while (command) {
		cout << "\nPlease enter the command: ";
		cin  >> command;
		switch (command) {
			case 1:
				int length;
				cout << "Please enter the length of the singly linked list: ";
				cin >> length;
				cout << "\n1.β�巨\t2.ͷ�巨\n";
				cin >> command;
				if (command == 1) {
					L.tailCreateLinkList(length);
				} else if (command == 2) {
					L.headCreateLinkList(length);
				}
				break;
			case 2:
				L.travalLinkList();
				break;
			case 3:
				cout << "Please enter the search serial number: ";
				cin >> index;
				cout << index << "-th value: " << L.getElement(index)->data << endl;
				break;
			case 4:
				cout << "Please enter the search value: ";
				cin >> value;
				if (L.localElement(value) != NULL) {
					cout << "The " << value << " is in the link list." << endl;
				} else {
					cout << "Value " << value << " is not in the link list." << endl;
				}
				break;
			case 5:
				cout << "Please enter the insert location: ";
				cin >> index;
				cout << "Please enter the insert value: ";
				cin >> value;
				L.insertNode(index, value);
				break;
			default:
				break;
		}
	}
	return 0;
}
