#!/usr/bin/env python
# coding: utf-8

# In[1]:


# easy 17 to 33

#17 Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.

chords = ["A", "G7", "Am", "F7", "Dm7", "E7"]

i = 0
while i < len(chords):
    if not chords[i].endswith("7"):
        chords[i] += "7"
    i += 1

print(chords)


# In[2]:


#18 Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

mood = None
while mood is None:
    mood = input("Enter your current mood: ")
    if mood.strip() == "":
        print("Today, I am feeling awesome")
        mood = "neutral"
    else:
        print(f"Today, I am feeling {mood}")


# In[3]:


#19 Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

decimal_str = input("Enter a decimal number: ")
decimal = int(decimal_str)

binary_str = ""

while decimal > 1:
    binary_str = str(decimal % 2) + binary_str
    decimal = decimal // 2

print(f"Binary representation: {binary_str}")


# In[10]:


#20 Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

How to solve:

Calculate the volume of the cylinder.
Convert cm³ into dm³.
1dm³ = 1L, 1L is 1Kg.

# Input radius (r) and height (h) in cm
r = float(input("Enter the radius (in cm): "))
h = float(input("Enter the height (in cm): "))

# Calculate the volume of the cylinder in cm³
volume_cm3 = 3.14159265 * r**2 * h

# Initialize a variable to convert cm³ to dm³
conversion_factor = 1000  # 1 dm³ = 1000 cm³

# Convert the volume to dm³
volume_dm3 = volume_cm3 / conversion_factor

# The mass in kg is equal to the volume in dm³
mass_kg = volume_dm3

# Round the result to two decimal places
mass_kg = round(mass_kg, 2)

print(f"The mass of the water-filled cylinder is {mass_kg} kg.")


# In[ ]:


#21 Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.

from datetime import datetime

date_str = input("Enter a date in the format (YYYY-MM-DD): ")
date = datetime.strptime(date_str, "%Y-%m-%d")

# Check if it's Christmas Eve (December 24th)
is_christmas_eve = False
while date.month == 12:
    if date.day == 24:
        is_christmas_eve = True
    break

print(is_christmas_eve)


# In[1]:


#22 Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Arrange the integers in ascending order
while a > b or b > c:
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

# Check if it's a Pythagorean triplet
is_pythagorean = (a**2 + b**2 == c**2)

print(is_pythagorean)


# In[1]:


#23 Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.

number = int(input("Enter an integer: "))
count = 0

while number > 0:
    if number % 2 == 1:
        count += 1
    number //= 2

print(f"The number of ones in the binary representation is: {count}")


# In[2]:


#24 Create a function that takes a string and returns the number (count) of vowels contained within it.

text = input("Enter a string: ")
count = 0
vowels = "AEIOUaeiou"

i = 0
while i < len(text):
    if text[i] in vowels:
        count += 1
    i += 1

print(f"The number of vowels in the string is: {count}")


# In[4]:


#25 Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

char = input("Enter a single character: ")

if len(char) == 1:
    if char.isalpha():
        # Check if it's an uppercase character
        is_upper = char.isupper()

        # Convert to the opposite case
        if is_upper:
            opposite_char = char.lower()
        else:
            opposite_char = char.upper()

        # Get the character code of the opposite character
        char_code = ord(opposite_char)

        print(f"The character code of the {'' if is_upper else 'lowercased / uppercased '}counterpart is: {char_code}")
    else:
        print("Please enter a valid alphabetic character.")
else:
    print("Please enter a single character.")
    


# In[6]:


#26 Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

a = int(input("Enter the lower bound (a): "))
b = int(input("Enter the upper bound (b): "))
c = int(input("Enter the divisor (c): "))

sum_divisible_by_c = 0
number = a

while number <= b:
    if number % c == 0:
        sum_divisible_by_c += number
    number += 1

print(f"The sum of numbers evenly divisible by {c} in the range from {a} to {b} is: {sum_divisible_by_c}")


