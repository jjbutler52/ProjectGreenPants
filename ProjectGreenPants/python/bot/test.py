from combat import flipDigits, isCrit, isImpaled, isImpenetrable, isFumble, isMissfire, successLevel, targetLocation, beastLocation, attack, createResponse, defend, combatRoll, skillRoll, oopsRoll, windsRoll, windsOutcome
import random

# "expected test"
def ext(outcome, description):
    if outcome == False:
        print ("test failure: ")
        print (description)
        quit()

result = combatRoll(47, "John", True, 65)
print(result)

# auto fail
print ("auto fail:")
print (combatRoll(47, "cread", True, 100)) # when skill < 100
print (combatRoll(125, "cread", True, 100)) # when skill > 100
print ("auto fumble:")
print (combatRoll(47, "cread", True, 99)) # fumble!
print (combatRoll(125, "cread", True, 99)) # fumble!

# auto success
print ("auto success:")
print (combatRoll(1, "cread", True, 4)) # when skill lower than roll
print (combatRoll(125, "cread", True, 3)) # when skill > 100

# success
print ("regular success:")
print (combatRoll (120, "cread", True, 94))

# missfire
print ("missfires:")
print (combatRoll (60, "John", True, 66))
print (combatRoll (60, "John", True, 88))
print (combatRoll (60, "John", True, 100))
print (combatRoll (66, "John", True, 66)) # non-missfire
print (combatRoll (66, "John", True, 77)) # non-missfire, fumble

# skills
print ("skills success:")
print (skillRoll (60, "John", 55))
print (skillRoll (60, "John", 60))
print (skillRoll (60, "John", 50))
print (skillRoll (60, "John", 40))
print (skillRoll (60, "John", 30))
print (skillRoll (60, "John", 20))
print (skillRoll (60, "John", 10))
print (skillRoll (60, "John", 1))

print ("skills failure:")
print (skillRoll (40, "John", 44))
print (skillRoll (40, "John", 41))
print (skillRoll (40, "John", 50))
print (skillRoll (40, "John", 60))
print (skillRoll (40, "John", 70))
print (skillRoll (40, "John", 80))
print (skillRoll (40, "John", 90))
print (skillRoll (40, "John", 100))

print ("oops rolls:")
print (oopsRoll ("John", 1))
print (oopsRoll ("John", 20))
print (oopsRoll ("John", 21))
print (oopsRoll ("John", 40))
print (oopsRoll ("John", 41))
print (oopsRoll ("John", 60))
print (oopsRoll ("John", 61))
print (oopsRoll ("John", 70))
print (oopsRoll ("John", 71))
print (oopsRoll ("John", 80))
print (oopsRoll ("John", 81))
print (oopsRoll ("John", 90))
print (oopsRoll ("John", 91))
print (oopsRoll ("John", 100))

print ("\nstarting unit tests...")

ext (isFumble (100, 50), "100 is auto fumble!")
ext (isFumble (99, 50), "99 is auto fumble!")
ext (not isFumble (98, 50), "98 is not a fumble!")
ext (not isFumble (97, 50), "97 is not a fumble!")
ext (not isFumble (96, 50), "96 is not a fumble!")

ext (isCrit (1, 1), "1 is auto crit!")
ext (not isImpenetrable (11, False), "No crit so not impenetrable")
ext (not isImpenetrable (22, True), "Even roll is not impenetrable")
ext (isImpenetrable (11, True), "odd roll is impenetrable")
ext (not isImpenetrable (11, False), "odd roll but was not a crit impenetrable")

ext (isMissfire (100, 50), "100 is an auto missfire!")
ext (isMissfire (88, 50), "88 is missfire!")
ext (isMissfire (66, 50), "66 is a missfire!")
ext (not isMissfire (99, 50), "99 is a fumble but not a missfire!")
ext (not isMissfire (77, 50), "77 is a fumble but not a missfire!")
ext (not isMissfire (44, 50), "44 is NOT a missfire!")

ext (windsOutcome (1) == -30, "wind roll of 1 is -30 to casting and channeling!")
ext (windsOutcome (2) == -10, "wind roll of 2-3 is -10 to casting and channeling!")
ext (windsOutcome (3) == -10, "wind roll of 2-3 is -10 to casting and channeling!")
ext (windsOutcome (4) == 0, "wind roll of 4-7 is +0 to casting and channeling!")
ext (windsOutcome (5) == 0, "wind roll of 4-7 is +0 to casting and channeling!")
ext (windsOutcome (6) == 0, "wind roll of 4-7 is +0 to casting and channeling!")
ext (windsOutcome (7) == 0, "wind roll of 4-7 is +0 to casting and channeling!")
ext (windsOutcome (8) == +10, "wind roll of 8-9 is +10 to casting and channeling!")
ext (windsOutcome (9) == +10, "wind roll of 8-9 is +10 to casting and channeling!")
ext (windsOutcome (10) == +30, "wind roll of 10 is +30 to casting and channeling!")


print ("all tests passed!\n")