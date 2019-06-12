//
//  main.swift
//  Queue
//
//  Created by 김지영 on 11/06/2019.
//  Copyright © 2019 김지영. All rights reserved.
//

import Foundation

let test = Int(readLine()!)!
typealias Data = (prior: Int, index: Int)
for _ in 1...test {
    let read = (readLine()!.split(separator: " ")).map{ Int($0)! }
    let n = read[0], m = read[1]
    
    var array: [Data] = readLine()!.split(separator: " ").enumerated().map{ (Int($1)!,$0)}
    var find: Bool = false
    
    while !find{
        let max = array.max(by: {$0.prior < $1.prior})!
        let first = array.remove(at: 0)
        
        if max == first{
            find = (first.index == m)
        }else{
            array.append(first)
        }
    }
    print(n - array.count)
}
