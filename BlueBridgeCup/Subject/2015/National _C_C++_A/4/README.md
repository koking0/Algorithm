## 穿越雷区

X星的坦克战车很奇怪，它必须交替地穿越正能量辐射区和负能量辐射区才能保持正常运转，否则将报废。
某坦克需要从A区到B区去（A，B区本身是安全区，没有正能量或负能量特征），怎样走才能路径最短？

已知的地图是一个方阵，上面用字母标出了A，B区，其它区都标了正号或负号分别表示正负能量辐射区。
例如：
A + - + -
- + - - +
- + + + -
+ - + - +
B + - + -

坦克车只能水平或垂直方向上移动到相邻的区。

数据格式要求：

输入第一行是一个整数n，表示方阵的大小， 4<=n<100
接下来是n行，每行有n个数据，可能是A，B，+，-中的某一个，中间用空格分开。
A，B都只出现一次。

要求输出一个整数，表示坦克从A区到B区的最少移动步数。
如果没有方案，则输出-1

例如：
用户输入：
5
A + - + -
- + - - +
- + + + -
+ - + - +
B + - + -

则程序应该输出：
10

资源约定：
峰值内存消耗 < 512M
CPU消耗  < 1000ms


请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。

注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。

提交时，注意选择所期望的编译器类型。

## Ideas

类似于迷宫问题，迷宫问题想搜索，最优问题想BFS，这道题让我们求的是A区到B区的最少移动步数，所以属于最优问题，要用BFS解决。

（这句话并不是绝对，有杠精别再杠了，你非要用DFS我也没拦着你，这只是我自己的经验总结，最优问题BFS，但如果想用DFS解决的肯定也可以，参加下面C++的代码，我还用Python实现了一遍BFS，略略略）

直接套BFS的模板，然后一点改动就是“交替地穿越正能量辐射区和负能量辐射区”，这个地方其实不用取反，因为开始位置是‘A’，目的地是‘B’，其它位置是‘+’和‘-’，单纯取反不好操作，其实只需要下一步走到的位置跟当前位置不一样就可以了。

## Code

### C++

```cpp
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int n,Ax,Ay,Bx,By;
int step=1<<30;
bool vis[107][107];
char mapp[100+7][100+7];
int dir[4][2]={{1,0},{-1,0},{0,1},{0,-1}};

bool check(int x,int y,int new_x,int new_y){
	if(new_x<1||new_x>n||new_y<1||new_y>n||mapp[x][y]==mapp[new_x][new_y])
		return false;
	return true;
}

void dfs(int x,int y,int cnt){
	if(mapp[x][y]=='B'){
		step=min(step,cnt);
		return;
	}
	
	for(int i=0;i<4;i++){
		int new_x=x+dir[i][0];
		int new_y=y+dir[i][1];
		if(!vis[new_x][new_y] && check(x,y,new_x,new_y)){
			vis[new_x][new_y]=true;
			dfs(new_x,new_y,cnt+1);
			vis[new_x][new_y]=false;
		}
	}
}

int main(){
	cin>>n;
	memset(vis,0,sizeof(vis));

	for(int i=1;i<n+1;i++){
		for(int j=1;j<n+1;j++){
			cin>>mapp[i][j];
			if(mapp[i][j]=='A'){
				Ax=i;Ay=j;
				vis[Ax][Ay]=true;
			}
		}
	}
	
	dfs(Ax,Ay,0);
	cout<<(step==1<<30?-1:step)<<endl;
	return 0;
}
```

### Python

```python
from collections import deque


def bfs(x, y, step):
	queue = deque()
	queue.append((x, y, step))
	visit[x][y] = True

	while queue:
		front = queue.popleft()
		x, y, step = front

		if matrix[x][y] == 'B':
			return step

		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = x + dx, y + dy
			if -1 < nx < n and -1 < ny < n and not visit[nx][ny] and matrix[x][y] != matrix[nx][ny]:
				visit[nx][ny] = True
				queue.append((nx, ny, step + 1))

	return -1


if __name__ == '__main__':
	n = int(input())
	visit = [[False] * n for _ in range(n)]
	matrix = [[None] * n for _ in range(n)]

	ai, aj = 0, 0
	for i in range(n):
		for j, v in enumerate(input().split()):
			matrix[i][j] = v

			if v == 'A':
				ai, aj = i, j

	print(bfs(ai, aj, 0))
```