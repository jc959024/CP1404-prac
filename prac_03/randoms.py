"""
What did you see on line 1?
This line generates a random integer between 5 and 20, inclusive.
What was the smallest number you could have seen, what was the largest?
Smallest number: 5
Largest number: 20
What did you see on line 2?
This line generates a random number starting from 3 to the range up to 10 with a step of 2.
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Smallest number: 3
Largest number: 9
No, because the step size is 2, so the possible numbers are 3, 5, 7, 9. Therefore, line 2 does not produce a 4.
What did you see on line 3?
This line generates a random floating point number between 2.5 and 5.5.
What was the smallest number you could have seen, what was the largest?
Smallest number: 2.5
Largest number: 5.5
"""
import random
print(random.randint(1, 100))