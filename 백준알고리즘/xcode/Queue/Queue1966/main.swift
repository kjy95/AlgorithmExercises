//
//  main.swift
//  Queue
//
//  Created by 김지영 on 10/06/2019.
//  Copyright © 2019 김지영. All rights reserved.
//

import Foundation

var wonderIndex : Int = 0
var ArrayLen : Int = 0
var maxVal : Int = 0
var flag : Bool = false
var result = 0

let testcase = Int(readLine()!)!
for _ in 0...testcase-1{
    if let ArrayDump = readLine(){
        var Array : [String] = ArrayDump.components(separatedBy: " ")
        wonderIndex = Int(Array[1]) ?? 0
        ArrayLen = Int(Array[0]) ?? 0
    }
    var Array : [String] = []
    if let ArrayDump = readLine(){
        Array = ArrayDump.components(separatedBy: " ")
    }
    while flag == false{
        maxVal = Int(Array.max() ?? "") ?? 0
        for index in 0...Array.count-1{
            if maxVal == Int(Array[index]) ?? 0 {
                if index == wonderIndex{
                    result = result+1
                    print(result)
                    flag = true
                    break
                }else if index != 0{
                    for _ in 0...index-1{
                        if maxVal == Int(Array.min() ?? "") ?? 0{
                            break
                        }
                        let temp = Array.remove(at: 0)
                        Array.append(temp)
                        if wonderIndex == 0{
                            wonderIndex = Array.count
                        }
                        wonderIndex -= 1
                    }
                }
                Array.remove(at: 0)
                wonderIndex -= 1
                if !Array.isEmpty{
                    maxVal = Int(Array.max() ?? "") ?? 0
                }
                result += 1
                break
            }
        }
    }
    result = 0
    flag = false
}
