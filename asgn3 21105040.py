# Python Assignment 3 for Introduction To Computing

# Question 1 A python code for Finding the number of Occurences of Letters or Words in the entered string
print("Question Number 1 \n")
My_String = input("Enter the String :\n")

# Convert all the string to Lowercase characters
My_String = My_String.lower()
Number_Letters = len(My_String)

# Divide the string into a list taking each word as an element
My_String1 = My_String.split()
Number_Elements = len(My_String1)

# When Only one word is entered , Letters are counted.
if Number_Elements == 1:
    dict={}  
    for x in range(0,Number_Letters):
        dict.update({My_String[x]:My_String.count(My_String[x])})
    print(" Hence the repititions of letters can be given as :\n",dict ,"\n")    
# When More than word is entered, Occurence of words is counted
elif Number_Elements>=1:
    dict={}
    for i in range(0,Number_Elements):
        dict.update({My_String1[i]:My_String1.count(My_String1[i])})
    print("Hence the repititions of Words can be given as :\n",dict ,"\n")   
else :
    print("Please Make sure to enter a Statement of Word \n")

# Question 2 Python code to print the next date of input date
print("Question 2 \n")

Year =int(input("Enter year :"))
# Check if input is a leap year
if Year%4 == 0:
    Leap_Year = True
else:
    Leap_Year = False


if Year in range(1800,2025):
    Month = int(input("Enter month :"))     
    if Month in (4,6,9,11):      # Month with 30 days
        Day = int(input("Enter day: "))
        if Day in range(1,30):
            print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} \n")
            
        elif Day == 30:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} \n ")
            
        else:
            print("Error: enter correct day (1-30 for this month)\n ")
    
    elif Month in (1,3,5,7,8,10):  # Month with 31 days
        Day = int(input("Enter day: "))
        if Day in range(1,31):
            print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} \n ")
        elif Day == 31:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} \n ")
            
        else:
            print("Error: enter correct day (1-31 for this month) \n")

    elif Month == 12:  # for December
        Day=int(input("Enter day: "))
        if Day in range(1,31):
            print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} \n ")
            
        elif Day == 31:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{1}/{Year+1} \n")
            
        else:
            print("Error: enter corrent day (1-31 for this month) \n")

   
    elif Month == 2:  #for February
        if Leap_Year == True:   # If Entered Year is Leap year
            Day = int(input("Enter day: "))
            if Day in range(1,29):
                print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} \n")
                
            elif Day == 29:
                print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} \n")
                
            else:
                print("Error: enter corrent day (1-29 for this month) \n")

        elif Leap_Year == False:  # If entered year is not a Leap Year
            Day = int(input("Enter day: "))
            if Day in range(1,28):
                print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} \n ")
                
            elif Day==28:
                print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} \n")
                
            else:
                print("Error: enter corrent day (1-28 for this month)\n")
            
    else:
        print("Error: Please enter correct month (1-12) \n")

else:
    print("Error: Please enter year in range (1800-2025) \n")


# Question 3 A python code to create list of tuples
print("Question 3 \n")
Terms = int(input("Number of Terms to be entered in list :\n"))
list = [] 
for i in range(1,Terms + 1):
     Element = int(input(f'Enter the required element :\n'))
     list.append(Element)
# Make empty list and Store elements entered by User
New_List=[]   
i=0
for i in range (0,Terms):  
     New_List.append((list[i], list[i]**2))
     i=i+1

print("The required list is:\n",New_List)


# Question 4 Printing remarks forGrade points
print("Question  4 \n")
Grade = int(input("Enter your grade point: "))

if 4<=Grade<=10:
    if Grade == 10:
        Grade_Value = "A+"
        Performance = "Outstanding"

    elif Grade == 9:
        Grade_Value = "A"
        Performance = "Excellent"

    elif Grade == 8:
        Grade_Value = "B+"
        Performance = "Very Good"

    elif Grade == 7:
        Grade_Value = "B"
        Performance = "Good"

    elif Grade == 6:
        Grade_Value = "C+"
        Performance = "Average"

    elif Grade == 5:
        Grade_Value = "C"
        Performance = "Below Average"

    elif Grade == 4:
        Grade_Value = "D"
        Performance = "Poor"

    print(f"Your Grade is '{Grade_Value}' and {Performance} performance \n")

else:
    print("Error (Grade points should be in range 4-10) \n")



#Question 5 Printing a Specific Pattern
print("Question 5 \n")

MY_STRING = 'ABCDEFGHIJK'   

for i in range(0,6):
    print(' '*i,MY_STRING[0:(11-(i*2))])   # Enter an extra space and remove last two letters from string with each loop
print ("\n")


# Question 6 Storing and printing details in the dictionary
print("Question 6 Making a Dictionary \n")

