dial = 50
zeros = 0

input = open("/Users/ewanhuggon/Documents/Projects/input.txt").read().splitlines()

for turn in input:
    if turn[0] == "L":
        rotations = int(turn[1:]) % 100
        dial -= rotations
        if dial < 0:
            dial = 100 + dial
    else:
        rotations = int(turn[1:]) % 100
        dial += rotations
        if dial > 99:
            dial = dial - 100
    if dial == 0:
        zeros += 1  
    
print(zeros)
    

