//
// Created by alex on 2019/11/25.
//

#include <iostream>

using namespace std;

int main(int argc, const char *argv[]) {
    for (int i = 1; i < 20; ++i) {
        for (int j = 1; j < 20; ++j) {
            if (i < j && i * j == (i + j) * 6)
                cout << i << " " << j << endl;
        }
    }
    return 0;
}

