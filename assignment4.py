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
Word = input("Enter the first word: ")

# Taking input of meaningful word with the exact same letters
Test_Word = input("\n Enter a new meaningful word to test your friendship: ")

# defining dictionary
def count_in_dict(Word):
    count = {}
    list1 = list(Word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# Test to verify the letters of the new word
if count_in_dict(Word) != count_in_dict(Test_Word):
    print("The letters aren't exact, friendship is fake!!")
else :
#shopkeeper's input to verify the word's meaning
    def userinput():
        ans = input("Does the word makes sense?(y or n)\n")

        if ans == 'y':
            print("The friends pass the friendship test!!\n\n")
        elif ans == 'n':
            print("The word doesn't have a meaning, friendship is fake!!\n\n")
        else:
            print("Invalid input, try again")
            userinput()
    userinput()
print("\n")

print ("Thank You")
