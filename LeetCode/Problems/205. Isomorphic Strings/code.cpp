class Solution {
public:
    bool isIsomorphic(string s, string t) {
    	// �����ֵ䣬�� s ���ַ�Ϊ����ӳ���� t ���ַ�Ϊֵ 
        unordered_map<char, char> s2t;
        // �����ֵ䣬�� t ���ַ�Ϊ����ӳ���� s ���ַ�Ϊֵ
        unordered_map<char, char> t2s;
        // s �� t ������ͬ�ĳ��� 
        int length = s.length();
        for (int i = 0; i < length; ++i) {
        	char x = s[i], y = t[i];
        	// �����ǰ i ��Ӧ�� s[i]/t[i] �Ѿ����ڲ��Ҳ�Ϊ t[i]/s[i] ���޷�����ͬ�� 
        	if ((s2t.count(x) && s2t[x] != y) || (t2s.count(y) && t2s[y] != x)) {
        		return false;
			}
			s2t[x] = y;
			t2s[y] = x;
		}
		return true;
    }
};
