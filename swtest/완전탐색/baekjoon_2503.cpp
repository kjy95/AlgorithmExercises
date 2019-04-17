#include <iostream>
using namespace std;
int main(void){
    int i, j, askTime, thinkNum, strike, ball, result = -1;
    int possibleNum[729];
    fill(possibleNum, possibleNum + 729, 0);
    cin >> askTime;

    cin >> thinkNum;
    cin >> strike;
    cin >> ball;
    
    for(j = 0; j<729; j++){
         //1: 0을 1로 바꿈
        int three = thinkNum / 100;
        int two = (thinkNum - three * 100) / 10;
        int one =  (thinkNum - three * 100 - two*10);
        switch (strike)
        {
            case 1:
                if(j/100 == three ||(j - three * 100) / 10 == two ||(j - three * 100 - two*10)== one){
                    possibleNum[j] == 1;
                }
                break;
            case 2:
                for(i = 0; i<729; i++){

                }
                break;
            case 3:
                result = 1;
                break;
            default:
                break;
        }
         if(ball == 1){

         }
    }
    
    for(i = 0; i<askTime;i++){
        cin >> thinkNum;
        cin >> strike;
        cin >> ball;
        for(j = 0; j<729; j++){
            //1: 0을 1로 바꿈
        }
        //2: 1을 0으로 못바꿈
    }
}