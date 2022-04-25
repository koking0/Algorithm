#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <queue>
#include <set>
using namespace std;
char *start="012345678";
char *target="087654321";
struct StateAndLevel
{
	char *state;
	int level;
	int pos0;

	StateAndLevel(char *_state,int _level,int _pos0):state(_state),level(_level),pos0(_pos0){}
};
struct cmp
{
	bool operator()(char *a,char *b)
	{
		return strcmp(a,b)<0;
	}
};
void swap(char *s, int a, int b)
{
    char t = s[a];
    s[a] = s[b];
    s[b] = t;
}
queue<StateAndLevel> q;
set<char *,cmp> allState;
void addNei(char *state,int pos,int newPos,int le)
{
	char *new_state=(char*)malloc(9* sizeof(char));
	strcpy(new_state,state);
	swap(new_state,pos,newPos);
	if(allState.find(new_state)==allState.end())
	{
		allState.insert(new_state);
		q.push(StateAndLevel(new_state,le+1,newPos));
	}
}
int main()
{
	q.push(StateAndLevel(start,0,0));
	allState.insert(start);

	while(!q.empty())
	{
		StateAndLevel sal=q.front();
		char *state=sal.state;
		int le=sal.level,pos0=sal.pos0,new_pos;
		if(strcmp(state,target)==0)
		{
			cout << le << endl;
			return 0;
		}
		new_pos=(pos0-1+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0-2+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0+1+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0+2+9)%9;
		addNei(state,pos0,new_pos,le);
		q.pop();
	}
	return 0;
}
