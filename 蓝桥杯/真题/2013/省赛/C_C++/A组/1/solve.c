//
// Created by alex on 2019/11/5.
//

#include <stdio.h>

int is_year(int year){
    return (year % 4 == 0 && year % 100 != 0) || year % 400 ==0 ? 1 : 0;
}

void solve(){
    int year = 1777, month = 4, day = 30;

    for (int i = 1; i < 8113; ++i) {
        day++;

        if (day == 32){
            if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10){
                day = 1;
                month++;
            }
            if (month == 12){
                day = 1;
                month = 1;
                year++;
            }
        }

        if (day == 31){
            if (month == 4 || month == 6 || month == 9 || month == 11){
                day = 1;
                month++;
            }
        }

        if ((day == 30 && is_year(year) == 1) || (day == 29 && is_year(year) == 0)){
            if (month == 2){
                day = 1;
                month++;
            }
        }
    }

    printf("%d-%02d-%02d", year, month, day);
}

int main(){
    solve();
    return 0;
}