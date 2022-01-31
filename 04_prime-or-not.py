n=int(input("Enter a Number: \n"))

# for i in range(2,n):
#     if(n%2!=0):
#         print("prime number")
#         break
#     else:
#         print("Not prime number")
        # break

prime=True
for i in range(2,n):
    if(n%2==0):
        prime=False
        break
if prime:
    print("Your Number is Prime Number")
else:
    print("Your Number is Not Prime Number")
