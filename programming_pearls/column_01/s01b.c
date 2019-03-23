/* 
Explanation of while (scanf("%d", &a[n]) != EOF) { n++; }

"Indian Hill C Style and Coding Standards" uses end-of-file checks
as valid examples of "embedded assignments":

"There is a time and a place for embedded assignment statements"
*/
#include <stdio.h>  // for printf, scanf
#include <stdlib.h>  // for qsort
#include <stdbool.h>  // for bool type

int compare_ints(const void *x, const void *y) {
    return *(const int *)x - *(const int *)y;
}

int a[10000000];

int main() {
    int i, n = 0;

    bool is_end = false;
    int num;
    while(!is_end) {
        // returns number of read characters, or EOF, or, feof, or ferror
        int num_chars = scanf("%d", &num);
        is_end = num_chars == EOF;
        a[n] = num;
        n++;
    }

    qsort(a, n, sizeof(int), compare_ints);  // in-place sort

    for(i = 0; i < n; i++) {
        printf("%d\n", a[i]);
    }    

    return 0;
}