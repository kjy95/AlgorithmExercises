//
//  main.swift
//  Queue
//
//  Created by 김지영 on 11/06/2019.
//  Copyright © 2019 김지영. All rights reserved.
//

import Foundation

let inputnum = Int(readLine() ?? "") ?? 0

for temp in 1...inputnum/2{
    if inputnum % temp == 0{
        print(temp, terminator: " ")
    }
}

print(inputnum)
