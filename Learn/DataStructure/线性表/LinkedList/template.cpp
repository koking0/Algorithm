#include <iostream> 

using namespace std;

typedef int DataType;	// 利用 typedef 将链表元素类型设置为 int 

class Node {
	public:
		DataType data;	// 数据域：指定数据元素的类型 
		Node *next;		// 指针域：指向后继节点的地址 
};

class LinkList {
	private:
		 Node *head;	// 头结点 
	public:
		LinkList() {
			/* 初始化：构建一个空的单链表 L */
			head = new Node;
			head->data = 0;		// 头结点的数据域定义为 0 
			head->next = NULL;	// 头结点的后继节点定义为 NULL 
		}
		void headCreateLinkList(int n) {
			/* 头插法创建链表 
				n - 初始链表长度 
			*/
			if (n < 0) {
				cout << "The length of the linked list cannot be less than 0!" << endl;
				return; 
			}
			Node *item;		// item 表示当前正在处理的结点  
			for (int i = 0; i < n; i++) {
				item = new Node;
				cout << "Please enter the value of the " << i + 1 << "-th node value:";
				cin >> item->data;
				item->next = head->next;	// 将当前结点的后继节点设置为头结点的后继节点 
				head->next = item;			// 将头结点的后继节点设置为当前结点 
				cout << i + 1 << "-th node value:" << item->data << endl;	
			}
		}
		void tailCreateLinkList(int n) {
			/* 尾插法创建链表 
				n - 初始链表长度 
			*/
			if (n < 0) {
				cout << "The length of the linked list cannot be less than 0!" << endl;
				return; 
			}
			
			Node *tail, *item;		// tail 用于指向链表的尾结点，item 表示当前正在处理的结点  
			tail = head;	// 初始化后链表为空，尾节点即头结点 
			for (int i = 0; i < n; i++) {
				item = new Node;
				cout << "Please enter the value of the " << i + 1 << "-th node value:";
				cin >> item->data;
				item->next = NULL;	// 新增结点要插入当前链表的末尾，因此 item 下一个结点的地址为 NULL 
				tail->next = item;	// 当前链表的尾节点的后继结点设置为 item 
				tail = item;		// 将当前链表的尾节点设置为 item 
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
			/* 按序查找 */
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
			/* 按值査点 */
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
			/* 在第 idx 结点后插入值为 v 的结点 */
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
	
	cout << "\t1.创建单链表\n\t2.遍历链表\n\t3.按序查值\n\t4.按值査点\n\t5.插入结点\n0.退出\n";
	
	int command = -1;
	while (command) {
		cout << "\nPlease enter the command: ";
		cin  >> command;
		switch (command) {
			case 1:
				int length;
				cout << "Please enter the length of the singly linked list: ";
				cin >> length;
				cout << "\n1.尾插法\t2.头插法\n";
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
