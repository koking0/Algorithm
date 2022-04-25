#include<stdio.h>

void swap(int *a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void BubbleSort(int *a, int len) {
    int i, j, temp;
    for (j = len - 1; j > 0; j--) {
        for (i = 0; i < j; i++) {
            if (a[i] > a[i + 1]) {
                swap(a, i, i + 1);
            }
        }
    }
}


int main(){
    int n;
    scanf("%d",&n);
    int arr[n];

    int i;
    for (i = 0; i < n; i++)
        scanf("%d",&arr[i]);
    
    BubbleSort(arr,n);
    for(i = 0; i < n; i++)
        printf("%d ",arr[i]);
    return 0;
}

