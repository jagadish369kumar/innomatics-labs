#!/usr/bin/env python
# coding: utf-8

# In[1]:


# easy from 17 to 33

#17 Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.


chords = ["abc7", "Ab7", "D7", "G", "F#m7"]

for i in range(len(chords)):
    if not chords[i].endswith("7"):
        chords[i] += "7"

print(chords)


# In[54]:


#18 Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".


moods = ["happy", "sad", "excited", "angry", "relaxed"]

for mood in moods:
    if mood == "":
        print("Today, I am feeling neutral")
    else:
        print(f"Today, I am feeling {mood}")


# In[2]:


#19 Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

decimal_str = "180"

# Convert the decimal string to an integer
decimal_num = int(decimal_str)
binary_str = ""

# Initialize a list of binary values for each bit
binary_values = [256, 128, 64, 32, 16, 8, 4, 2, 1]

for value in binary_values:
    if decimal_num >= value:
        binary_str += "1"
        decimal_num -= value
    else:
        binary_str += "0"

print(binary_str)


# In[63]:


#20 Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

# Input: radius 'r' (in cm) and height 'h' (in cm)
radius = 5.0  # You can change the radius as needed
height = 10.0  # You can change the height as needed

# Define the density of water in kg/cm^3
water_density = 1.0  # 1 kg/cm^3

# Calculate the volume of the cylinder in cm^3
cylinder_volume = 3.141592653589793 * (radius**2) * height

# Convert the volume to liters (1 dm^3 = 1 liter)
cylinder_volume_liters = cylinder_volume / 1000.0

# Calculate the mass of water in kg
mass_of_water_kg = cylinder_volume_liters * water_density

# Round the mass to two decimal places
rounded_mass = round(mass_of_water_kg, 2)

print(f"The mass of the water-filled cylinder is: {rounded_mass} kg")


# In[12]:


#21 Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.


from datetime import date

# Create a Date object
given_date = date(2023, 12, 24)  # You can change the year as needed

# Check if it's Christmas Eve
is_christmas_eve = False

if given_date.month == 12 and given_date.day == 24:
    is_christmas_eve = True

if is_christmas_eve:
    print("It's Christmas Eve!")
else:
    print("It's not Christmas Eve.")


# In[13]:


#22 Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

# Input: Three integers a, b, and c
a, b, c = 3, 4, 5  # You can change the values as needed

# Create a list of the three integers
numbers = [a, b, c]

# Sort the list in ascending order
numbers.sort()

# Check if it's a Pythagorean triplet
is_pythagorean = False

if numbers[0] ** 2 + numbers[1] ** 2 == numbers[2] ** 2:
    is_pythagorean = True

if is_pythagorean:
    print("It's a Pythagorean triplet!")
else:
    print("It's not a Pythagorean triplet.")


# In[3]:


#23 Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.


# Input: an integer
num = 14  # You can change the integer as needed

# Convert the integer to its binary representation
binary_str = bin(num)[2:]  # [2:] to remove the '0b' prefix

# Initialize a count for the number of ones
count_ones = 0

# Iterate through the binary string
for digit in binary_str:
    if digit == '1':
        count_ones += 1

# Print the count of ones
print(f"Number of ones in the binary representation: {count_ones}")


# In[4]:


#24 Create a function that takes a string and returns the number (count) of vowels contained within it.

# Input: a string
input_string = "Hello, Vijay!"  # You can change the string as needed

# Convert the string to lowercase to simplify vowel checking
input_string = input_string.lower()

# Initialize a count for the number of vowels
count_vowels = 0

# Define a set of vowel characters
vowels = {'a', 'e', 'i', 'o', 'u'}

# Iterate through the string
for char in input_string:
    if char in vowels:
        count_vowels += 1

# Print the count of vowels
print(f"Number of vowels in the string: {count_vowels}")


# In[5]:


#25 Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.


# Input: a single character
char = 'B'  # You can change the character as needed

# Check if the character is uppercase
if 'B' <= char <= 'Z':
    counterpart_char = chr(ord(char) + 32)
    print(f"Character code of lowercased counterpart: {ord(counterpart_char)}")
elif 'a' <= char <= 'z':
    counterpart_char = chr(ord(char) - 32)
    print(f"Character code of uppercased counterpart: {ord(counterpart_char)}")
else:
    print("Invalid character. Please provide an alphabetic character.")


# In[17]:


#26 Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

# Input: a, b, and c
a = 1
b = 10
c = 3

