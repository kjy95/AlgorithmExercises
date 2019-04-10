#include <iostream>
#include <string>
using namespace std;

int main(void){
    int inputCount;
    string UserStackCommendPiece;
    int i;
    
    cin >> inputCount;
    for(i = 0; i < inputCount ; i++){
        cin >> UserStackCommendPiece;
        if (UserStackCommendPiece.compare("push")){

        }else if(UserStackCommendPiece.compare("pop")){

        }else if(UserStackCommendPiece.compare("size")){

        }else if(UserStackCommendPiece.compare("empty")){

        }else if(UserStackCommendPiece.compare("top")){

        }else{
            cout << "error" << endl;
        }
    }
}