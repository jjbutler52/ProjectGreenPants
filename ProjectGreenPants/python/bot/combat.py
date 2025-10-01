import random

def attack (skill, username):
    return combatRoll(skill, username, True, random.randint(1,100))

def defend (skill, username):
    return combatRoll(skill, username, False, random.randint(1,100))

def probability (characteristic, skill):
    # 1 - (1 - P)^N
    P = skill / 10.0
    N = characteristic
    d = 1 - pow (1 - P, N)
    p = (d * 100)
    return f'{p:10.1f}' + '%'

def skill (skill, username):
    return skillRoll(skill, username, random.randint(1,100))

def multiskill (skill, username, count):
    rolls = []
    for r in range (count):
        rolls.append (random.randint(1,100))
    return multiskillRoll(skill, username, rolls)

def oops (username):
    return oopsRoll(username, random.randint(1,100))

def winds (username):
    return windsRoll(username, random.randint(1, 10))

def combatRoll(skill,username, wasAttack, roll):
    sl = successLevel(skill, roll)
    location = flipDigits(roll)

    wasCrit = isCrit(roll, skill)
    wasImpenetrable = isImpenetrable (roll, wasCrit)
    wasImpaled = isImpaled(roll, skill)
    wasFumble = isFumble(roll, skill)
    wasMissfire = isMissfire(roll, skill)
    wasAutoFail = isAutoFail (roll)
    wasAutoSuccess = isAutoSuccess (roll)

    response = createResponse(wasAttack, wasFumble, wasCrit, wasImpaled, wasImpenetrable, wasMissfire, wasAutoFail, wasAutoSuccess, sl, roll, location, username)
    return response 

def multiskillRoll(skill,username, rolls):
    response = "[multiple skill rolls]\n\n"
    critCount = 0
    fumbleCount = 0
    successCount = 0
    failCount = 0
    for roll in rolls:
        sl = successLevel(skill, roll)
        wasCrit = isCrit(roll, skill)
        wasFumble = isFumble(roll, skill)
        wasAutoFail = isAutoFail (roll)
        wasAutoSuccess = isAutoSuccess (roll)   

        if wasCrit == True:
            critCount += 1
        if wasFumble == True:
            fumbleCount += 1
        if sl >= 0:
            successCount += 1
        else:
            failCount += 1

        response += "\t\t" + createSkillResponse(wasFumble, wasCrit, wasAutoFail, wasAutoSuccess, sl, roll, skill, username)
        response += "\n"

    response += "\n"
    response += "[pass: " + str (successCount) + "\tfail: " + str (failCount) + "]"
    response += "\t\t\t[crits: " + str (critCount) + "\tfumbles: " + str (fumbleCount) + "]"
    return response

def skillRoll(skill,username, roll):
  
    sl = successLevel(skill, roll)
    wasCrit = isCrit(roll, skill)
    wasFumble = isFumble(roll, skill)
    wasAutoFail = isAutoFail (roll)
    wasAutoSuccess = isAutoSuccess (roll)

    response = createSkillResponse(wasFumble, wasCrit, wasAutoFail, wasAutoSuccess, sl, roll, skill, username)
    return response 

def flipDigits(flippee):
    ones = 0
    tens = 0
    result = 0

    ones = flippee % 10
    tens = flippee / 10
    result = (ones * 10) + tens

    return int (result)

def isCrit(roll, skill):
    if roll == 99:
        return False # 99 is auto fail
    elif roll % 11 == 0 and skill >= roll:
        return True
    elif roll == 1:
        return True # 1 is auto crit
    else:
        return False

def isImpenetrable (roll, wasCrit):
    if wasCrit and roll != 1 and roll % 2 != 0:
        return True
    else:
        return False

def isImpaled(roll, skill):
    if roll == 100:
        return False # 100 is auto fail
    elif roll % 10 == 0 and skill >= roll:
        return True
    else:
        return False

def isFumble(roll, skill):
    if (roll % 11 == 0 and skill < roll):
        return True
    elif roll == 99 or roll == 100:
        return True # 99/100 is auto fumble
    else:
        return False

# misfire is an even numbered fumble
def isMissfire(roll, skill):
    if isFumble (roll, skill) and roll % 2 == 0:
        return True
    else: 
        return False

def isAutoFail(roll):
    return roll >= 96

def isAutoSuccess(roll):
    return roll <= 5

def successLevel(skill, roll):
    rollTens = roll / 10
    skillTens = skill / 10

    success = int(skillTens) - int(rollTens)
    if success == 0 and roll > skill:
        success = -1

    if isAutoFail(roll):
        success = min(-1, success)

    if isAutoSuccess(roll):
        success = max(1, success)

    return int(success)

def targetLocation(location):
    if location < 10:
        return "Head"

    elif location < 25:
        return "Off Arm"

    elif location < 45:
        return "Main Arm"

    elif location < 80:
        return "Body"

    elif location < 90:
        return "L-Leg"

    elif location <= 100:
        return "R-Leg"

    else:
        return "ERROR"

def beastLocation(location):
    if location < 17:
        return "Head"

    elif location < 57:
        return "Body"

    elif location < 68:
        return "FL-Leg"

    elif location < 79:
        return "FR-Leg"

    elif location < 90:
        return "BL-Leg"

    elif location <= 100:
        return "BR-Leg"

    else:
        return "ERROR"

