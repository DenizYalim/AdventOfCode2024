with open("input", "r") as file:
    longString = file.read()
longerString = []
for i, char in enumerate(longString):
    if i % 2 != 0:
        [longerString.append(".") for j in range(int(char))]
    else:
        [longerString.append(i // 2) for j in range(int(char))]

print(longerString)

right = len(longerString) - 1

while right > 0:
    left = longerString.index('.')
    starting_left = left
    starting_right = right
    target_number = longerString[right]

    valid = True
    while left <= right:
        print("sd")

        valid = True
        while longerString[right] == target_number:
            print("sds")
            right-=1
            left+=1

            if longerString[left] != '.':
                valid = False
                break
        left += 1

        if valid: # valid, lists can change

            longerString[starting_left:left], longerString[right+1 : starting_right+1] = longerString[right+1: starting_right+1], longerString[starting_left:left]
        else:
            right = starting_right

    if valid:
        right-=1

    while longerString[right] == '.':
        print("burada olamaz")
        right-=1

print(longerString)
"""
while(right > 0):
    # print(f"{left}: left:{longerString[left]}, {right}:right: {longerString[right]}, {str(longerString)}")
    left = longerString.index('.')
    temp_right = right
    current_number = longerString[right]
    invalid = False
    while left < right and not invalid:
        temp_left = left
        invalid = False

        while longerString[right] == current_number:
            right-=1
            left+=1
            if longerString[left] != '.':
                invalid = True

        if invalid:
            left = temp_left
        else:
            print(f"Valid {longerString[temp_right]}")
            longerString[temp_left:left], longerString[right + 1 :temp_right+1] = longerString[right + 1:temp_right+1], longerString[temp_left:left]
            break
        left+=1
          while(longerString[right] == '.'):
        right-=1
    while(longerString[left] != '.'):
        left += 1

"""
