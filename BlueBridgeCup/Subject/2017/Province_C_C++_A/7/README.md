��������������

����һ�ּ򵥵�������ʽ��
ֻ�� x ( ) | ��ɵ�������ʽ��
С����������������ʽ�ܽ��ܵ���ַ����ĳ��ȡ�  

���� ((xx|xxx)x|(x|xx))xx �ܽ��ܵ���ַ����ǣ� xxxxxx��������6��

����

һ����x()|��ɵ�������ʽ�����볤�Ȳ�����100����֤�Ϸ���  

���

���������ʽ�ܽ��ܵ���ַ����ĳ��ȡ�  

���磬
���룺
((xx|xxx)x|(x|xx))xx

����Ӧ�������
6  

��ԴԼ����
��ֵ�ڴ����ģ���������� < 256M
CPU����  < 1000ms


���ϸ�Ҫ���������Ҫ��������ش�ӡ���ƣ�����������...�� �Ķ������ݡ�

ע�⣺
main������Ҫ����0;
ֻʹ��ANSI C/ANSI C++ ��׼;
��Ҫ���������ڱ��뻷�������ϵͳ�����⺯����
���������ĺ���������ȷ����Դ�ļ��� #include <xxx>
����ͨ���������ö�ʡ�Գ���ͷ�ļ���

�ύ����ʱ��ע��ѡ�����������������ͺͱ��������͡�

## Ideas

��������ƥ�����Ƶ����⣬�����뵽�ľ�����ջ��

�����ջ�Ļ������֣��� �ݹ���ϵͳջ���� �Զ���ջ�õ�����

��������ͨ���ݹ���ʵ�֡�

��������������������x�ַ������ȣ�������ʵ���ǿ���ֱ�ӵݹ��󳤶ȣ��������ַ����������ˡ�

����������Ҫ���������ַ����������ǵݹ����������������Ҫ����һ��ȫ�ֱ���`pos`��ʾ��ǰ��������λ��������

Ȼ������������������`|`���ţ�`|`�϶�����������`x`�ַ���������Ҫ�����������Ǹ���������Ҫ��������������`tmp`��`res`���ֱ��ʾ`|`��ߵ�`x`�����ұߵ�`x`�����ȡ�

��ʼ��`tmp`��`res`����0��Ȼ������`x`ʱ�� pos + 1, tmp + 1��

��ʱ�������`|`����ʱ������`res = max(res, tmp)`��Ȼ���� tmp Ϊ0������tmpҪ����`|`����ĳ��ȡ�

�������`)`��ͬ��Ҳ��`res = max(res, tmp)`��Ȼ�󷵻� res��

�������`(`����ôӦ�����ۼ�pos��Ȼ����һ���µĵݹ顣

## Code

### C++
```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
char s[100];
int len,pos;

int f() {
	int m = 0, tmp = 0;
	while(pos<len) {
		switch(s[pos]) {
			case '(': {
					pos++;
					tmp += f();
					break;
				}
			case ')': {
					pos++;
					m = max(m, tmp);
					return m;
				}
			case 'x': {
					pos++;
					tmp++;
					break;
				}
			case '|': {
					pos++;
					m = max(m, tmp);
					tmp = 0;
					break;
				}
		}
	}
	m = max(m, tmp);
	return m;
}

int main() {
	cin >> s;
	len = strlen(s);
	int ans = f();
	cout << ans << endl;
	return 0;
}
```

### Python
```python
def dfs():
    global pos
    res, tmp = 0, 0
    while pos < len(s):
        if s[pos] == '(':
            pos += 1
            tmp += dfs()
        elif s[pos] == ')':
            pos += 1
            res = max(res, tmp)
            return res
        elif s[pos] == 'x':
            pos += 1
            tmp += 1
        elif s[pos] == '|':
            pos += 1
            res = max(res, tmp)
            tmp = 0
    res = max(res, tmp)
    return res


if __name__ == '__main__':
    pos = 0
    s = input().strip()
    print(dfs())
```

## �������⣺[https://www.acwing.com/problem/content/1227/](https://www.acwing.com/problem/content/1227/)