import random

def attack (skill, username):
  #  result = f"[ATT] @{username} [SL]:+5  [Roll]:18 [Bi/Quad]: L-Leg/BL-Leg"
    return combatRoll(skill, username, True)

def defend (skill, username):
    result = f"[DEF] @{username} [SL]:+5  [Roll]:18 [Bi/Quad]: L-Leg/BL-Leg"
    return result

def combatRoll(skill,username, wasAttack):
    roll = 0
    sl = 0
    location = 0

    roll = random.randint(0 ,100)
    sl = successLevel(skill, roll)
    location = flipDigits(roll)

    isCrit(roll, sl)
    isImpaled(roll, sl)
    isFumble(roll, sl)

    wasCrit = isCrit(roll, sl)
    wasImpaled = isImpaled(roll, sl)
    wasFumble = isFumble(roll, sl)

    response = createResponse(wasAttack, wasFumble, wasCrit, wasImpaled, sl, roll, location, username)
    print(response)
    return roll 


def flipDigits(flippee):
    ones = 0
    tens = 0
    result = 0

    ones = flippee % 10
    tens = flippee / 10
    result = (ones * 10) + tens
        
    return int (result)

def isCrit(roll, SL):
    if roll % 11 == 0 and SL >= 0:
        return True
    else:
        return False

def isImpaled(roll, SL):
    if roll % 10 == 0 and SL >= 0:
        return True
    else:
        return False

def isFumble(roll, SL):
    if roll % 11 == 0 and SL < 0:
        return True
    else: 
        return False

def successLevel(skill, roll):
    success = 0
    roll = roll / 10
    skill = skill / 10

    success = skill - roll

    return success

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



def createResponse(wasAttack, wasFumble, wasCrit, wasImpaled, SL, roll, location, username):
    #target
    #beast
   # result
   

    if wasAttack:
        result = f"[ATT @{username}]" 
    else:
        result += f"[DEF @{username}]"
    
    if SL > 0:
        result += "[SL:+" + SL + "] "
    else:
        result += "[SL:" + SL + "] "

    if wasCrit:
        result += "{CRIT!} "
    
    if wasImpaled:
        result += "{IMPALE!} "

    if wasFumble:
        result += "{FUMBLE!} "
    elif not wasFumble:
        target = targetLocation(location)
        beast = beastLocation(location)
        result += "[Bi:" + target + "|Quad:" + beast + "]"
    
    result += " [Roll:" + roll +"] "
    return result


