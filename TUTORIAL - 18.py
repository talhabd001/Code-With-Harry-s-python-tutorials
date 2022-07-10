                     # TUTORIAL - 18
i=0

while (True):
    if i+1<5:
        i=i+1
        continue

    print(i+1,end=' ')

    if (i == 44):
        break                    
    i=i+1


                                      #Quiz
'''take input from user and print congrats when he type less than 100,
otherwise continue the program '''                      


while(True):
    inp=int(input('enter the number'))
    if inp>100:
        print('congrats!you entired a number that is bigger than 100')
        break
    else:
        print('Try again')
        continue