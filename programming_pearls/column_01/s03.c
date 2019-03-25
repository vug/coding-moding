/*
$ cat numbers_small.txt | s03.exe > numbers_small_sorted.txt
$ cat numbers_big.txt | s03.exe > numbers_big_sorted.txt
*/
#include <stdio.h>

#define BITS_PER_WORD 32
#define SHIFT 5
#define MASK 0x1F
#define N 10000000

int a[1 + N / BITS_PER_WORD];

void set(int i) {
    a[i >> SHIFT] |= 1 << (i & MASK);
}

void clr(int i) {
    a[i >> SHIFT] &= ~(1 << (i & MASK));
}

int test(int i) {
    return a[i >> SHIFT] & (1 << (i & MASK));
}

int main() {
    int num;
    // I don't think that clearing is needed
    // C initializes an array of zeroes.
    // for(int i = 0; i < N; i++) {
    //     clr(i);
    // }

    while(scanf("%d", &num) != EOF) {
        set(num);
    }

    for(int i = 0; i < N; i++) {
        if (test(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}