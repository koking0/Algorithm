#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

void i2s(long long num, string &str)
{
    stringstream ss;
    ss << num;
    ss >> str;
}
bool check(long long i1, long long i2) 
{
        string s1, s2;
        i2s(i1, s1);
        i2s(i2, s2);
        for (long long i = 0; i < s1.length(); i++)
        if (s2.find(s1[i]) != string::npos) return false;
        return true;

}


int main()
{
    for (int a = 1; a < 10; a++)
        for (int b = 0; b < 10; b++)     if (b != a)
                for (int c = 0; c < 10; c++)     if (c != a && c != b)
                        for (int d = 0; d < 10; d++)     if (d != a && d != b && d != c)
                                for (int e = 0; e < 10; e++)     if (e != a && e != b && e != c && e != d)
                                        for (int f = 0; f < 10; f++)     if (f != a && f != b && f != c && f != d && f != e) 
											                     {
                                                long long i1 = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f;
                                                long long i2 = i1 * i1;
                                                if (check(i1, i2)) 
												                        cout << i1 << endl;
                                            }

    return 0;
}
