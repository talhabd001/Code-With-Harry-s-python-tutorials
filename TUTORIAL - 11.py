                                                # TUTORIAL - 11
                                                # Exercise-01 /Creat Dictionary
'''
 Question:
          Creat a dictionary and take input from the user and return  the meaning of the word from the dictionary
'''
print("This dictionary have stored the below's following words:\n\t",)

var1= "01)Probably\n"
var2= "02)Heavenly\n"
var3= "03)Purchase\n"
print(var1+var2+var3)

dicstore={"Probably":"used to say that something is likely to happen,likely to be true,possibly",
          "Heavenly":"very pleasing,wonderful",
          "Purchase":"to buy something by paying money for it"}


print("Write the word that you want to know in details & click \"Enter\"\n-->>",end=" ")

print("The defination of your word meaning is \n-->>"+dicstore[input()])



