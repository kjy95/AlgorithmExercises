#include <iostream>
#include <math.h>
using namespace std;

int intLen(int num){
    int intLen = 1, powTen = 1;
    while(num / powTen !=0){
        intLen += 1;
        powTen *= 10;
    }
    return intLen-1;
}
int main(void){
    int N, i, k, result=0, sum, powTen = 1;
    cin >> N;
    for(i=1; i<N; i++){
        int tempNum = i; 
        int length = intLen(i) -1 ; 
        int firstNum;
        sum = i;
        while(length != -1){ 
            firstNum = tempNum/pow(10, length) ;
            sum += firstNum;
            tempNum -= firstNum * pow(10, length);
            length -= 1;
        }
        if(sum == N){
            cout<< i;
            return 0;
        }
        powTen = 1;
        result = 0;
    } 
    cout << 0;
    return 0;
}