dict = {}        # Make an empty list in which Name and SID is to be stored
i = "y"          # Make 1st entry as default
if i == "y" :
    while i == "y" or i == "Y":              #continouly asking name and sid and storing it in empty dictionary until user enters n
        Name = str(input("Enter name: \n"))   
        SID=int(input("Enter SID: \n"))      
        if SID<=0:
            print("SID should be positive integer \n")
            exit()
        dict.update({Name:SID})               # Store name and sid in dictionary (Name as key, SID as value)
        print(dict)
        i=input("Want to make another entry? \n Press 'Y' for YES / 'N' for NO.\n")    
        # Asking user if want to a make another entry                                 
        
        
    if i == "n" or i == "N":                 # If user enters 'N', code progresses
        
        # (a) Print Student Details
        print("(a) The Stored Student Details are : \n",dict ,"\n")  
        
        # (b) Sort using Student Names
        New_List = dict.keys()               #making a list(New_List) containing Names (dictionary's keys)
        sorted_list_1=sorted(New_List)         #Sorting list 
       
        new_dic_1={}                     #making a new dictionary sorted on  the basis of name
        for items in sorted_list_1:
            new_dic_1.update({items:dict.get(items)})

        print("(b) Dictionary sorted on the basis of names: \n",new_dic_1 , "\n")
        
        # (c) Sort Using SID
        rev_dict={}                     #making a new dict with SIDs as keys and name as values
        for key,value in dict.items():
            rev_dict.update({value:key})

        New_List1 = rev_dict.keys()          # making another list(New_List1) containing SIDs
        sorted_list_2=sorted(New_List1)      #sorting list on the basis of SIDS
        
        
        new_dic_2={}                         #making a new dictionary sorted on  the basis of SIDs
        for items in sorted_list_2:
            new_dic_2.update({rev_dict.get(items):items})

        print("(c) Dictionary sorted on the basis of SID: \n",new_dic_2 , "\n")

        # (d) Search Using SID and Print Name
        SID=int(input("(d) Enter a SID to get the Student's name :"))  # Taking SID as input to print the name assigned with it
        if SID in New_List1 :
            print("Name related to following sid is: \n",rev_dict.get(SID), "\n")
        else:
            print("ERROR: The following SID is not present in Dictionary \n")
   
    else:
        print("ERROR: Enter 'Y' or 'N' only \n" )


# Question 7 Program to print Fibonacci Series and Average of resultant of Fibonacci Series
print("Question 7 \n")

Number=int(input("How many terms are to be printed in fibonacci series?\n"))

NUM1 = 0   
NUM2 = 1

if Number<=0:
    print("Please Enter a postive number")

else:
    list=[]                     # Make an empty list
    for i in range (0,Number-1):
        if i==0:
            list.append(NUM1)    #entering '0' as first term in list
        if i==1:
            list.append(NUM2)    #entering '1' as second term in list
            continue
        sum = NUM1+ NUM2
        NUM1 = NUM2
        NUM2 = sum
        list.append(sum)        #entering the remaining terms
        sum+=sum

    print("The Required Fibonacci series is:\n",list , "\n")

    #calculating sum of all terms present in list
    sum=0
    for items in list:
        sum = sum + items
    #calculating average
    Average = sum/len(list)         #len(list)=no. of elements in list
    print("Average of following series is:\n",Average , "\n")


# Question 8 Different Commands with sets
print("Question 8\n")

Set_1={1,2,3,4,5}
Set_2={2,4,6,8}
Set_3={1,5,9,13,17}

# (a) A new set with all elements of Set_1 and Set_2 but not of Both
print("(a)",end=" ")
New_Seta = (Set_1^Set_2)      #New_Seta =(Set_1|Set_2)- (Set_1&Set_2)
print(New_Seta , "\n")

# (b) A new Set with elements that are only in one of the three sets
print("(b)",end=" ")
New_Setb =(Set_1^Set_2^Set_3)  # New_Setb=(Set_1|Set_2|Set_3)- (Set_1&Set_2)- (Set_2&Set_3)- (Set_3&Set_1)
print(New_Setb , "\n")

# (c) A new Set with elements that are exactly in Two of three sets
print("(c)",end=" ")
print((Set_1|Set_2|Set_3)-(Set_1^Set_2^Set_3)-(Set_1&Set_2&Set_3),"\n")  
    #(union of all sets)- (elements present in only one set) - (elements present in all three sets)

# (d) A new set of integers in range 1,10 that are not in Set_1
print("d)",end=" ")
Integers={1,2,3,4,5,6,7,8,9,10}
print(Integers-Set_1 , "\n")

# (e) A new set of integers in range 1,10 that are not in Set_1 ,Set_2 and Set_3
print("e)",end=" ")
print(Integers-(Set_1|Set_2|Set_3) , "\n")   # (integers) - (union of Set_1,Set_2 and Set_3)

print ("Thank You")
