def attack (skill, username):
    result = f"[ATT] @{username} [SL]:+5  [Roll]:18 [Bi/Quad]: L-Leg/BL-Leg"
    return result

def defend (skill, username):
    result = f"[DEF] @{username} [SL]:+5  [Roll]:18 [Bi/Quad]: L-Leg/BL-Leg"
    return result

def combatRoll(skill, wasAttack):
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

    response = printAttack(wasAttack, wasFumble, wasCrit, wasImpaled, sl, roll, location)
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


    
