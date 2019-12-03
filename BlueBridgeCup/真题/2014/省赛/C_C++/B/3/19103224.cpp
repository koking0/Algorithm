#include <iostream>
using namespace std;
int sum = 0;

void f(int a, int b, int c)
{
    if(a > 0)
        f(a-1, b, c*2);
    if(b > 0)
        f(a, b-1, c-1);
    if(a==0 && b==0 && c==1) 
        sum += 1;
}

int main()
{
    f(5, 9, 2);
    cout << sum << endl;
    return 0;
} 