# In[9]:


#27 Mubashir was walking through a straight street with exactly n identical houses on both sides. House numbers in the street look like this:

#1 |   | 6

#3 |   | 4

#5 |   | 2
#He noticed that Even numbered houses increase on the right while Odd numbered houses decrease on the left.Create a function that takes a house number house and length of the street n and returns the house number on the opposite side.

# Input house number and length of the street
house = int(input("Enter the house number: "))
n = int(input("Enter the length of the street (number of houses on one side): "))

# Calculate the house number on the opposite side
opposite_house = 0
if house % 2 == 0:
    # Even house number
    opposite_house = house - 1
else:
    # Odd house number
    opposite_house = n * 2 - house + 1

print(f"The house number on the opposite side is: {opposite_house}")


# In[11]:


#28 Create a function that returns True if a given inequality expression is correct and False otherwise.


expression = input("Enter an inequality expression: ")

# Find and split the expression into its parts
while '<=' in expression:
    parts = expression.split('<=')
    if len(parts) == 2:
        left = float(parts[0].strip())
        right = float(parts[1].strip())
        result = left <= right
        print(result)
        break

while '>=' in expression:
    parts = expression.split('>=')
    if len(parts) == 2:
        left = float(parts[0].strip())
        right = float(parts[1].strip())
        result = left >= right
        print(result)
        break

while '<' in expression:
    parts = expression.split('<')
    if len(parts) == 2:
        left = float(parts[0].strip())
        right = float(parts[1].strip())
        result = left < right
        print(result)
        break

while '>' in expression:
    parts = expression.split('>')
    if len(parts) == 2:
        left = float(parts[0].strip())
        right = float(parts[1].strip())
        result = left > right
        print(result)
        break

while '==' in expression:
    parts = expression.split('==')
    if len(parts) == 2:
        left = float(parts[0].strip())
        right = float(parts[1].strip())
        result = left == right
        print(result)
        break


# In[12]:


#29 Create a function that replaces all the vowels in a string with a specified character.

string = input("Enter a string: ")
replace_char = input("Enter the character to replace vowels with: ")

i = 0
while i < len(string):
    if string[i].lower() in "aeiou":
        string = string[:i] + replace_char + string[i + 1:]
    i += 1

print(f"The modified string is: {string}")


# In[13]:


#30 Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

credit_card_number = input("Enter your credit card number: ")

# Ensure the input is at least 4 characters long
while len(credit_card_number) < 4:
    print("Invalid input. Please enter a valid credit card number.")
    credit_card_number = input("Enter your credit card number: ")

# Mask all characters except the last four
i = 0
masked_credit_card = "************"  # Mask for the first 12 characters
while i < len(credit_card_number) - 4:
    i += 1

# Display the last four characters
masked_credit_card += credit_card_number[-4:]

print(f"The masked credit card number is: {masked_credit_card}")


# In[15]:


#31 Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

#Return a boolean value (True or False).
#Return True if the amount of x's and o's are the same.
#Return False if they aren't the same amount.
#The string can contain any character.
#When "x" and "o" are not in the string, return True.

string = input("Enter a string: ")

# Initialize counters for "x" and "o"
count_x = 0
count_o = 0

i = 0
while i < len(string):
    char = string[i].lower()  # Convert to lowercase for case-insensitive comparison
    if char == "x":
        count_x += 1
    elif char == "o":
        count_o += 1
    i += 1

# Check if the counts are the same or both zero
if count_x == count_o:
    result = True
else:
    result = False

print(result)


# In[16]:


#32 Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

full_name = input("Enter a person's first and last name: ")

# Initialize a variable to store the swapped name
swapped_name = ""

# Split the full name into a list of words
name_parts = full_name.split()

# Check if there are at least two words in the input
while len(name_parts) < 2:
    print("Invalid input. Please enter both the first and last names.")
    full_name = input("Enter a person's first and last name: ")
    name_parts = full_name.split()

