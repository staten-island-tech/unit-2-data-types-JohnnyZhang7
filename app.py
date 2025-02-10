""" # Strings represent characters. names. words
name = "a"
#integers for WHOLE numbers
age = 14
#BooLean is True or False, typically used for evaluations
graduated = False
#Floats for decimal
money = 4.50
#Lists can be a collection of multiple data types in a single variable
list = [1, 2, 3] """

""" def add(x,y):
    print(round(x + y))
add(54,+ "11") """
#example of not good problem

#input seeks user response and outputs that into the variable
#Bill value will be equal to the response of the user
#input result is a string

""" bill = float(input("How much was the bill?"))
add(15, bill) """
#Lists which store lists of data
""" students = ["u", "me", "that", "them", "gaf", "gar"] """
#similar to for i in range(4)
#scalable, don't have to change the range all the time
""" for student in students:
    print(student) """

#adding the latter to the former
""" moneys = [1,2,3,4,5,6]
for student in students:
    print(student)
x=0 """
""" for money in moneys:
    x = x + money
    print(x) """



""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6])  """   #prints the first(1) and sixth number(15)

""" "test"
["t","e","s","t"] """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" word = string = "a b c d e"
words = string.split()         #splits the string and returns how many words
word_count = len(words)     #counts the number of elements in the list
print(word)
print(word_count) """

""" #MADLIB PROJECT
name = "Jonathan"
emotion = "excited"
verb = "jumping"
print(f"Today is {name} birthday and he is super {emotion}, {verb} around everywhere.")
number = "7"
celebrityname = "George Washington"
print(f"There was {number} presents on his desk and his favorite celebrity, {celebrityname} was there!")
emotion2 = "excitement"
verb2 = "ran"
emotion3 = "joy"
print(f"Overwhelmed by the {emotion2}, he {verb2} out of the house in {emotion3}") """

""" day_of_week = input("what day is it? ")     #Only has two answers which vary based on your answer
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")
temp = 68               #code creates conditions and if their met will give you said response
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#EVEN ODD CHALLENGE
#use modeulo to check remainder for 1 factor
#use a loop to check all potential factors range(2,15)
#conditional statement if factor append to list
#print the list
""" def evenodd(number):
    if number % 2 ==0:
        return "even"
    else:
        return "odd"
number = [2, 5, 6, 7]
for num in number:
    print(f"{num} is {evenodd(num)}") """   #I searched this up, it loops through using a f string to define each one

#BILL AND TIP CHALLENGE
def total(bill, tip):
    return bill + (bill * tip)

bill = 15
service = "bad, okay, good, great"



#LESSON
""" def login(password):
    #If statement evaluates as true, run next line
    if(password) == "secret":
        print("logged in")
    else:
        print("incorrect password")
login("secret") """
