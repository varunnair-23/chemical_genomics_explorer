#define variables
number = 8
threshold = 10
word = "Python"

#condtional statements: if number is greater than threshold, print a message stating that, and print I am learning Python 5 times. If equal or less than threshold, print a message stating that.
if number > threshold: 
    print(f"{number} is greater than {threshold}")
    for i in range(5):
        print(f"{i + 1}: I am learning {word}")

elif number == threshold:
    print(f"number is equal to threshold")

else:
    print(f"{number} is less than {threshold}")