# Assignment - Looping

#1
print("1. Write a python program that takes in a range of values from 0 to 10 and prints all the values")
for i in range(0,11):
    print(i, end=" ")

#2
print("\n\n2. Write a python program that takes in a range of values from 0 to 10 and prints all even values")
for i in range(2,11,2):
    print(i, end=" ")
print("\nOR")
for i in range (1,11):
    if i%2==0:
        print(i, end=" ")

#3
print("\n\n3. Write a python program that takes in a range of values from 0 to 10 and prints all odd values")
for i in range (1,11):
    if i%2!=0:
        print(i, end=" ")

#4
print("\n\n4. Write a python program that takes in an alphanumeric variable and prints only the digits in it")
#    Hint:
#          Use 'isdigit()' in the condition part of the IF STATEMENT
#      Input:
#          a = 'ais1324'
#      Expected Output:
#          1324
inp = 'ais1324'
for i in inp:
    if i.isdigit():
        print(i, end="")


#5
print("\n\n5. Write a python program that takes in an alphanumeric variable and prints only the alphabets in it")
#      Hint:
#          Use 'isalpha()' in the condition part of the IF STATEMENT
#      Input:
#          a = 'ais1324'0
#      Expected Output:
#          ais
inp = 'ais1324'
for i in inp:
    if i.isalpha():
        print(i, end="")

# 6. a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']
# Using the above list, check if the length of each word is > 2 and the first character and last character are the same
# If the above two conditions are satisfied, then print that word, else print the first character of the word.
print("\n\n6. a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']")
a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        print(i, end=" ")
        print()
    else:
        print(i[0], end=" ")

#7
print("\n\n7. Write a python program to calculate the length of values present in a list. Should not use "
      "len() function")
test_list = [1, 4, 5, 7, 8]
print("The list is : " + str(test_list))
count = 0
for i in test_list:
    count = count + 1
print("Length of list using naive method is : " + str(count))

#8
print("\n\n8. Write a python program to get the minimum value from a list. Should not use min() function")
list1 = [10, 20, 4, 45, 99]
print("The list is :",list1)
list1.sort()
print("Smallest element is:", list1[0])

#9
print("\n\n9. Write a python program to get the maximum value from a list. Should not use max() function")
list1 = [10, 98, 4, 80, 52]
print("The list is :",list1)
list1.sort()
print("Largest element is:", list1[-1])

#10
print("\n\n10. a = [1,2,3,[4,5,6],'hello',{'a':1,'b':2}]. Add all the values")
# 1+2+3+4+5+6+1+2
# Expected output: 24
a = [1,2,3,[4,5,6],'hello',{'a':1,'b':2}]
x = 0
y = 0
z = 0
for i in a:
    if type(i)==dict:
        v = i.values()
        for m in v:
            y = y+m
    if type(i)==list:
        for n in i:
            x = x+n
    if type(i)==int:
        z = z+i
print("The sum is :",x+y+z)

#11
print("\n\n11. To sort the list containing number and alphabet")
lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
s = sorted(lst, key=str)
print(s)

