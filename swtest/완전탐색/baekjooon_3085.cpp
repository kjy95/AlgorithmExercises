#include <iostream>

using namespace std;
int main(void){
    int N, i, j, k, z, maxResult = 0;
    int a,b;
    cin>> N; 
    
    char candy[N][N];
    int tempCase = N * N;
    int pivot;
    int tempCandy;
    for(i = 0; i< tempCase; i++){
        for(j = 0; j<tempCase; j++){
            cin >> candy[i][j];
        }
    }
    for(i = 0; i<tempCase; i++){
        for(j = 0; j<tempCase; j ++){
            pivot = candy[i][j];
            for(k = i; k<tempCase; k++){
                if(i == k) break;
                for(z = j; z< tempCase; z++){
                    tempCandy = candy[k][z];
                    candy[i][z] =pivot;
                    candy[i][j] = tempCandy;
                    for(a = 0; a<tempCase; a++){
                        for(b=0; b<tempCase-1; b++){
                            if(candy[a][b]==candy[a][b+1]){
                                maxResult += 1;
                            }

                        }
                    }
                }
            }
        }
    } 
}