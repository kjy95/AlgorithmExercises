#include <iostream>

using namespace std;

int main(void){
    int testcase, triArray[70];
    int testNum,i,j,k, sumResult = 0, result = -1;
    cin>> testcase;
    for(i=1;i<70;i++){
        triArray[i] = i*(i+1)/2;
    }
    for(i=1;i<70;i++){
        cout<< triArray[i] << endl;
    }

    while(testcase){
        cin>> testNum;
        for(i=1;i<70;i++){
            sumResult += triArray[i];
            for(j=1;j<70;j++){
                sumResult += triArray[j]; 
                for(k=1;k<70
                ;k++){
                    sumResult += triArray[k];
                    if(testNum == sumResult){
                        result = 1;
                        cout<<result<<endl; 
                        break;
                    } 
                    
                    sumResult = 0;
                }
                sumResult = 0;
                if(result == 1) break;
            }  
                sumResult = 0; 
            if(result == 1) break;   
        }
                sumResult = 0;
        if(result!=1) cout << 0<< endl; 
        result = -1;
        testcase--;
    }
}