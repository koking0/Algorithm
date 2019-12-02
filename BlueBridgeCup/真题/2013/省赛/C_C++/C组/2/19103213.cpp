#include<iostream>
using namespace std;

int main() 
{
    int sum = 0;
    for (int a = 1; a <= 9; a++)
	{
        for (int b = 1; b <= 9; b++)
		{
            if (b != a) 
			{
                for (int c = 1; c <= 9; c++) 
				{
                    if (c != b && c != a)
					{
                        for (int d = 1; d <= 9; d++) 
						{
                            if (d != c && d != b && d != a) 
							{
                                for (int e = 1; e <= 9; e++) 
								{
                                    if (e != d && e != c && e != b && e != a) 
									{
                                        if ((a * 10 + b) * (c * 100 + d * 10 + e) == (a * 100 + d * 10 + b)* (c * 10 + e)) 
										{
                                            sum++;
                                            cout << "   " << (a * 10 + b) << " * " << (c * 100 + d * 10 + e) << " = "
                                                 << (a * 100 + d * 10 + b) << " * " << (c * 10 + e) << " = "
                                                 << (a * 100 + d * 10 + b) * (c * 10 + e) << endl;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout<<sum<<endl;
}

