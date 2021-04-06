#!/usr/bin/env python3

grade = int(input("What was your score on the test?"))
message = 'congratulations '

# wrap connection in a float() to accept decimals as numbers

# if input value was higher or equal to 25
if grade >= 95:
    message = message + "you're a genius "
elif grade >= 85:
    message = message + "great job"
elif grade >= 75:
    message = message + "you passed"
else:
    message = message + "see me after class"
print(message)