# Initialize a variable to store the sum
sum_divisible_by_c = 0

# Use a for loop to iterate through the range [a, b]
for number in range(a, b + 1):
    if number % c == 0:
        sum_divisible_by_c += number

# Print the sum of numbers divisible by c
print(f"The sum of numbers divisible by {c} in the range [{a}, {b}] is: {sum_divisible_by_c}")


# In[6]:


#27 Mubashir was walking through a straight street with exactly n identical houses on both sides. House numbers in the street look like this:


# Input: house number 'house' and length of the street 'n'
house = 4
n = 8

# Calculate the house number on the opposite side
opposite_house = 0

if house % 2 == 0:
    opposite_house = n - (house // 2) + 1
else:
    opposite_house = (house // 2) + 1

# Print the house number on the opposite side
print(f"The house number on the opposite side of house {house} is: {opposite_house}")


# In[7]:


#28 Create a function that returns True if a given inequality expression is correct and False otherwise.

# Input: an inequality expression as a string
inequality_expression = "6 < 10"  # You can change the expression as needed

# Split the inequality expression into its components
components = inequality_expression.split()

# Check if the inequality expression is correct
is_correct = False

if len(components) == 3:
    left_operand = float(components[0])
    operator = components[1]
    right_operand = float(components[2])

    if operator == "<" and left_operand < right_operand:
        is_correct = True
    elif operator == ">" and left_operand > right_operand:
        is_correct = True
    elif operator == "<=" and left_operand <= right_operand:
        is_correct = True
    elif operator == ">=" and left_operand >= right_operand:
        is_correct = True
    elif operator == "==" and left_operand == right_operand:
        is_correct = True
    elif operator == "!=" and left_operand != right_operand:
        is_correct = True
        
        # Print the result
print(f"The inequality expression is correct: {is_correct}")


# In[8]:


#29 Create a function that replaces all the vowels in a string with a specified character.

# Input: a string and the character to replace vowels with
input_string = "Hello, Vijay!"  # You can change the string as needed
replacement_char = '*'  # You can change the replacement character as needed

# Initialize an empty string for the result
result_string = ""

# Define a set of vowel characters
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Iterate through the input string
for char in input_string:
    if char in vowels:
        result_string += replacement_char
    else:
        result_string += char

# Print the result string with vowels replaced
print(result_string)


# In[9]:


#30 Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

# Input: a credit card number as a string
credit_card_number = "1234 5678 9876 8888"  # You can change the credit card number as needed

# Initialize an empty string for the result
result_card_number = ""

# Calculate the number of asterisks needed
num_asterisks = len(credit_card_number) - 4

# Use a for loop to create the masked card number
for i in range(num_asterisks):
    result_card_number += "*"

# Add the last four characters to the result
result_card_number += credit_card_number[-4:]

# Print the result
print(result_card_number)


# In[28]:


#31 Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.


# Input: a string
input_string = "xoxoxoxo"  # You can change the string as needed

# Initialize counts for "x" and "o"
count_x = 0
count_o = 0

# Iterate through the characters in the string
for char in input_string:
    if char.lower() == 'x':
        count_x += 1
    elif char.lower() == 'o':
        count_o += 1

# Check if the counts of "x" and "o" are the same
if count_x == count_o:
    print(True)
else:
    print(False)


# In[10]:


#32 Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

# Input: a string containing a person's first and last name
full_name = "The Vijay"  # You can change the full name as needed

# Split the full name into words
name_parts = full_name.split()

# Check if there are at least two words (first name and last name)
if len(name_parts) >= 2:
    # Swap the first and last name
    swapped_name = name_parts[-1] + " " + name_parts[0]

    print(swapped_name)
else:
    # Handle the case when there are not enough words
    print("Invalid input. Please provide both a first and last name.")


# In[11]:


#33 Create a function that takes a list and finds the integer which appears an odd number of times.

# Input: a list of integers
numbers = [1, 2, 3, 2, 1, 3, 4, 4, 5, 5, 7]  # You can change the list as needed

# Initialize a dictionary to count the occurrences of each integer
count_dict = {}

# Use a for loop to count the occurrences of each integer
for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# Find the integer that appears an odd number of times
odd_occurrence = None
for number, count in count_dict.items():
    if count % 2 == 1:
        odd_occurrence = number
        break

if odd_occurrence is not None:
    print(f"The integer that appears an odd number of times is: {odd_occurrence}")
else:
    print("No integer appears an odd number of times in the list.")


# In[12]:


#9 Write a function that takes a list of numbers and returns a list with two elements:

#The first element should be the sum of all even numbers in the list.
#The second element should be the sum of all odd numbers in the list.

# Input: a list of numbers
numbers = [1, 4, 3, 4, 5, 6]  # You can change the list as needed

# Initialize variables to store the sums of even and odd numbers
sum_even = 0
sum_odd = 0

# Use a for loop to calculate the sums
for number in numbers:
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

# Create a list with the two sums
sums_list = [sum_even, sum_odd]

print(sums_list)


# In[13]:


#10 In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

# Input: the number of balls bowled by a bowler
balls_bowled = 24  # You can change the number of balls as needed

# Initialize variables for overs and remaining balls
overs = 3
remaining_balls = balls_bowled

# Use a for loop to calculate the overs and remaining balls
for _ in range(balls_bowled):
    if remaining_balls >= 6:
        overs += 1
        remaining_balls -= 6

# Create a float value in the format overs.balls
overs_and_balls = float(f"{overs}.{remaining_balls}")

print(overs_and_balls)


# In[42]:


#11 Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?! Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:

# Input: a dictionary of stolen items and a lowercase string representing the pet's name
stolen_items = {
    "jewelry": 5000,
    "electronics": 2000,
    "cash": 1000
}

pet_name = "rambo"  # You can change the pet's name as needed

# Convert the pet's name to title case
pet_name_title = pet_name.capitalize()

# Check if the pet's name is in the stolen items
is_pet_stolen = False
for item in stolen_items:
    if item == pet_name_title:
        is_pet_stolen = True
        break

# Return an appropriate message
if is_pet_stolen:
    print(f"{pet_name_title} is gone...")
else:
    print(f"{pet_name_title} is here!")
    


# In[47]:


#12 Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.Scale Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.


# Input: an integer (radius of the circle)
radius = 5  # You can change the radius as needed

# Calculate the side length of the smaller square (using the radius as the diagonal)
side_length_small_square = (2 * radius) / (2 ** 0.5)

# Calculate the side length of the bigger square (using the radius as the inradius)
side_length_big_square = 2 * radius

# Calculate the areas of the two squares
area_small_square = side_length_small_square ** 2
area_big_square = side_length_big_square ** 2

# Calculate the difference in areas
area_difference = area_big_square - area_small_square

print(area_difference)


# In[48]:


#13 Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

# Input: a list of dictionaries with names and notes
people = [
    {"name": "John", "notes": [3, 5, 4]},
    {"name": "Alice", "notes": [4, 6, 8]},
    {"name": "Bob", "notes": [7, 5, 6]}
]

# Initialize a list to store the new dictionaries
new_people = []

# Iterate through the list of dictionaries
for person in people:
    name = person["name"]
    notes = person["notes"]
    
    # Find the top note (maximum note)
    top_note = max(notes)
    
    # Create a new dictionary with the name and top_note
    new_person = {"name": name, "top_note": top_note}
    
    # Append the new dictionary to the list
    new_people.append(new_person)

print(new_people)


# In[50]:


#14 You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar.

# Input: a dictionary containing cost price, sell price, and starting inventory
product_info = {
    "cost_price": 10,  # cost price per unit in dollars
    "sell_price": 20,  # sell price per unit in dollars
    "inventory": 100  # starting inventory
}

# Calculate the profit per unit
profit_per_unit = product_info["sell_price"] - product_info["cost_price"]

# Calculate the total profit
total_profit = profit_per_unit * product_info["inventory"]

# Round the total profit to the nearest dollar
rounded_total_profit = round(total_profit)

print(rounded_total_profit)


# In[51]:


#15 Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

# Input: a country's name and its area in square kilometers
country_name = "United States"  # You can change the country name as needed
country_area = 9826675  # You can change the country's area as needed

# Define the total world's landmass in square kilometers (for example)
total_world_landmass = 148940000  # You can change this value to a more accurate estimate

# Calculate the country's proportion of the total world's landmass
proportion = (country_area / total_world_landmass) * 100

print(f"The proportion of {country_name}'s area to the total world's landmass is: {proportion:.2f}%")


# In[14]:


#16 You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.


# Input: two numbers 'a' and 'b'
a = 13  # You can change the value of 'a' as needed
b = 3   # You can change the value of 'b' as needed

# Use a for loop to find the next number
for num in range(a + 1, a + b + 1):
    if num % b == 0:
        next_number = num
        break

print(next_number)

