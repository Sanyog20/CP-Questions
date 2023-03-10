# include <iostream>
# include <boost/math/common_factor.hpp>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int n, k;
        cin >> n >> k;
        int t1 = boost::math::lcm(n, k);
        cout << t1 / k << endl;
    }
    return 0;
}