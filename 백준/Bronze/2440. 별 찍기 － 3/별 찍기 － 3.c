#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int num;
    int i;
    int j;

    scanf("%d", &num);

    for (i = num; i > 0; i--)
    {
        for (j = 0; j < i; j++)
        {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}