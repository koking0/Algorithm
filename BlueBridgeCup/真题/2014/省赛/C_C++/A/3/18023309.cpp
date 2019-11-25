//
// Created by alex on 2019/11/25.
//

#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

bool check(int src, int r);

using namespace std;
int ans;

int main(int argc, const char *argv[]) {
    for (int i = 1; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            if (i != j)
                for (int k = 0; k < 10; ++k) {
                    if (k != i && k != j)
                        for (int l = 0; l < 10; ++l) {
                            if (l != i && l != j && l != k) {
                                int src = i * 1000 + j * 100 + k * 10 + l;//ijkl四位数
                                //验证
                                if (j != 0) {
                                    int r1 = i * (j * 100 + k * 10 + l);//乘法结果
                                    if (check(src, r1)) {
                                        printf("%d * %d\n", i,j * 100 + k * 10 + l);
                                        ans++;
                                    }
                                }
                                //验证
                                if (k != 0) {
                                    int r2 = (i * 10 + j) * (k * 10 + l);//乘法结果
                                    if ((i * 10 + j)< (k * 10 + l)&&check(src, r2)) {
                                        printf("%d *   %d\n", i * 10 + j, k * 10 + l);
                                        ans++;
                                    }
                                }
                            }
                        }
                }
        }
    }

    cout << ans << endl;
    return 0;
}

bool check(int src, int r) {
//    先转字符串，排序，比较
    string src_str, r_str;
    stringstream ss;
    ss << src;
    ss >> src_str;
    stringstream ss1;
    ss1 << r;
    ss1 >> r_str;
    sort(r_str.begin(), r_str.end());
    sort(src_str.begin(), src_str.end());
    return r_str == src_str ? true : false;
}
