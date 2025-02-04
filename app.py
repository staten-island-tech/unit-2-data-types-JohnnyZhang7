# Strings represent characters. names. words
name = "a"
#integers for WHOLE numbers
age = 14
#BooLean is True or False, typically used for evaluations
graduated = False
#Floats for decimal
money = 4.50

def add(x,y):
    print(round(x + y))
""" add(54, "11") """
#example of not good problem

#input seeks user response and outputs that into the variable
#Bill value will be equal to the response of the user
#input result is a string
""" bill = float(input("How much was the bill?"))
add(15, bill) """

#Lists which store lists of data
students = ["u", "me", "that", "them", "gaf", "gar"]
#similar to for i in range(4)
#scalable, don't have to change the range all the time
for student in students:
    print(student)

#adding the latter to the former
moneys = [1,2,3,4,5,6]
for student in students:
    print(student)
x=0
for money in moneys:
    x = x + money
    print(x)