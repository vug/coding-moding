/* 
In-memory sort using standard library method qsort

Compilation:
$ gcc -g s01.c -o s01.exe

Run:
$ cat numbers_small.txt | s01.exe > numbers_small_sorted.txt

# took 8 seconds
$ cat numbers_big.txt | s01.exe > numbers_big_sorted.txt
*/
#include <stdio.h>  // for printf, scanf
#include <stdlib.h>  // for qsort
#include <stdbool.h>

int compare_ints(const void *x, const void *y) {
    return *(const int *)x - *(const int *)y;
}

int a[10000000];

int main() {
    int i, n = 0;
    while (scanf("%d", &a[n]) != EOF) {
        n++;
    }

    qsort(a, n, sizeof(int), compare_ints);

    for(i = 0; i < n; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}