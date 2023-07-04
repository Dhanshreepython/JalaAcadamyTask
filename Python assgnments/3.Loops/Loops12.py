# 12. Print gender (Male/Female) program according to given M/F using switchc = input("Enter F for female, M for male and O for others :--> ")

c = input("Enter F for female, M for male and O for others :--> ")

if c == 'F'or c == 'f':
    print("Your gender is Female")
    
elif c == 'M'or c == 'm':
    print("Your gender is Male")
    
elif c == 'O'or c == 'o':
    print("Your gender is Other")
else:
    print("Please give the right input..")
