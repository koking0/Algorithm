class Solution {
public:
	vector<int> topologicalSort(vector<vector<int> > &adj, vector<int> &indegree, int n) {
		queue<int> que;
		vector<int> res;
		for (int i=0; i < n; i++) {
			if (indegree[i] == 0) {
				que.push(i);
			}
		}
		while (!que.empty()) {
			int front = que.front();
			que.pop();
			res.push_back(front);
			for (int item:adj[front]) {
				if (!(--indegree[item])) {
					que.push(item);
				}
			}
		}
		return res.size() == n ? res : vector<int> ();
	}
	
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
		for(int i=0; i < group.size(); i++) {
			if (group[i] == -1) {
				group[i] = m;
				m++;
			}
		}
		// 实例化 group 和 project 的邻接表和入度统计数组 
		vector<vector<int> > groupAdj(m, vector<int>());
		vector<int> groupIndegree(m, 0);
		vector<vector<int> > itemAdj(n, vector<int>());
		vector<int> itemIndegree(n, 0);
		
		int length = group.size();
		for(int i=0; i < length; i++) {
			int currentGroup = group[i];
			for(int item:beforeItems[i]) {
				int beforeGroup = group[item];
				if (beforeGroup != currentGroup) {
					groupAdj[beforeGroup].push_back(currentGroup);
					groupIndegree[currentGroup]++;
				}
			}
		}
		for(int i=0; i < n; i++) {
			for(int item:beforeItems[i]) {
				itemAdj[item].push_back(i);
				itemIndegree[i]++;
			}
		}
		
		// 拓扑排序
		vector<int> groupList = topologicalSort(groupAdj, groupIndegree, m);
		if (groupList.size() == 0) {
			return vector<int> ();
		}
		vector<int> itemList = topologicalSort(itemAdj, itemIndegree, n);
		if (itemList.size() == 0) {
			return vector<int> ();
		}
		
		// item 拓扑排序 + item 到 group 的多对一关系 -> group 到 item 的一对多关系
		map<int, vector<int> > group2item;
		for (int item: itemList) {
			group2item[group[item]].push_back(item);
		}
		
		// 组的拓扑排序结果替换成为项目的拓扑排序结果
		vector<int> res;
		for (int groupId: groupList) {
			vector<int> items = group2item[groupId];
			for (int item:items) {
				res.push_back(item);
			}
		}
		return res;
    }
};
