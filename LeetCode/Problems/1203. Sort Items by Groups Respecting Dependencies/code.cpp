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
		// ʵ���� group �� project ���ڽӱ�����ͳ������ 
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
		
		// ��������
		vector<int> groupList = topologicalSort(groupAdj, groupIndegree, m);
		if (groupList.size() == 0) {
			return vector<int> ();
		}
		vector<int> itemList = topologicalSort(itemAdj, itemIndegree, n);
		if (itemList.size() == 0) {
			return vector<int> ();
		}
		
		// item �������� + item �� group �Ķ��һ��ϵ -> group �� item ��һ�Զ��ϵ
		map<int, vector<int> > group2item;
		for (int item: itemList) {
			group2item[group[item]].push_back(item);
		}
		
		// ��������������滻��Ϊ��Ŀ������������
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
