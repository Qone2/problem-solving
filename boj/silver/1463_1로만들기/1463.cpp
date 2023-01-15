#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int dp[1000001];

int foo(int n){
    if (dp[n] != -1){
        return dp[n];
    }
    if (n % 3 == 0 and n % 2 == 0){
        dp[n] = min(min(foo(n / 3), foo(n / 2)), foo(n - 1)) + 1;
        return dp[n];
    }
    if (n % 3 == 0){
        dp[n] = min(foo(n / 3), foo(n - 1)) + 1;
        return dp[n];
    }
    if (n % 2 == 0){
        dp[n] = min(foo(n / 2), foo(n - 1)) + 1;
        return dp[n];
    }
    dp[n] = foo(n-1) + 1;
    return dp[n];
}

int main(){
    int N;
    cin >> N;
    memset(dp, -1, sizeof(int) * 1000001);
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2; 

    for(int i = 5 ; i < N + 1 ; i++){
        foo(i);
    }
    cout<<foo(N);

}