#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(void){
    string line;
    string resultLine = "";
    stack <char> operStack;
    
    int i;
    cin >> line;
//a+b*c-(d*e+f)*g
    for(i = 0; i < line.size(); i++){
        if(isalpha(line[i])){
            resultLine += line[i];
        }else if(!operStack.empty()){
            if(line[i] == '+' || line[i] == '-'){
                while(operStack.top() == '+' || operStack.top() == '-' || operStack.top() == '*' || operStack.top() == '/'){
                    resultLine += operStack.top();
                    operStack.pop();
                    if(operStack.empty()){break;}
                }
                operStack.push(line[i]);
            }else if(line[i] == '*' || line[i] == '/'){
                while(operStack.top() == '*' || operStack.top() == '/'){
                    resultLine += operStack.top();
                    operStack.pop();
                    if(operStack.empty()){break;}
                }
                operStack.push(line[i]);
            }else if( line[i] == ')' ){   
                while( operStack.top() != '('){
                    resultLine += operStack.top();
                    operStack.pop(); 
                } 
                operStack.pop();
            }else{
                operStack.push(line[i]);
            }
        }else{
            operStack.push(line[i]);
        }
        
    }
    while(!operStack.empty()){
        resultLine += operStack.top();
        operStack.pop(); 
    }
    cout << resultLine ;
}