#!/usr/bin/env python3

import random

wordbank = ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

num = input("""Pick a number between 0 and 18.
                Or type 'random'.
                Or type a student's name: """)

if num == 'random':
    num = random.randint(0, 18)
    student2 = tlgstudents[num]
elif num in tlgstudents:
    student2 = num
else:
    num = int(num)
    student2 = tlgstudents[num]

student_name = tlgstudents[slice(0, 1)][0]

print(f"{student_name} always uses {str(wordbank[2])} {wordbank[1]} to indent.")

print(f"{student2} always uses {str(wordbank[2])} {wordbank[1]} to indent too.")
