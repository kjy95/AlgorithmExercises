string = input()
end = False
while end != True: 
    temp = string.replace("PPAP","P")
    string = temp
    count = string.count("PPAP")
    if count == 0:

        if temp =="P": 
            print("PPAP")
             
        else:
            print("NP")
        end = True 