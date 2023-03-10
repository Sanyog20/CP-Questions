#include <stdio.h>
int operations(int *);

int main(void)
{
    int n;
    int t;
    scanf("%d", &n);
    scanf("%d", &t);
    int i;
    int k;
    int ans = n;
    for(i = 0 ; i < t; i++)
    {
        scanf("%d", &k);
        if(k < n)
        {
            if(k % 2 != 0)
            {
                ans = ans - k;
            }
            else
            {
                ans = ans / k; 
            }
        }
        else if(k > n)
        {
            if(k % 2 != 0)
            {
                ans = ans * k;
            }
            else
            {
                ans = ans + k;
            }
        }
        else
        {
            n = n + n;
        }
    }
    printf("%d", ans);
    return 0;
}
