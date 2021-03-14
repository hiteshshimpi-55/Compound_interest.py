# #Q 11. Write python program to calculate compound interest i.e.
# A = final amount
# P = initial principal balance
# r = interest rate
# n = number of times interest applied per time period
# t = number of time periods elapsed
# A = int(input("Enter Final Amount: "))
P = int(input("Enter Principal Balance: "))
r = float(input("Enter Interest Rate: "))
n = int(input("Enter No. of Times intrest applied : "))
t = int(input("Enter No. of Time period: "))
r=r/100
mid  = 1+r/n
expo = n*t
Ans= P*mid**expo
print(Ans)