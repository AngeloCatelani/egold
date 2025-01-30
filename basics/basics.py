# Exercise 1: Calculate the multiplication and sum of two numbers
# def multiplication(n1,n2):
#     product = n1*n2
#     sum = n1+n2
#     if product <= 1000:
#         return product
#     else:
#         return sum


# Exercise 2: Print the sum of the current number and the previous number
# def sum(num):
#     sum = 0
#     for i in range(0,10):
#         sum +=i

#     print(sum)

# Exercise 3: Print characters from a string that are present at an even index number
# def even(str):
#     for i in range(len(str)):
#         if i%2==0:
#             print(str[i])

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# def remove(str,n):
#     newStr = ""
#     for i in range(n,len(str)):
#         newStr +=str[i]
#     return newStr
# print(remove("pynative",4))

# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def check(list):
    if list[0] == list[-1]:
        return True
    return False



print(check([75, 65, 35, 75, 30]))