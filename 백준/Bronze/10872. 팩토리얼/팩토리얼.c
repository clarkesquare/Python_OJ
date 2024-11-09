#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    int i;
    int answer = 1;

    scanf("%d", &n);

    for(i=1;i<=n;i++)
    {
        answer *= i;
    }

    printf("%d", answer);

    return 0;
}