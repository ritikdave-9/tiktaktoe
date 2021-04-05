b ={
    'a1':' ','a2':' ','a3':' ',
    'a4':' ','a5':' ','a6':' ',
    'a7':' ','a8':' ','a9':' ',
}
player = 1
total_moves = 0
end_check = 0

def check():
    # for player one 
    # for horizontal
    if b['a1'] == 'x'and b['a2']=='x'and b['a3']=='x':
        print('player 1 won')
        return 1
    if b['a4'] == 'x'and b['a5']=='x'and b['a6']=='x':
        print('player 1 won')
        return 1
    if b['a7'] == 'x'and b['a8']=='x'and b['a9']=='x':
        print('player 1 won')
        return 1
    # for vertical 
    if b['a1'] == 'x'and b['a3']=='x'and b['a7']=='x':
         print('player 1 won')
         return 1
    if b['a2'] == 'x'and b['a5']=='x'and b['a8']=='x':
         print('player 1 won')
         return 1
    if b['a3'] == 'x'and b['a6']=='x'and b['a9']=='x':
         print('player 1 won')
         return 1
    # for diagnal 
    if b['a1'] == 'x'and b['a5']=='x'and b['a9']=='x':
        print('player 1 won')
        return 1
    if b['a3'] == 'x'and b['a5']=='x'and b['a7']=='x':
        print('player 1 won')
        return 1
   
    # for player 2
    if b['a1'] == 'o'and b['a2']=='o'and b['a3']=='o':
        print('player 2 won')
        return 1
    if b['a4'] == 'o'and b['a5']=='o'and b['a6']=='o':
        print('player 2 won')
        return 1
    if b['a7'] == 'o'and b['a8']=='o'and b['a9']=='o':
        print('player 2 won')
        return 1
    # for vertical 
    if b['a1'] == 'o'and b['a3']=='o'and b['a7']=='o':
        print('player 2 won')
        return 1
    if b['a2'] == 'o'and b['a5']=='o'and b['a8']=='o':
        print('player 2 won')
        return 1
    if b['a3'] == 'o'and b['a6']=='o'and b['a9']=='o':
        print('player 2 won')
        return 1
    # for diagnal 
    if b['a1'] == 'o'and b['a5']=='o'and b['a9']=='o':
        print('player 2 won')
        return 1
    if b['a3'] == 'o'and b['a5']=='o'and b['a7']=='o':
        print('player 2 won')
        return 1
    return 0

print('00000000000000000000000000000000000000000000000000')
print(''' 
player one and two can input "x" and "o" by there position in this manner 
''')
print(''' 
  a1 | a2 | a3
     +    +  
  a4 | a5 | a6
     +    +
  a7 | a8 | a9
  ''')  
print("0000000000000000000000000000000000000000000000000000") 
input('press enter to play best of luck')

while True:
    print(b['a1']+'|'+b['a2']+'|'+b['a3'])
    print('-+-+-')
    print(b['a4'] + '|' + b['a5'] + '|' + b['a6'])
    print('-+-+-')
    print(b['a7'] + '|' + b['a8'] + '|' + b['a9'])  
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break

    while True:
        if player == 1:
            p1 = input('player no.1 chance : ')
            if p1 in b and b[p1]==' ':
                b[p1]='x'
                player = 2
                break 
            else:
                print('chutiya hai kya ! vaapis input kar !')
                continue
        else:
            p2 = input('player no.2 chance : ')
            if p2 in b and b[p2]==' ':
                b[p2]='o'
                player = 1
                break
            else:
                print('chutiya hai kya ! vaapis input kar !')
                continue
    total_moves+=1
    print('00000000000000000000000000000000000')

  
    
    

    