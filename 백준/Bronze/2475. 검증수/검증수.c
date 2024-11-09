#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int a, b, c, d, e;
    int answer = 0;

    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    printf("%d", ((a * a) + (b * b) + (c * c) + (d * d) + (e * e)) % 10);
}