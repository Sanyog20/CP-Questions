# include <iostream>
# include <bits/stdc++.h>
# define int               long long
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        int a[n];
        int x;
        for(int i = 0; i < n; i++)
        {
            cin >> x;
            if(x < 0)
            {
                a[i] = (-1) * x;
            }
            else
            {
                a[i] = x;
            }
        }
        int m1 = INT64_MAX; int m2 = INT64_MIN;
        int sum = 0;
        int c1 = 0; int c2 = 0;
        for(int i = 0; i < n; i++)
        {
            if(i % 2 == 0)
            {
                if(m1 > a[i])
                {
                    m1 = a[i];
                    c1 = i;
                }
            }
            else
            {
                if(m2 < a[i])
                {
                    m2 = a[i];
                    c2 = i;
                }
            }
        }
        if(m1 < m2)
        {
            a[c1] = m2;
            a[c2] = m1;
        }
        for(  int i = 0; i < n; i++)
        {
            if(i % 2 == 0)
            {
                sum = sum + a[i];
            }
            else
            {
                sum = sum - a[i];
            }
        }
        cout << sum << endl;
    }
    return 0;
}
