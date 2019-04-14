#include <iostream>
using namespace std;

int main(void){
    int L, P, V, result, testCase = 1;
    int divvy ,remain;
    while(1){
        cin >> L;
        cin >> P;
        cin >> V;
        if(L == 0 && P == 0 && V == 0){
            return 0;
        }
        divvy = V/P;
        remain = V%P;
        result = divvy*L ;
        if(remain>=L){   
            result+=L;
        } else{
            result+=remain;
        }
        cout << "Case "<< testCase <<": " << result << endl;
        testCase ++;
    }

}

// 4월 14일 오늘은 내 생일 > 0 <!!