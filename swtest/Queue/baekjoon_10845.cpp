#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(void){
    int i, commandLine, pushNum;
    string command;
    queue <int> Queue;
    cin >> commandLine ;
    for(i = 0; i<commandLine; i++){
        
        cin >> command; 
        if(command == "push"){
            cin >> pushNum;
            Queue.push(pushNum);
        }else if(command == "pop"){
            if(Queue.empty() != 0){
                cout << -1 << endl;;
            }else{
                cout << Queue.front() << endl;;
                Queue.pop();
            }
        }else if(command == "size"){ 
            cout << Queue.size() << endl;; 
        }else if(command == "empty"){
            if(Queue.empty() != 0){
                cout << 1 << endl;;
            }else{
                cout <<0 << endl;;
            }
        }else if(command == "front"){
            if(Queue.empty() != 0){
                cout << -1 << endl;
            }else{
                cout << Queue.front() << endl;;
            }
        }else if(command == "back"){
            if(Queue.empty() != 0){
                cout << -1 << endl;;
            }else{
                cout << Queue.back() << endl;; 
            }
        }
    }
}