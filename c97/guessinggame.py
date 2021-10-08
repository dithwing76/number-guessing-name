r = 1
print(r)
gueses=0
while gueses <5:
    n=input("enter a number between 1 and 9: ")
    gueses = gueses+1
    if n<1:
        print("To low try again")
    elif n>9:
        print("To high try again")
    elif n==r:
        print("correct")
        gueses = 6 
    else :
        print("Incorrect try again")