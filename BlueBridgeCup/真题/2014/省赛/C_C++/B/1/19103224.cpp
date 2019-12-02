#include<iostream>

using namespace std;

int main()
{
    for(int i = 0; i < 80; i++)
    {
        for(int j = 0; j < 80; j++)
        {
            if(2.3 * i + 1.9 * j == 82.3 && i < j)
            {
                cout << "beer: " << i << " drink: " << j << endl;
            }
        }
    }
    return 0;
}
