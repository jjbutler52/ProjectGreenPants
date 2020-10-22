from combat import flipDigits, isCrit, isImpaled, isFumble, successLevel, targetLocation, beastLocation, attack, createResponse, defend, combatRoll
import random


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
print (combatRoll(47, "cread", True, 1)) # when skill < 100
print (combatRoll(125, "cread", True, 3)) # when skill > 100
