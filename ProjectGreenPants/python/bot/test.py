from combat import flipDigits, isCrit, isImpaled, isFumble, isMissfire, successLevel, targetLocation, beastLocation, attack, createResponse, defend, combatRoll
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

print ("\nstarting unit tests...")

ext (isFumble (100, 50), "100 is auto fumble!")
ext (isFumble (99, 50), "99 is auto fumble!")
ext (not isFumble (98, 50), "98 is not a fumble!")
ext (not isFumble (97, 50), "97 is not a fumble!")
ext (not isFumble (96, 50), "96 is not a fumble!")

ext (isMissfire (100, 50), "100 is an auto missfire!")
ext (isMissfire (88, 50), "88 is missfire!")
ext (isMissfire (66, 50), "66 is a missfire!")
ext (not isMissfire (99, 50), "99 is a fumble but not a missfire!")
ext (not isMissfire (77, 50), "77 is a fumble but not a missfire!")
ext (not isMissfire (44, 50), "44 is NOT a missfire!")

print ("all tests passed!\n")