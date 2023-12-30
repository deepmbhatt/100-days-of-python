#This is a code to generate a password as per required number of letters, symbols and numbers
print("Welcome to password generator")
import random
n_let=int(input("Enter the number of letters you like in your password: \n"))
n_sym=int(input("Enter the number of symbols you like in your password: \n"))
n_num=int(input("Enter the number of numbers you like in your password: \n"))
letters=[]
numbers=[]
symbols=[]
for i in range(65,91):
    letters.append(chr(i))
for i in range(98,123):
    letters.append(chr(i))
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','(',')','+']
password=""
for i in range(n_let):
    password+=letters[random.randint(0,len(letters)-1)]
for i in range(n_sym):
    password+=symbols[random.randint(0,len(symbols)-1)]
for i in range(n_num):
    password+=numbers[random.randint(0,len(numbers)-1)]
password=''.join(random.sample(password,len(password)))
print(password)