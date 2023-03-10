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
        int arr[n];
        int i = 0;
        int j = n - 1;
        int t1 = n;
        while(i <= j)
        {
            if(i == j)
            {
                arr[i] = t1;
                t1--;
            }
            else
            {
                arr[i] = t1;
                t1--;
                arr[j] = t1;
                t1--;
            }
            i++;
            j--;
        }
        for(int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
    return 0;
}