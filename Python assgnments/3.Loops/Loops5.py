# 5. Write a program to print largest number among three numbers.

num=15
num1=19
num2=8

if num >= num1 and num>= num2:
    largest=num
elif  num1 >= num and num1>=num2:
    largest=num1
else:
    largest=num2

print("The largest number is",largest)
