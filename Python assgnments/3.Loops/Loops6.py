# 6. Write a program to print even number between 10 and 20 using while

x=int(input("Enter a number: "))
i=1
while i <= x:
    if i % 2 == 0:
        print(i,end=" ")
    i= i+1
