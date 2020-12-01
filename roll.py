import random
import time
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("You see me rollin")
    time.sleep(3)
    print ("Your results are - ")
    print (random.randint(min, max))
    print (random.randint(min, max))
    time.sleep(1)
    roll_again = input('Roll again? - ')