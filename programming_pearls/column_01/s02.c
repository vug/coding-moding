#include <stdio.h>

// Use 32-bit integers as array unit to generate bit-vector
#define BITS_PER_WORD 32
// SHIFT = log2(BITS_PER_WORD). 
// Division by 32 is same as bitshift by 5. To compute quotient.
#define SHIFT 5
// MASK = BITS_PER_WORD - 1
// a.k.a 31 a.k.a. 0bx11111111_11111111_11111111_11111111. To compute remainder.
// modulus by 2^32 is the same as bit-wise and with 31.
#define MASK 0x1F
#define N 10000000 // 10M numbers

int a[1 + N / BITS_PER_WORD];

void set(int i) {
    // int *word_in_vector = &a[i / BITS_PER_WORD];
    // int word_to_or = 1 << i % BITS_PER_WORD;
    // *word_in_vector |= word_to_or;
    //  OR
    // a[i / BITS_PER_WORD] |= 1 << i % BITS_PER_WORD;
    a[i >> SHIFT] |= 1 << (i & MASK);
}

void clr(int i) {
    // a[i / BITS_PER_WORD] &= ~(1 << i % BITS_PER_WORD);
    a[i >> SHIFT] &= ~(1 << (i & MASK));
}

int read(int i) {
    return a[i >> SHIFT] & (1 << (i & MASK)) ? 1 : 0;
}


void int_to_bits(char* bits, int n) {
    for (int i = 0; i < 32; i++) {
        int ci = 31 - i;
        bits[i] = (n & (1 << ci)) ? '1' : '0'; 
    }
}

void test_int_to_bits() {
    char bits[32 + 1];
    for (int m = 0; m < 40; m++) {
        int_to_bits(bits, m);
        printf("%s\n", bits);
    }
}

void test_set() {
    char bits[32 + 1];
    for (int m = 0; m < 40; m++) {
        set(m);
        int_to_bits(bits, a[1]);
        printf("%s", bits);
        int_to_bits(bits, a[0]);
        printf("%s\n", bits);
    }
}

void test_clr() {
    char bits[32 + 1];
    for (int m = 0; m < 40; m++) {
        clr(m);
        int_to_bits(bits, a[1]);
        printf("%s", bits);
        int_to_bits(bits, a[0]);
        printf("%s\n", bits);
    }
}

void test_read() {
    set(3);
    set(5);
    set(7);
    for (int m = 0; m <= 8; m ++) {
        printf("%d: %d, ", m, read(m));
    }
    printf("\n");
}

int main() {
    printf("Hi!\n");
    // test_int_to_bits();

    test_set();
    test_clr();

    // test_read();
    return 0;
}