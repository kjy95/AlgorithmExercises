#include <iostream>

using namespace std;

int main(void){
    int testcase, triArray[50];
    int testNum,i,j,k, sumResult = 0, result = -1;
    cin>> testcase;
    for(i=1;i<50;i++){
        triArray[i] = i*(i+1)/2;
    }

    while(testcase){
        cin>> testNum;
        for(i=1;i<50;i++){
            for(j=1;j<50;j++){
                for(k=1;k<50;k++){
                    if(testNum == triArray[i]+triArray[j]+triArray[k]){
                        result = 1;
                        cout<<result<<endl; 
                        break;
                    } 
                }
                if(result == 1) break;
            }  
            if(result == 1) break;   
        }
        if(result!=1) cout << 0<< endl; 
        result = -1;
        testcase--;
    }
}