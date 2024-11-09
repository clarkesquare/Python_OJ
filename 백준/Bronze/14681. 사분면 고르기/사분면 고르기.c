#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int x;
    int y;

    scanf("%d", &x);
    scanf("%d", &y);
    if (x > 0)
    {
        if (y > 0)
        {
            printf("1");
        }

        else
        {
            printf("4");
        }
    }
    else
    {
        if (y > 0)
        {
            printf("2");
        }

        else
        {
            printf("3");
        }
    }

    return 0;
}