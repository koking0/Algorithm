
/*高斯出生于：1777年4月30日。

在高斯发现的一个重要定理的日记上标注着：5343，
因此可算出那天是：1791年12月15日。

高斯获得博士学位的那天日记上标着：8113   

请你算出高斯获得博士学位的年月日。*/

#include<stdio.h>

#define MONTH 12

int ifleapyear(int year) {
    if (year % 4 == 0 && year % 100 == 0 || year % 400 == 0)
        return 29;
    else
        return 28;
}

int main() {
    int year = 1791, n = 2770;
    int array[MONTH] = {31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int month = 12, day = 15;
    while (1) {
        day++;
        if (day > array[month]) {
            month++;
            day = 1;
        }
        if (month > 12) {
            year++;
            array[1] = ifleapyear(year);
            month = 1;
        }
        n--;
        if (n == 0)
            break;
    }
    printf("%d-%d-%d \n", year, month, day);
    return 0;
}

