'''
Name: Thomas Nguyen
Professor: Jack Ho
Class: CS77 - Computer Organization
This program converts any floating point number into the simple model.
'''

#While loop to get user input and confirms if it's a float.
while True:
    try:
        unchanged = float(input("Please enter a floating number: "))
        break
    except:
       print("You have entered an invalid input, please try again.")

#Gets the sign bit
if(unchanged<0):
    sign_bit="1"
    unchanged = str(unchanged)
    unchanged = unchanged[1:]
elif(unchanged>0):
    sign_bit="0"

#Creates a variable named zuprem and saves a str value of the unchanged variable to use the length function.
zuprem = str(unchanged)
i=0

#Gets the index of the number preceding the decimal.
while i<len(zuprem):
    while True:
        if(zuprem[i]=="."):
            numbers_before_decimal = i-1
            break
        else:
            i += 1
    break

#Gets the fractional portion of the number
fractional_part = zuprem[numbers_before_decimal+1:]
counter1 = 0
tries = 0
fractional_binary = ["."]

#Calculates the fractional portion of the floating point number in binary.
while True:
    while tries<=10:
        fractional_part = float(fractional_part)
        if fractional_part==1:
            fractional_binary.append(1)
            break
        elif fractional_part==0:
            fractional_binary.append(0)
            break
        else:
            multiplied = fractional_part*2
            if multiplied >1:
                fractional_binary.append(1)
                fractional_part = multiplied - 1
            if multiplied <1:
                fractional_binary.append(0)
                fractional_part = multiplied
            if multiplied==1:
                fractional_binary.append(1)
                break
            if multiplied==0:
                fractional_binary.append(0)
                break
        tries+=1
    break

#Gets all numbers before the decimal and saves it in a variable named hi
counter = 0
hi = ""
while counter<=numbers_before_decimal:
    hi = hi + zuprem[counter]
    counter +=1

#Converts the numbers before the decimal to binary.
float_to_binary = float(hi)
binary_code = []
while True:
    if(float_to_binary%2==1):
        binary_code.append(1)
    elif(float_to_binary%2==0):
        binary_code.append(0)
    float_to_binary//=2
    if(float_to_binary==0):
        break
binary_code.reverse()

#Saves the non-fractional portion binary into a variable
binary_code_string = ""
binary_code_counter=0
while binary_code_counter<len(binary_code):
    binary_code_string += str(binary_code[binary_code_counter])
    binary_code_counter+=1

#Gets location of decimal
decimal_location = len(binary_code_string)
#Appends to the current binary variable the fractional portion of the number
counter2 = 0
while counter2<len(fractional_binary):
    binary_code_string += str(fractional_binary[counter2])
    counter2+=1

#Gets the significand bits
significand = binary_code_string[:decimal_location] + binary_code_string[decimal_location+1:]


#Gets the exponent binary code
exponent = decimal_location-1
exponent_to_binary = exponent + 16
exponent_list = []
hello=0
while True:
    while hello<5:
        hello += 1
        if (exponent_to_binary % 2 == 1):
            exponent_list.append(1)
        elif (exponent_to_binary % 2 == 0):
            exponent_list.append(0)
        exponent_to_binary //= 2
        if (exponent_to_binary == 0):
            break
    break
exponent_list.reverse()

#Gets the exponent bits
exponent_bits = ""
ebits_counter=0
while ebits_counter<len(exponent_list):
    exponent_bits += str(exponent_list[ebits_counter])
    ebits_counter+=1

#Prints out the floating point number in the simple model.
print("In simple model, this floating point number is : " + sign_bit + exponent_bits + significand[0:8])