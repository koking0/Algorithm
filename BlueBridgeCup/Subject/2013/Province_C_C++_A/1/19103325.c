/*高斯出生于：1777年4月30日。
    
    在高斯发现的一个重要定理的日记上标注着：5343，因此可算出那天是：1791年12月15日。

    高斯获得博士学位的那天日记上标着：8113   

    请你算出高斯获得博士学位的年月日。

提交答案的格式是：yyyy-mm-dd, 例如：1980-03-218*/
#include<stdio.h>

#define MONTHS 12

int main() {
    int days[MONTHS] = {31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int year = 1777;
    int month = 4;
    int day = 30;
    int m = 8112;

    while (m) {
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) days[1] = 29;
        else days[1] = 28;

        day++;
        m--;

        if (day > days[month - 1]) {
            month++;
            day = 1;
        }

        if (month > 12) {
            year++;
            month = 1;
            day = 1;
        }
    }
    printf("%d-%02d-%02d", year, month, day);
    return 0;
}