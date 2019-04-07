#include <iostream>
#include <queue>
using namespace std;

int main(void){
    int i, cardCount;
    queue <int> dack;
    cin >> cardCount;

    for(i=1; i<cardCount+1; i++){
        dack.push(i);
    }
    for(i=1; i<cardCount; i++){
        dack.pop();
        dack.push(dack.front());
        dack.pop(); 
    }
    cout << dack.front();
}