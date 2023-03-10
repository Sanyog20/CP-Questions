 int k=0;
        while(k!=c){
            // cout<<n<<" ";
            v.push_back(n);
            k++;
            n--;
        }
        // cout<<n-2<<" ";
        v.push_back(n-2);
        n--;
        while(n>0){
            // cout<<n-1<<" ";
            v.push_back(0);
            n--;
        }