# Swap the first and last names
if len(name_parts) >= 2:
    swapped_name = name_parts[-1] + " " + name_parts[0]

print(f"The swapped name is: {swapped_name}")


# In[17]:


#33 Create a function that takes a list and finds the integer which appears an odd number of times.

numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5]

while len(numbers) > 0:
    current_num = numbers.pop()
    if numbers.count(current_num) % 2 == 0:
        continue
    else:
        odd_occurrence = current_num
        break

print(f"The integer with an odd number of occurrences is: {odd_occurrence}")


# In[19]:


# 9 to  Medium

#9 Write a function that takes a list of numbers and returns a list with two elements:

#The first element should be the sum of all even numbers in the list.
#The second element should be the sum of all odd numbers in the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_sum = 0
odd_sum = 0

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_sum += numbers[i]
    else:
        odd_sum += numbers[i]
    i += 1

result = [even_sum, odd_sum]
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Result:", result)


# In[20]:


#10 In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

balls_bowled = int(input("Enter the number of balls bowled: "))

overs = balls_bowled // 6
remaining_balls = balls_bowled % 6

overs_and_balls = f"{overs}.{remaining_balls}"

print(f"Overs and balls bowled: {overs_and_balls}")


# In[2]:


#11 Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:

#"Rambo is gone..." if the name is on the list.
#"Rambo is here!" if the name is not on the list.

stolen_items = {
    "jewelry": 5000,
    "laptop": 1500,
    "watch": 800,
    "rambo": 1  # Assume "rambo" is the name of the pet
}

pet_name = input("Enter the name of the pet: ")

is_pet_stolen = False

while pet_name in stolen_items:
    is_pet_stolen = True
    break

if is_pet_stolen:
    print(f"{pet_name.capitalize()} is gone...")
else:
    print(f"{pet_name.capitalize()} is here!")


# In[3]:


#12 Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

#Scale Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.


radius = int(input("Enter the radius of the circle: "))

# Calculate the difference between the areas of the two squares
difference = (2 * radius) ** 2 - (radius ** 2)

print(f"The difference between the areas of the two squares is: {difference}")


# In[4]:


#13 Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

data = [
    {"name": "John", "notes": [3, 5, 4]},
    {"name": "Alice", "notes": [4, 7, 6]},
    {"name": "Bob", "notes": [5, 8, 9]},
]

def transform_notes(data):
    result = []
    i = 0
    while i < len(data):
        student = data[i]
        max_note = max(student["notes"])
        result.append({"name": student["name"], "top_note": max_note})
        i += 1
    return result

transformed_data = transform_notes(data)
print(transformed_data)


# In[5]:


#14 You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar.


product_data = {
    "cost_price": 10.5,
    "sell_price": 15.0,
    "inventory": 1000
}

# Calculate the total profit
total_profit = 0
i = 0

while i < product_data["inventory"]:
    total_profit += (product_data["sell_price"] - product_data["cost_price"])
    i += 1

# Round the total profit to the nearest dollar
rounded_total_profit = round(total_profit)

print("Total Profit:", rounded_total_profit)


# In[22]:


#15 Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

#The total world's landmass is 148,940,000 [Km^2]
#Round the result to two decimal places.

# Total world's landmass
world_landmass = 148940000  # in square kilometers

# Input country's name and area
country_name = input("Enter the country's name: ")
country_area = float(input("Enter the country's area (in square kilometers): "))

# Calculate the proportion
proportion = (country_area / world_landmass) * 100  # Calculate the percentage

# Round the result to two decimal places
rounded_proportion = round(proportion, 2)

# Display the result
print(f"The proportion of {country_name}'s area to the total world's landmass is {rounded_proportion}%.")


# In[16]:


#16 You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

while True:
    a += 1
    if a % b == 0:
        break

print(f"The next number greater than {a-1} and divisible by {b} is {a}")

