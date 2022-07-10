                                       # TUTORIAL - 13
                                       #If_Else If_Else
#exm-01
list1 = [1,2,8,30] 
if 22 in list1:
    print('yes')
else:
    print('nope')    

#exm-02
list2= [5,2,6,5]
if 55 not in list2:
    print('true')
else:
    print('false')    

#exm-03
list3= [55,65,52.22]
print(52.22 not in list3)
print(64 in list3)

                                        #Quiz

"""
 first, ask the user's age.
 if he is 
 1.under 18 
 2.upper 18
 3.equal to 18

 command him :
 if 
 1= Stop!!!  Stop!!!    Stop!!!
	 You're under  than 18 years old. 
 So,Don't drive the car.
 
 2= Congrats!
	 You're upper than 18 years old.
 So, now you can drive your car in this road.
 
 3= Sorry!
	 You're equal to 18.
 So please, contact with us physically.
"""

                                         #solve
print("hey! this is police check post/n")
print("\t\tplease tell me(write using keyword) your age")
print('\t\t\t\t--->',end='')

user= int(input())

if user > 18 :
    print(" Congrats!\n\t You're upper than 18 years old.\n So, now you can drive your car in this road.")
elif user == 18 :
    print('Sorry!\n\t You\'re equal to 18.\n So please, contact with us physically.')
else:
    print("Stop!!!  Stop!!!    Stop!!!\n\t You're under  than 18 years old. \n So,Don't drive the car.")

