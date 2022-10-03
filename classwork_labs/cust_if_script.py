#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your grade is:  '

# wrap connection in a float() to accept decimals as numbers
exam_score = float(input("What score did you get on the exam?(0-100): "))

# if input value was higher or equal to 25
if exam_score >= 90:
    message = message + 'A'
elif exam_score >= 80 and exam_score < 90:
    message = message + 'B'
elif exam_score >= 70 and exam_score < 80:
    message = message + 'C'
elif exam_score >=60 and exam_score < 70:
    message = message + 'D'
elif exam_score < 60:
    message = message + 'F'
print(message)

