# include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    long long int cases[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 3072, 9216, 27648, 82944, 248832, 746496, 2239488, 6718464, 20155392, 60466176, 181398528};
    while(t--)
    {
        long long int n, d;
        cin >> n >> d;
        long long int ans = cases[d];
        if(n < ans)
        {
            cout << n << endl;
        }
        else
        {
            cout << ans << endl;
        }
    }
    return 0;
}
