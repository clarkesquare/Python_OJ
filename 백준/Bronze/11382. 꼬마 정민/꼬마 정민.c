#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    long long a;
    long long b;
    long long c;

    scanf("%lld %lld %lld", &a, &b, &c);
    printf("%lld", a + b + c);

    return 0;
}