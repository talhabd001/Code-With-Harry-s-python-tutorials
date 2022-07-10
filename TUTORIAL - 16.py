                                         # TUTORIAL - 16
                                         #For Loops
list1=[['harry','open'],['larry',5],['marie','three']]

for iteam,value in list1:
    print(value)


 #using dictonary
dict1=dict(list1)

for iteams,value in dict1.items():
    print(iteams,'and aboltabol is',value)

for iteams in dict1: 
    print(iteam)

print(" ",end='\n\n')     #not example.


                                    #Quiz
'''
creat a list with any type of elements and find numbers ,
finally identify that,, is the number bigger(>) than 6?
'''

list3=['kamal',5,9,'rimi',78,4,8,0,int,float]
for iteam in list3:
    if str(iteam).isnumeric() and iteam > 6:
        print(iteam)