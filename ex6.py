# assign 10(intiger) to types of people 
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people"
# assign binary and do_not to an f-string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
# a good way to troubleshoot if something is wrong. 
print(">>>> printing y to see what is wrong",y)

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")


# prints a difinitive value inside a string 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation,format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
