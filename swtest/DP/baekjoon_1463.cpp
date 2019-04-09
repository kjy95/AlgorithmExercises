#include <iostream>
#include <algorithm>
using namespace std;
int cal(int number);
const int MAX = 1000001;
int dp[MAX];

int main(void){
    int number;  
    cin >> number ;
    fill(dp, dp+MAX, -1);
    cout << cal(number);
}
int cal(int number){ 
    if(number == 1){
        return 0;
    }
    if(dp[number] != -1){
        return dp[number];
    }
    int result = cal(number - 1) +1;
    if(number%2 == 0){
        result = min(result, cal(number/2)+1); 
    }
    if(number%3 == 0){
        result = min(result, cal(number/3)+1); 
    }
    dp[number] = result;
    return dp[number];
}