#include <stdio.h>

int memo[10001];

int main()
{
    int n, t, max = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &t);
        memo[t]++;
        if (max < t)
            max = t;
    }
    for (int i = 1; i <= max; i++)
    {
        while (memo[i]--)
            printf("%d\n", i);
    }
}