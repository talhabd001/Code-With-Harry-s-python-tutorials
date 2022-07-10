                                            # TUTORIAL - 15
                                            #Exercise 2
                                            #Faulty Calclulator
'''
Your task for today is “Faulty Calculator.” As the name gives away that, our program has something
to do with a calculator.
In my upcoming exercises, you will notice that each one of them contains a scenario. 
The reason for that is just to develop your interest in solving the problems as it is essential for you
to participate in these tasks as they will help you to develop logic-making skills. 
Each of the scenarios will be totally unique and related to your interest as I know my audience. 
And also I have made each of the scenarios myself. 

So, let me give a brief introduction of the scenario here.


Suppose that you are an invigilator in an exam. A calculator is not allowed for the exam.
You discover somehow that students are planning to cheat in exams, 
using a calculator program in Python language. Somehow,
you get your hands on the calculator program.
Now you want to alter a few results in the calculator with your own provided results to catch the students
trying to cheat using the calculator program.

The user will provide the following inputs:
1.Operator
2.he two numbers between which the operator is applied

All the results will be correct, except for these few:

45 * 3 = 555
56+9 = 77
56/6 = 4   results
'''
num1=int(input('Enter your first number\n'))
operator=input('Enter the operator\n')
num2=int(input('Enter your secound number\n'))

if num1 == 45:
    if num2 == 3:
        if operator == '*' :
            print('Your answer is - 555')

if num1 == 56:
    if num2 == 9:
        if operator == '+' :
            print('Your answer is - 77')

if num1 == 56:
    if num2 == 6:
        if operator == '/' :
            print('Your answer is - 4')

