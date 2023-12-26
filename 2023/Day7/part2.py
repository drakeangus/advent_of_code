#!/bin/python3
from collections import defaultdict


custom_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
rank_order = ["Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair", "One pair", "High card"]


def GetHandStrength(hand):
    cardCount = defaultdict(int)
    for card in hand:
        cardCount[card] += 1

    best_card_type=""
    max_card_count=0
    for card,count in cardCount.items():
        if card != "J" and count > max_card_count:
            max_card_count = count
            best_card_type = card

    cardCount[best_card_type] += cardCount["J"]
    cardCount.pop("J")
    return CalcScore(cardCount)


def CalcScore(cardCount):
    sets = len(cardCount)

    if sets == 1:
        return "Five of a kind"
    elif sets == 5:
        return "High card"
    elif sets == 4:
        return "One pair"

    for card,count in cardCount.items():
        if count == 4 and sets == 2:
            return "Four of a kind"
        if count == 3 and sets == 2:
            return "Full house"
        if count == 3 and sets == 3:
            return "Three of a kind"

    return "Two pair"


def CompareCards(handA, handB):
    # Should return true if handA beats handB (assuming both have equal type)
    for i in range(0, len(handA)):
        scoreA = custom_order.index(handA[i])
        scoreB = custom_order.index(handB[i])
        
        if  scoreA == scoreB:
            continue
        
        if scoreA < scoreB:
            return True

        return False


def OrderHands(strength, hand, bid):
    global hands

    if len(hands) == 0:
        hands.append((strength, hand, bid))
        return


    for e, play in enumerate(hands):
        currentHandStrength = rank_order.index(strength)
        targetHandStrength = rank_order.index(play[0])

        if currentHandStrength < targetHandStrength:
            hands.insert(e, (strength, hand, bid))
            return
        
        if currentHandStrength > targetHandStrength:
            continue
    
        if currentHandStrength == targetHandStrength:
            if CompareCards(hand, play[1]):
                hands.insert(e, (strength, hand, bid))
                return
            else:
                continue

    hands.append((strength, hand, bid))


hands=[]
for line in open(0):
    hand, bid = line.split()
    strength = GetHandStrength(hand)
    OrderHands(strength, hand, bid)


answer=0
for enum, (strength, hand, bid)  in enumerate(reversed(hands), 1):
    score = int(bid) * enum
    answer += score
    print(f"Hand {hand} : {score} = {int(bid)} x {enum}")

print(f"Answer = {answer}")
