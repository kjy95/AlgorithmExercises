//
//  File.swift
//  SwiftAlgo
//
//  Created by 김지영 on 12/06/2019.
//  Copyright © 2019 김지영. All rights reserved.
//

import Foundation

let inputStr = Array(readLine() ?? "")
var tempStack :[Character]=[]
var flag : Bool = false
for currentChar in inputStr{
    if currentChar == "+" || currentChar == "-" {
        if tempStack.isEmpty{
            tempStack.append(currentChar)
        }else{
            while tempStack.last == "*" || tempStack.last == "/" || tempStack.last == "+" || tempStack.last == "-"{
                let pop = tempStack.remove(at: tempStack.count - 1)
                print(pop, terminator: "")
            }
            tempStack.append(currentChar)
        }
    }else if currentChar == "*" || currentChar == "/"{
        if tempStack.isEmpty{
            tempStack.append(currentChar)
        }else{
            while tempStack.last == "*" || tempStack.last == "/"{
                let pop = tempStack.remove(at: tempStack.count - 1)
                print(pop, terminator: "")
            }
            tempStack.append(currentChar)
        }
    }else if currentChar == ")"{ 
        while tempStack.last != "(" {
            let pop = tempStack.remove(at: tempStack.count - 1)
            print(pop, terminator: "")
        } 
        tempStack.remove(at: tempStack.count - 1)
    }else if currentChar == "("{
        tempStack.append(currentChar)
    }else{
        print(currentChar, terminator: "")
    }
        
}

for _ in tempStack{
    let pop = tempStack.remove(at: tempStack.count - 1)
    if pop != ")" && pop != "(" {
        print(pop, terminator: "")
    }
}
