// you can use includes, for example:
//1번
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    int result = -1, tempResult = 0;
    int equalTopNum, k;
    for(equalTopNum = 1; equalTopNum<=6; equalTopNum++){
        for(k = 0; k<A.size();k++){
            if(A[k]!=equalTopNum){
                switch(A[k]){
                    case 1:
                        if(equalTopNum==6){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    case 2:
                        if(equalTopNum==5){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    case 3:
                        if(equalTopNum==4){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    case 4:
                        if(equalTopNum==3){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    case 5:
                        if(equalTopNum==1){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    case 6:
                        if(equalTopNum==1){
                            tempResult += 2;
                        }else{
                            tempResult += 1;
                        }
                        break;
                    default:
                        break; 
                }
                
                
            }   
           
        } 
        if(result == -1){
            result = tempResult; 
        }else{
            result = min(result, tempResult);
        }
        tempResult = 0;
    }
    return result;
}
//2번 풀었는데 여기복붙하는거 까먹음
//3번
// you can use includes, for example:
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &T) {
    int maxT;
    unsigned int pivot, maySummerIndex;
    maxT = T[0];
    for(pivot = 0; pivot<T.size(); pivot++){
        maxT = max(maxT, T[pivot]);
        for(maySummerIndex = pivot+1; maySummerIndex<T.size(); maySummerIndex++){
            if(maxT>T[maySummerIndex]){
                break;
            }
        }
        if(maySummerIndex == T.size()){
            return pivot+1;
        }
    }
    return 0;
}