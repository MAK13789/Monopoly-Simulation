import random
board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_pos = {0: "Go", 1: "Old Kent Road", 2: "Community Chest 1", 3: "Whitechapel Road", 4: "Income Tax", 5: "Kings Cross Station", 6: "The Angel Islington", 7: "Chance 1", 8: "Euston Road", 9: "Pentonville Road", 10: "Jail", 11: "Pall Mall", 12: "Electric Company", 13: "White Hall", 14: "North Humberland Avenue", 15: "Marylebone Station", 16: "Bow Street", 17: "Community Chest 2", 18: "Marlborough Street", 19: "Vine Street", 20: "Free Parking", 21: "Strand", 22: "Chance 2", 23: "Fleet Street", 24: "Trafalgar Square", 25: "Fenchurch Street Station", 26: "Leicester Square", 27: "Coventry Street", 28: "Water Works", 29: "Piccadilly", 30: "Go to Jail", 31: "Regent Street", 32: "Oxford Street", 33: "Community Chest 3", 34: "Bond Street", 35: "Liverpool Street Station", 36: "Chance 3", 37: "Park Lane", 38: "Super Tax", 39: "Mayfair"}  
community_chest_cards = [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #1 means advance to go, 2 means go to jail, 0 means everything else
random.shuffle(community_chest_cards)
chance_cards = [1, 2, 3, 4, 5, 0, 0, 6, 7, 0, 0, 8, 9, 0, 0, 0]#1 means advance to go, 2 means trafalgar square, 3 means pall mall, 4 means nearest utility, 5 means nearest railroad, 6 means go back 3 spaces, 7 means go to jail, 8 means kings cross, 9 means mayfair 
random.shuffle(chance_cards)
init = 0
pos = 0
check_1 = []
check_2 = []
community_chest_count = 0
chance_count = 0
while (init < 10000000):
    die_1 = random.randint(1, 6)
    check_1.append(die_1)
    die_2 = random.randint(1, 6)
    check_2.append(die_2)
    if ((pos == 2) or (pos == 17) or (pos == 33)):
        temp_6 = community_chest_count % 17
        if (community_chest_cards[temp_6] == 1):
            pos = 0
            community_chest_count = community_chest_count + 1
        if (community_chest_cards[temp_6] == 2):
            pos = 10
            community_chest_count = community_chest_count + 1
    if ((pos == 7) or (pos == 22) or (pos == 36)):
        temp_7 = chance_count % 16
        if (chance_cards[temp_7] == 1):
            pos = 0
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 2):
            pos = 24
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 3):
            pos = 11
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 4):
            temp_8 = abs(12 - pos)
            temp_9 = abs(28 - pos)
            if (temp_9 < temp_8):
                pos = 28
            if (temp_8 < temp_9):
                pos = 12
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 5):
            compare = []
            temp_10 = abs(5 - pos)
            compare.append(temp_10)
            temp_11 = abs(15 - pos)
            compare.append(temp_11)
            temp_12 = abs(25 - pos)
            compare.append(temp_12)
            temp_13 = abs(35 - pos)
            compare.append(temp_13)
            temp_14 = compare.index(min(compare))
            if (temp_14 == 0):
                pos = 5
            if (temp_14 == 1):
                pos = 15
            if (temp_14 == 2):
                pos = 25
            if (temp_14 == 3):
                pos = 35
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 6):
            pos = (pos - 3) % 40
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 7):
            pos = 10
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 8):
            pos = 5
            chance_count = chance_count + 1
        if (chance_cards[temp_7] == 9):
            pos = 39
            chance_count = chance_count + 1
    if (pos == 30):
        pos = 10
    else:
        if (init >= 3):
            if ((check_1[init] == check_2[init]) & (check_1[init-1] == check_2[init-1]) & (check_1[init-2] == check_2[init-2])):
                pos = 10
            else:
                move = die_1 + die_2
                pos = (pos + move) % 40
        else:
            move = die_1 + die_2
            pos = (pos + move) % 40
    temp = board[pos]
    board[pos] = temp + 1
    init = init + 1
print (board)
temp_1 = sum(board)
for i in range(len(board)):
    temp = board[i] / temp_1
    temp = temp * 100
    percentage[i] = temp
print (percentage)
temp_2 = (percentage.index(max(percentage)))
print (temp_2)
print (board_pos[temp_2])
temp_3 = (percentage.index(min(percentage)))
print (temp_3)
print (board_pos[temp_3])
'''
check = 0
while (check < 39):
    temp_4 = board.index(max(board))
    temp_5 = board_pos[temp_4]
    print (temp_5)
    board.pop(temp_4)
    check = check + 1
'''
check = 0
while (check < 40):
    temp_4 = board.index(max(board))
    temp_5 = board_pos[temp_4]
    print (temp_5)
    board[temp_4] = 0
    check = check + 1
#results: jail is always the most visited and the next most are the red and orange properties explain that it works park lane is the worst property

