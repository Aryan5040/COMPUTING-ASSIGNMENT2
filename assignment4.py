# Assignment 4 Introduction to Computing
# Question 1 Program for problem of Hanoi with three disks
print ("Question Number 1 \n")
print("")
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

# calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print("\n")

# Question 2 Program for printing Pascal's Triangle for n Number of rows
print ("Question Number 2 \n")
# Taking rows as input
n = int(input("Enter the number of rows in Pascal's Triangle: "))

# Using Recursions
print("\n Triangle using recursions :\n")
def pascal(n, originaln = n):
    if n == 0:
        return
    
    pascal(n-1,originaln)
    # Printing the Spaces
    print('  '*(originaln-n), end='')
    # First Number is taken 1
    entry = 1
    for i in range(1, n+1):
        print(entry, end ='   ')
        # Using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

# Using Loops
print("\n Using loops: \n")
for line in range(1, n+1):

    # Everything Else remains same as Recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("\n")

# Question 3 Operations with Two Integers taken from input
print ("Question Number 3 \n")
First_Int = int(input("Enter the first integer: "))
Second_Int = int(input("Enter the Second integer: "))
Remainder = First_Int%Second_Int
Quotient = First_Int//Second_Int
# (a) Check whether functions are callable
print("Remainder is: ", Remainder)
print("Quotient is: ",Quotient)
# (b) Check whether all values are zero
if(Remainder!=0):
    if (Quotient!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (Quotient!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
# (c) Add values to the result and filter some values 
set1=set()
for i in range (4,7):
    f=Remainder + i
    g=Quotient + i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
# (d) Convert result into datatype
set2=frozenset(set1)
# (e) Make the set immutable 
print("Immutable set: ", frozenset(set1))
# (f) Largest value of set and Hash value
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("\n")

# Question 4 Program to create Class.
print ("Question Number 4: \n")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

# Create object
student1 = Student("Sahil Sharma", 21104019)
print("Object created")

# Printing the assigned values
print(f"The name of the Student is {student1.name} and SID is {student1.sid}.")

# Delete object
del student1
print("\n")

#Question 5 Program to Store details and Commit changes.
print ("Question Number 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

# Create Employee records
Employee_1 = Employee("Mehak", 40000)
Employee_2 = Employee("Ashok", 50000)
Employee_3 = Employee("Viren", 60000)

# (a) Update Salary of Mehak
Employee_1.salary = 70000
print(f"(a) The updated salary of the employee {Employee_1.name} is {Employee_1.salary}")

# (b) Deleting Record of Viren
print("(b) ", end='')
del Employee_3

print("\n")

#Question 6 Program to help check Meaningful Words
print ("Question Number 6 \n")
# Taking input word from the first friend
print("\n[Question 6]")
gap=" "*10
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
