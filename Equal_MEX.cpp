# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        int a[2 * n];
        int b[2 * n] = {0};
        string ans = "YES";
        for(int i = 0; i < (2 * n); i++)
        {
            cin >> a[i];
            b[a[i]]++;
        }
        for(int i = 0; i < (2 * n); i++)
        {
            if(b[i] == 0)
            {
                break;
            }
            else if(b[i] < 2)
            {
                ans = "NO";
                break;
            }
        }
        cout << ans << endl;
    }
    return 0;
}