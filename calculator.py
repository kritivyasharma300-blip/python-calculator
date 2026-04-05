# To design calculator by using python 

num_1 =float(input("enter your number : "))
num_2 =float(input("enter your number : "))

op=input("enter your operation , ('+','-','%','*','/') : ")
 
if op=='+':
    print("Result",num_1 + num_2)
elif op=='-':
    print("Result",num_1 - num_2)
elif op == '*':
    print("Result",num_1 * num_2)
elif op=='/':
    print("Result",num_1 / num_2)
elif op=='%':
    print("Result",num_1 % num_2)

else :
    print("ERROR YOUR  VALUE NOT VALID ")
