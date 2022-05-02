class Solution {
public:
    bool isIsomorphic(string s, string t) {
    	// 无序字典，以 s 中字符为键，映射至 t 的字符为值 
        unordered_map<char, char> s2t;
        // 无序字典，以 t 中字符为键，映射至 s 的字符为值
        unordered_map<char, char> t2s;
        // s 和 t 具有相同的长度 
        int length = s.length();
        for (int i = 0; i < length; ++i) {
        	char x = s[i], y = t[i];
        	// 如果当前 i 对应的 s[i]/t[i] 已经存在并且不为 t[i]/s[i] 则无法构成同构 
        	if ((s2t.count(x) && s2t[x] != y) || (t2s.count(y) && t2s[y] != x)) {
        		return false;
			}
			s2t[x] = y;
			t2s[y] = x;
		}
		return true;
    }
};
