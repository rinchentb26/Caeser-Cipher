from resources import logo
from resources import alphabet

#function that encodes/decodes a given message
def cipher(plain_text,shift_amt,direction):
    msg=""
    if direction=="decode":
        shift_amt*=-1
    for char in plain_text:
        if char in alphabet:
            msg+=alphabet[alphabet.index(char)+shift_amt]
        else:
            msg+=char
    print(f"Here's your {direction}d message: {msg}")
runProgram=True
print(logo)
print("Welcome to Caeser Cipher.")

#loop that keeps program running until user enters "no"
while(runProgram):
    choice=input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    if choice=="encode" or choice=="decode":
        text=input("Type your message: ").lower()
        shift_amount=int(input("Type the shift number: "))
        shift_amount%=26
        cipher(plain_text=text,shift_amt=shift_amount,direction=choice)
        runCheck=input("Do you wish to continue? Type 'yes' or 'no': ").lower()
        if runCheck=="no":
            runProgram=False
            print("Adios.")
    else:
        print("Oops, Invalid Input! Try Again")
