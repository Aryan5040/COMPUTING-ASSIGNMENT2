#Assignment 2

#Question 1
STATEMENT="Python is a case sensitive language"
print(STATEMENT,"\n")

#a
print("The length of the statement is",len(STATEMENT),"\n")

#b
print("the reverse statement- ",STATEMENT[::-1],"\n")

#c
b=STATEMENT[10:26]
print(b,"\n")

#d
print(STATEMENT.replace("a case sensitive","object oriented"),"\n")

#e
print(STATEMENT.find("a"),"\n")

#f
print(STATEMENT.replace(" ",""),"\n")


# question2

a=input("Enter your name-")
b=input("Enter your SID-")
c=input("Enter your Department name-")
d=input("Enter your CGPA-")
print("\n")

print("Hey, ",a,"here")
print("My SID is ",b)
print("I am from ",c,"and my CGPA is ",d)


#question 3

#bitwise operator
#     32 16 8 4 2 1
#a=56= 1  1 1 0 0 0
#b=10= 0  0 1 0 1 0

a=56
b=10
print("a&b is-",a&b)
print("a|b is-",a|b)
print("a^b is-",a^b)
print("a<<2-", a<<2,"\t b<<2-",b<<2)
print("a>>2-", a>>2,"\t b>>4-",b>>4,"\n")


# question 4

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

if a>b and a>c:
   print("a is the greatest number","\n")
elif b>c:
    print("b is the greatest number","\n")
else:
    print("c is the greatest number","\n")


# question5

a="My name is Aryan Singh"
if "name" in a:
    print("is name present in the line","yes","\n")
else:
    print("is name present in the line","no","\n")

# question6

a=int(input("length of first side is:"))
b=int(input("length of second side is:"))
c=int(input("length of third side is:"))

if a>b+c:
      print("no triangle is possible")
elif b>a+c:
      print("no triangle is possible")
elif c>a+b:
      print("no triangle is possible")
else:
      print(" triangle is possible")
    
