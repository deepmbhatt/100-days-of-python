import os   #to clear the screen
calc_ascii='''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''
print(calc_ascii)
def division(a,b):
    return a/b
def multiply(a,b):
    return a*b
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
#The four function for four operators
condition='n' #n=new o=old e=error
while True: #constant loop 
    if condition=='o': #if old take old answer as a
        a=answer
    elif condition=='n':    #if new take new a
        os.system('cls')
        print(calc_ascii)
        a=float(input("What's the first number?: "))
    else:   #in cale of error or other value entered take new a
        os.system('cls')
        print("MATH_ERROR")
        print(calc_ascii)
        a=float(input("What's the first number?: "))
    operator=input("+\n -\n /\n *\n Pick an operation: ")
    b=float(input("What's the next number: "))
    try:    #for exceptions like divide by zero
        if operator=="+":
            answer=addition(a,b)
        elif operator=="-":
            answer=subtraction(a,b)
        elif operator=="*":
            answer=multiply(a,b)
        elif operator=="/":
            answer=division(a,b)
        else: #if wrong operator 
            condition='e'
            continue
        print(f"{a} {operator} {b} = {answer}") #for answer
        condition=input(f"Type 'o' to continue calculating with {answer}, or type 'n; to start a new calculation: ")
    except: #incase of exception
        os.system('cls')
        condition='e'
        print(calc_ascii)
    
    