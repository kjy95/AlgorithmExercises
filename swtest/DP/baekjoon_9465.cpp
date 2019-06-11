#include <iostream>

using namespace std;
int result = 0;
int someTowBox(int boxColNum, int topSticker[], int bottomSticker[]){
    int i;
    if(boxColNum == 1) {
        return max(topSticker[0], bottomSticker[0]);
    }
    for(i = 0; i<boxColNum; i++){ 
        
    }
    result = boxColNum;

}
int main(void){
    int i, k, testcase, StickerColCount;
    cin >> testcase;
    for(i = 0; i<testcase; i++){
        cin >> StickerColCount;
        int stickerNum;
        int topSticker[StickerColCount], bottomSticker[StickerColCount];
        for(k = 0; k<StickerColCount; k++){
            cin >> stickerNum;
            topSticker[k] = stickerNum; 
        }
        for(k = 0; k<StickerColCount; k++){
            cin >> stickerNum;
            bottomSticker[k] = stickerNum;
        }
        someTowBox(StickerColCount, topSticker, bottomSticker);
    }
    return 0;
} 