def createResponse(wasAttack, wasFumble, wasCrit, wasImpaled, wasImpenetrable, wasMissfire, wasAutoFail, wasAutoSuccess, SL, roll, location, username):

    if wasAttack:
        result = f"[ATT @{username}] " 
    else:
        result = f"[DEF @{username}] "

    if SL > 0:
        result += "[SL:+" + str(int(SL)) + "] "
    else:
        result += "[SL:" + str(int(SL)) + "] "

    if wasAutoSuccess:
        result += "{AUTO SUCCESS} "

    if wasAutoFail:
        result += "{AUTO FAIL} "

    if wasCrit:
        result += "{CRIT!} "

    if wasImpaled:
        result += "{IMPALE!} "

    if wasImpenetrable:
        result += "{IMPENETRABLE!} "

    if wasFumble and wasMissfire:
        result += "{MISSFIRE/FUMBLE!} "
    elif wasFumble:
        result += "{FUMBLE!} "
    elif not wasFumble:
        target = targetLocation(location)
        beast = beastLocation(location)
        result += "[Bi:" + target + "|Quad:" + beast + "]"

    result += " [Roll:" + str(roll) +"] "
    return result

def skillOutcome (SL, roll, skill):
    if SL >= 6:
        return "[Astounding Success] : The result is as good as it can be, perhaps with extra luck and fortunate coincidences thrown in!"
    if SL >= 4:
        return "[Impressive Success] : You achieve your goal with style, exceeding your expectations."
    if SL >= 2:
        return "[Success] : You achieve a solid success."
    if SL >= 0:
        return "[Marginal Success] : You more or less achieve what you intend, but imperfectly, and perhaps with an unpredictable side effect."
    if SL >= -1:
        return "[Marginal FAILURE] : You marginally fail, perhaps accomplishing a portion of what you intended."
    if SL >= -3:
        return "[FAILURE] : You just plain do it wrong."
    if SL >= -5:
        return "[Impressive FAILURE] : Not only do you mess up, but you also cause additional things to go wrong."
    return " [Astounding FAILURE] : Everything goes wrong in the worst possible way. The GM will likely add to your woes with unanticipated consequences of your actions. Surely no-one is this unlucky; you have clearly offended the gods."

def createSkillResponse(wasFumble, wasCrit, wasAutoFail, wasAutoSuccess, SL, roll, skill, username):

    result = f"[SKILL @{username}] "

    if SL > 0:
        result += "[SL:+" + str(int(SL)) + "] "
    else:
        result += "[SL:" + str(int(SL)) + "] "

    if wasAutoSuccess:
        result += "{AUTO SUCCESS} "

    if wasAutoFail:
        result += "{AUTO FAIL} "

    if wasCrit:
        result += "{CRIT!} "

    if wasFumble:
        result += "{FUMBLE!} "

    result += "[Roll:" + str(roll) +"]"
    result += "\n" + skillOutcome (SL, roll, skill)
    return result

def windsRoll(username, roll):
    result = f"[Winds of Magic! @{username}] "
    result += "[Roll:" + str(roll) +"] : "
    outcome = windsOutcome (roll)
    if outcome >= 0:
        result += "+" + str (windsOutcome (roll)) + " to Casting and Channeling."
    else:
        result += str (windsOutcome (roll)) + " to Casting and Channeling."
    return result

def windsOutcome(roll):
    if roll == 1:
        return -30
    if roll == 2 or roll == 3:
        return -10
    if roll == 4 or roll == 5 or roll == 6 or roll == 7:
        return 0
    if roll == 8 or roll == 9:
        return +10
    if roll == 10:
        return 30
    return 0

def oopsRoll(username, roll):
    result = f"[OOPS! @{username}] "
    result += "[Roll:" + str(roll) +"] : "
    result += oopsOutcome (username, roll)
    return result

def oopsOutcome(username, roll):
    if roll <= 20:
        return "You catch a part of your anatomy (we recommend you play this for laughs) — lose 1 Wound, ignoring Toughness Bonus or Armour Points."
    if roll <= 40:
        return "Your melee weapon jars badly, or ranged weapon malfunctions or slightly breaks – your weapon suffers 1 Damage. Next round, you will act last regardless of Initiative order, Talents, or special rules as you recover (see page 156)."
    if roll <= 60:
        return "Your manoeuvre was misjudged, leaving you out of position, or you lose grip of a ranged weapon. Next round, your Action suffers a penalty of –10."
    if roll <= 70: 
        return "You stumble badly, finding it hard to right yourself. Lose your next Move."
    if roll <= 80: 
        return "You mishandle your weapon, or you drop your ammunition. Miss your next Action."
    if roll <= 90: 
        return "You overextend yourself or stumble and twist your ankle. Suffer a Torn Muscle (Minor) injury (see page 179). This counts as a Critical Wound."
    if roll <= 100: 
        return "You completely mess up, hitting 1 random ally in range using your rolled units die to determine the SL of the hit. If that’s not possible, you somehow hit yourself in the face and gain a Stunned Condition (see page 169)."

