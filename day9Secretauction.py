#This is a code for Secret Aution Program in which there will be n number of bidders who bid secretly and the person with the highest bid will be declared the winner
import os   #to clear the screen
gavel=''' 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ 
                    '''
print(gavel)
print("Welcome to the secret auction program.")
bidders="yes"   #Initialize if there are any more bidders for while loop
bidder_dict={}  #Initialize a dictonary
while bidders=="yes":
    name=input("What is your name?: ")
    bid=input("What's your bid?: ₹")
    bidder_dict[name]=bid   #Add the values in the Dictonary with key
    bidders=input("Are there any more bidders? Type 'yes' or 'no'?: ").lower()
    if bidders=="yes":  
        os.system('cls')
        print(gavel)
        print("Welcome to the secret auction program.")
    else:
        os.system('cls')
        print(gavel)
highest_bid=0   #Initialize for maximan bid
for i in bidder_dict:   #To find the maximum bid
    bid=int(bidder_dict[i])
    if bid>highest_bid:
        highest_bid=bid
        winner=i
print(f"The winner is {winner} with bid of ₹{highest_bid}...")  #Print the final answer
