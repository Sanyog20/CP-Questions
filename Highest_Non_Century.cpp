# include <iostream>
# include <vector>
# define int long long
 
signed main()
{
    int ans = 0;
    std::vector<int> array;
    while(1)
    {
        int n;
        std::cin >> n;
        if(n < 0)
        {
            break;
        }
        else
        {
            array.push_back(n);
            if(n > ans)
            {
                if(n < 100)
                {
                    ans = n;
                }
            }
        }
    }
    std::cout << ans << std::endl;
    return 0;
}