
#입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
m = int(input("m"))
n = int(input("n"))
board  = [str(x) for x in input("board").split()]  
print(board)
count_cur = -1
heigh_list = list()
width_list = list()
#같은걸 0으로 만들기
while count_cur != 0:
    count_cur = 0 
    for heigh in range(m-1):
        for width in range(n-1):
            if board[heigh][width] == board[heigh][width+1] == board[heigh+1][width] ==  board[heigh+1][width+1] :
                # = "0"
                heigh_list.append(heigh)
                width_list.append(width)
                #oard[heigh][width+1] =  "0"
                #board[heigh+1][width] = "0"
                #board[heigh+1][width+1] = '0'
                count_cur += 1
                print(heigh_list)

    for i in range(len(heigh_list)):
        board[heigh_list[i]] = board[heigh_list[i]].replace(board[heigh_list[i]][width_list[i]],"0",2)
        board[heigh_list[i]+1] = board[heigh_list[i]+1].replace(board[heigh_list[i]+1][width_list[i]],"0",2)
        
                
                
print(board)
