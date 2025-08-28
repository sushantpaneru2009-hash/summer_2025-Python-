# a = 5
# b = 0
# while a > b:
#     a -=1
#     if a == 2:
#         continue # break only the loop in the condition only not whole loop
#     print("hello world",a)
# #  difference between break and continue
# a = 5
# b = 0
# while a > b:
#     a -= 1
#     if a==3:
#         break # break whole loop if meet the condition
#     print("hello world",a)
    
    
#  iteration : process of iterating through the first data to last data in the iterable 
#  iterator : is a variabl ethat is used to perform interaction in iterable 
#  iterable : is a data type that can be iterated over (string, list, tuple, dictionary, set)

# iterable = [1,2,3,4,5,6,"sushant"]
# for i in iterable:
#     print("hello world",i)

# a = ['neymar','messi','pele']
# for i in a:
#     print('i like',i)
    
 
# random_list = [1,2,3,4,5,6,7,8,9,10]
# square_list = []

# for i in random_list:
#     square_list.append(i**2)
# print(square_list) 
        
    
# for i in range(1,21):
#     print(i)
#     print(i**2)

a = '*'
for i in range(1,6):
    print((a*i))
    
# 
     
# while True:
#     output = input("Enter '+', '-', '*', '/' or 'q' to quit: ")
#     if output == 'q':
#         continue
    
#     num1 = int(input("First number? "))
#     num2 = int(input("Second number? "))
    
#     if output == '+':
#         print(num1 + num2)
#     elif output == '-':
#         print(num1 - num2)
#     elif output == '*':
#         print(num1 * num2)
#     elif output == '/':
#         print(num1 / num2)
#     else:
#         print("Invalid operator")
        
while True:
    choice = input("enter 'p' to play or 'q' to quit:")
    if choice == 'q':
        break
    if choice not in ['p','q']:
        print("invalid input")
        continue
    choice = ['rock','paper','scissors']
    user1 = input("user1 choice?")
    user2 = input("user2 choice?") 
    if user1 not in choice or user2 not in choice:
        print("invalid input")
        continue
    if user1 == user2:
        print("it's a tie")
    elif user1 == 'rock' and user2 == 'scissors':
        print("user1 wins")
    elif user1 == 'scissors' and user2 == 'paper':
        print("user1 wins")
    elif user1 == 'paper' and  user2 == 'rock':
        print("user1 wins")
    else:
        print("user2 wins")
        
