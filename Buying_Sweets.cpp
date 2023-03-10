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
        int n, r;
        cin >> n >> r;
        int a[n], b[n];
        for(int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        for(int i = 0; i < n; i++)
        {
            cin >> b[i];
        }
        for(int i = 0; i < n; i++)
        {
            int ac = a[i] - b[i];
            
        }
    }
    return 0;
}