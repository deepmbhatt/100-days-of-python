print("Welcome to Caesar Cipher.")
print('''
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          ''')
print('''
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')
str_input=input("Enter the string: ").lower()    #The actual string to encode or decode
shift=int(input("Enter the shift: "))   #the amount of shift you have to use
what_to_do=input("Type encode to encrypt and Decode to decrypt: ").lower()  #What to do: Encode or Decode
ciphered="" #initialize the string
symbols=["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}",";",":","'",".",'"',"<",",",".",">","/","?","`","~"," "]
#Symbols array for the characters to ignore
if what_to_do=="encode":    #encryption code
    for i in range(len(str_input)):
        if str_input[i] in symbols:
            ciphered+=str_input[i]
            continue
        letter=ord(str_input[i])+shift
        if letter>122:  #incase of values getting after z we start again from a
            letter-=25
        ciphered+=chr(letter)
    print(f"The encrypted code is:\n{ciphered}")
elif what_to_do=="decode":  #decryption code
    for i in range(len(str_input)):
        if str_input[i] in symbols:
            ciphered+=str_input[i]
            continue
        letter=ord(str_input[i])-shift
        if letter<95:   #incase of values getting before a we start again from z
            letter+=25
        ciphered+=chr(letter)
    print(f"The decrypted code is:\n{ciphered}")
else:
    print("Error, type encode or decode.")