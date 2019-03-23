#include <iostream>
#include <string>
#include <stack>
using namespace std;
int main(void){
    int inputCount;
    string UserStackCommendPiece;
    int UserStackCommendPieceNum;
    int i;
    stack<int> userStack;
    cin >> inputCount; 
    for(i = 0; i < inputCount; i++){
        cin >> UserStackCommendPiece;
        if (UserStackCommendPiece.compare("push")==0){ 
            cin >> UserStackCommendPieceNum;
            userStack.push(UserStackCommendPieceNum);
        }else if(UserStackCommendPiece.compare("pop")==0){ 
            if(userStack.empty()){
                cout <<  "-1" << endl; 
            }else{
                cout <<  userStack.top() << endl;
                userStack.pop(); 
            }
        }else if(UserStackCommendPiece.compare("size")==0){
            cout << userStack.size() << endl;
        }else if(UserStackCommendPiece.compare("empty")==0){
             if(userStack.empty()){
                cout <<  "1" << endl; 
            }else{
                cout <<  "0" << endl;
            }
        }else if(UserStackCommendPiece.compare("top")==0){
            if(userStack.empty()){
                cout <<  "-1" << endl; 
            }else{
                cout <<  userStack.top() << endl;
            }
        }else{
            cout << "error" << endl;
        }
    }
}
