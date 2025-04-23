# multifly program using for loop def fucntion
def muptiply(a,b):
    result = 0
    for i in range(b):
        result += a

    print(result)
muptiply(int(input("msg1:")),int(input("msg2:")))

# multifly program using recursion

def mul(a,b):
    if b==1:
        return a
    else:
        return a + mul(a,b-1)
print(mul(3,4))

 #-----------------------------------------------------------------------------------------------------   
print("\nWAP to find the sum of all integers in given list using recursion")
def sum_of_integers(lst):
    if not lst:
        return 0
    if isinstance(lst[0], int):
        return lst[0] + sum_of_integers(lst[1:])
    return sum_of_integers(lst[1:])
# -------------------------------------------------------------------------------------------------------
l = [1, 2, 3, 4, 5]
print("Sum of integers in list:", sum_of_integers(l))

print('''\nWAP to print following:
      l = ['hey', 76, True, 56, 'data', 'nice', False]
      output : ['yehhey', 76, True, 56, 'ataddate', 'ecinnice', False]''')
def modify_list(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            lst[i] = ''.join([char for char in lst[i][::-1]])
        elif isinstance(lst[i], bool):
            lst[i] = not lst[i]
    return lst
print(modify_list(['hey', 76, True, 56, 'data', 'nice', False])) # ['yehhey', 76, False, 56, 'ataddate', 'ecinnice', True]
# ----------------------------------------------------------------------------------------------------
print("\nWAP to reseverse the given string without using slicing")




print("\nWAP to chech whether the data is palindrome or not")

def palindrome(name):
    if len(name) == 0 or len(name) == 1:
        return " Its palindrom"
    if  name ([0]) != name ([-1]):
        return " Not palindrom"
    return palindrome(name([0]) == name([-1]))

        



print("\nWAP to find the lenght of given list without using inbuilt function")
print("\nWAP to find the maximum counted number in the list")
# ----------------------------------------------------------------------------------------------

print("\nWAP to reverse the given string without using slicing (Using Recursion)")
def reveres(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reveres(string[:-1])
print(reveres(input("Enter a string: "))) # Reverse of the string
# ----------------------------------------------------------------------------------------------
print("\nWAP to chech whether the data is palindrome or not")
def check_palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return "Given string is palindrome"
    if str[0] != str[-1]:
        return "Given string is not palindrome"
    return check_palindrome(str[1:-1])
print(check_palindrome(input("Enter a string: "))) # True or False
# ----------------------------------------------------------------------------------------------

print("\nWAP to find the lenght of given list without using inbuilt function")
def find_length(lst):
    if not lst:
        return 0
    return 1 + find_length(lst[1:])
print("Length of the list:", find_length([1, 2, 3, 4, 5])) # 5
# ----------------------------------------------------------------------------------------------

print("\nWAP to find the maximum counted number in the list (Using Recursion)")

def find_max_count(lst, max_count=0, max_num=None):
    if not lst:
        return max_num, max_count
    
    current_num = lst[0]
    count = lst.count(current_num)
    
    if count > max_count:
        max_count = count
        max_num = current_num
    
    return find_max_count(lst[1:], max_count, max_num)

l = [1,2,4,1,2,7,3,2,3,2,6,7,4,1]
print("Maximum counted number in the list:", find_max_count(l)[0], "Max count :", find_max_count(l)[1]) # (2, 4)
# ----------------------------------------------------------------------------------------------
