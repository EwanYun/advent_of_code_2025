dial = 50

zeros = 0
turns = ['L522']

f = open("/Users/ewanhuggon/Documents/Projects/input.txt").read().splitlines()

for turn in f:
    if turn[0] == "L":
        print(dial)
        print(turn)
        rotations = int(turn[1:]) % 100
        print(rotations)
        dial -= rotations
        if dial < 0:
            dial = 100 + dial
        print(dial)
    else:
        print(dial)
        print(turn)
        rotations = int(turn[1:]) % 100
        print(rotations)
        dial += rotations
        if dial > 99:
            dial = dial - 100
        print(dial)
    if dial == 0:
        zeros += 1  
    print(zeros)
    

